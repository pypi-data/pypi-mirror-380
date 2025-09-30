# -*- coding: utf-8 -*-
# #############################################################################
# Copyright (C) 2025 manatlan manatlan[at]gmail(dot)com
#
# MIT licence
#
# https://github.com/manatlan/reqman4
# #############################################################################
import os
import sys
import asyncio
import logging
import traceback
import tempfile
import webbrowser
from itertools import chain 
import glob

# pypi packages
import click
from colorama import init, Fore, Style
from urllib.parse import unquote
import dotenv; dotenv.load_dotenv()

# reqman imports
from . import __version__ as VERSION
from . import common
from . import scenario
from . import env
from . import output

logger = logging.getLogger(__name__)
init()

def colorize(color: str, t: str) -> str|None:
    return (color + Style.BRIGHT + str(t) + Fore.RESET + Style.RESET_ALL if t else None)

cy = lambda t: colorize(Fore.YELLOW, t)
cr = lambda t: colorize(Fore.RED, t)
cg = lambda t: colorize(Fore.GREEN, t)
cb = lambda t: colorize(Fore.CYAN, t)
cw = lambda t: colorize(Fore.WHITE, t)


class Output:
    def __init__(self,switchs:tuple):
        self.switchs = switchs
        self.nb_tests=0
        self.nb_tests_ok=0
        self.nb_req=0
        self.htmls=[ output.generate_base() ]
        self.error:Exception|None = None

    @property
    def nb_tests_ko(self):
        return self.nb_tests - self.nb_tests_ok

    def begin_scenario(self,file:str):
        file = os.path.relpath(file)
        print(cb(f"--- RUN {file} ---"))
        self.htmls.append( output.generate_section(file) )

    def write_a_test(self,r:common.Result):
        if r:
            self.nb_req+=1
            print(f"{cy(r.request.method)} {unquote(str(r.request.url))} -> {cb(r.response.status_code) if r.response.status_code else cr('X')}")
            for tr in r.tests:
                color = {True:cg,False:cr,None:cr}[tr.ok]
                print(" -",color(str(tr)),":", tr.text)
                self.nb_tests += 1
                if tr.ok:
                    self.nb_tests_ok += 1
            print()
            self.htmls.append( output.generate_request(r) )
            
    def write_an_error(self,ex:Exception):
        self.htmls.append( output.generate_error(ex) )
        self.error = ex


    def end_scenario(self):
        pass

    def end_tests(self):
        self.htmls.append( output.generate_final( self.switchs, self.nb_tests_ok, self.nb_tests, self.error) )

        if self.error:
            print(cr(f"SCENARIO ERROR: {self.error}"))
        else:
            if self.nb_tests_ko==0:
                print(cg(f"{self.nb_tests_ok}/{self.nb_tests}"))
            else:
                print(cr(f"{self.nb_tests_ok}/{self.nb_tests}"))


    def open_browser(self):

        with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html', encoding="utf-8") as f:
            f.write("\n".join(self.htmls))
            temp_html_path = f.name

        # Ouvre le fichier HTML dans le navigateur par défaut
        webbrowser.open(f'file://{os.path.abspath(temp_html_path)}')        



class ExecutionTests:
    def __init__(self,files:list,vars:dict={},is_debug=False, compatibility:int=0):
        self.files=common.expand_files(files)
        self.is_debug=is_debug
        self.env=None

        # init the conf
        reqman_conf = common.guess_reqman_conf(self.files)
        if reqman_conf is None:
            self.conf_global = common.Conf({})
        else:
            print(cy(f"Using conf : {os.path.relpath(reqman_conf)}"))
            self.conf_global = common.Conf(common.load_reqman_conf(reqman_conf))

        # init with the switchs from conf
        self.switchs = self.conf_global.switchs

        # update with vars from command line
        self.conf_global.update(vars)


        self.scenarios=[]
        # merge the switchs from others files
        for f in self.files:
            s=scenario.Scenario(f, compatibility)
            self.switchs.update( s._ys.conf.switchs )
            self.scenarios.append(s)



    async def execute(self,*switchs) -> Output:
        """ Run all tests in files """

        # apply switchs for global conf (aka reqman_conf)
        self.conf_global.apply(*switchs)

        # create the real env
        self.env = env.Env( **self.conf_global )

        output = Output(switchs)

        for idx,scenar in enumerate(self.scenarios):
            output.begin_scenario(scenar.file_path)

            # update conf of scenar into env
            self.env.update( scenar.conf.apply(*switchs) )
    
            try:
                async for req in scenar.execute( self.env, with_begin=(idx==0), with_end=(idx==len(self.scenarios)) ):
                    output.write_a_test(req)
            except common.ExeError as ex:
                if self.is_debug:
                    traceback.print_exc()

                output.write_an_error(ex)

                break # stop execution process !!!!

            output.end_scenario()

        output.end_tests()
        return output




#- ----------------------------------------------------------

@click.group()
def cli():
    pass


def patch_docstring(f):
    f.__doc__+= f"Version:{VERSION}"
    return f


def options_from_files(opt_name: str):
    options_from_files.error=None
    files = [i for i in sys.argv[1:] if not i.startswith("-")]  # guess files
    files_expanded = []
    for i in files:
        expanded = glob.glob(i, recursive=True)
        if not expanded and not i.startswith( ("http:","https:") ):
            #raise click.FileError(i, hint="File not found")
            options_from_files.error = f"File not found '{i}'"
            return lambda f:f

        files_expanded.extend(expanded if expanded else [i])

    files = common.expand_files([i for i in files_expanded if os.path.exists(i)])  # skip http files

    if not files:
        #raise click.MissingParameter(param_type='argument', param=click.Argument(['files']))
        options_from_files.error = "Missing argument 'FILES...'"
        return lambda f:f

    reqman_conf = common.guess_reqman_conf(files)
    if reqman_conf:
        files = [reqman_conf] + files
    d = {}
    for i in files:
        try:
            content = common.yload(open(i, "rb"))
        except Exception as e:
            options_from_files.error = f"File '{i}' is not yaml : {e}"
            return lambda f:f            
        if isinstance(content, common.YDict):
            d.update(common.Conf(content).switchs)

    ll = [dict(name=k, switch=f"--{k}", help=v.get("doc", "???")) for k, v in d.items()]

    def decorator(function):
        for p in reversed(ll):
            click.option(
                p['switch'], opt_name,
                is_flag=True,
                flag_value=p['name'],
                required=False,
                help=p['help'],
                multiple=True
            )(function)
        return function
    return decorator
options_from_files.error=None

@cli.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.argument('files', nargs=-1, required=True ) #help="Scenarios yml/rml (local or http)"
@options_from_files("switchs")
@click.option('-d',"is_debug",is_flag=True,default=False,help="Debug mode")
@click.option('-s',"vars",help="Set variables (ex: -s token=DEADBEAF,id=42)")
@click.option('-i',"is_shebang",is_flag=True,default=False,help="Interactive mode (with shebang)")
@click.option('-o',"open_browser",is_flag=True,default=False,help="Open a report in an html page")
@click.option('-c',"compatibility",is_flag=True,default=False,help="Accept old reqman3 scenarios")
@click.option('-cc',"comp_convert",is_flag=True,default=False,help="Accept old reqman3 and generate new version")
@click.pass_context
@patch_docstring
def command(ctx:click.Context,**p):
    """Test an http service with pre-made scenarios, whose are simple yaml files
(More info on https://github.com/manatlan/reqman4) """
    if options_from_files.error:
        # ctx.fail( options_from_files.error )
        click.echo( options_from_files.error )
        ctx.exit(-1)
    else:
        try:
            rc = reqman(ctx,**p)
        except Exception as ex:
            # everything that happen here is an real bug/error
            # and will need a fix !
            if p["is_debug"]:
                traceback.print_exc()
            print(cr(f"BUG ERROR: {ex}"))
            rc = -1
        ctx.exit( rc )

def reqman(ctx, files:list,switchs:list|None=None,vars:str="",is_debug:bool=False,is_shebang:bool=False,open_browser:bool=False,compatibility:bool=False,comp_convert:bool=False) -> int:
    if not switchs:
        switchs=[]
    else:
        switchs=list(switchs)

    if is_debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.ERROR)

    files = list(chain.from_iterable([glob.glob(i,recursive=True) if not i.startswith("http") else [i] for i in files]))
    logger.info("Files: %s",files)
    if compatibility:
        comp_mode=1
    elif comp_convert:
        comp_mode=2
    else:
        comp_mode=0

    if vars:
        dvars = dict( [ i.split("=",1) for i in vars.split(",") if "=" in i ] )
    else:
        dvars = {}

    if is_shebang and len(files)==1:

        with open(files[0], "r") as f:
            first_line = f.readline().strip()
        if first_line.startswith("#!"): # things like "#!reqman -e -d" should work
            options = first_line.split(" ")[1:]        
            print(cy(f"Use shebang {' '.join(options)}"))
            cmd,*fuck_all_params = sys.argv
            sys.argv=[ cmd, files[0] ] + options
            logger.info("USE SHEBANG: %s",sys.argv)
            return command() #redo click parsing !

    r = ExecutionTests( files,dvars, is_debug, comp_mode)
    if r.switchs and not switchs:
        # when switchs configured, and no switch in command line
        # defaulting to the first one
        default = list(r.switchs.keys())[0]
        logger.info("No switch in commandline, set default to %s",default)
        switchs.append( default )
        
    o = asyncio.run(r.execute(*switchs))

    if is_debug:
        print(cy("Environment:"))
        print(r.env)

    if o.error:
        rc = -1
    else:
        rc = o.nb_tests_ko

    if open_browser:
        o.open_browser()

    return rc



    
