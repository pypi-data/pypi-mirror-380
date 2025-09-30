# Reqman4

<a href="https://pypi.org/project/reqman4/">
    <img src="https://badge.fury.io/py/reqman4.svg" alt="Package version">
</a>


A complete rewrite of [reqman](https://github.com/manatlan/reqman). __It's a **prototype/poc**__ ! Don't know yet if it will replace the original, but I wanted to have a new/cleaner/simpler version, 
with all good ideas from the original. 

**MAJOR REASONS**: This prototype is more python based for vars & tests, and can display html in http-verb's doc (to be able to make human readable html reports). Syntax is simpler/cleaner (to be able to have a json-schema to valid yml/rml). And debugging is simpler. Switch mechanism is simpler (and no more trouble with defaults, coz the first switch is selected by default). Reqman conf is now "reqman.yml".

Currently, the package provide a `rq` command (but will be `reqman` in the future)

Here is the [JSON SCHEMA](https://github.com/manatlan/reqman4/blob/main/schema.json) of the new scenario (DSL)).

Major technical differences :
- licence gnu gpl v2 -> MIT
- "uv" & (a lot) simpler (less features)
- use httpx !
- options are inverted (--i -> -i & (switch) -dev --> --dev)
- step operator is always in uppercase (SET, CALL, 'VERB-HTTP' ).
- reqman.conf -> reqman.yml, renamed !
- switch mechanism based on "--key" in reqman.yml / scenars ... first one will be the default
- scenars(*.yml) & reqman.yml are yaml/dict only !
- scenars must(/can for compat) have a "RUN:" section (others keys are the global env)
- tests are simple python statements
- no break!
- no if 
- no more .BEGIN/.END
- no more RMR
- no more comparison side by side
- no more XML testing (may change)
- no more junit.xml output (may change)

Here is a valid scenario, which give you an overview :
[scenario.yml](https://github.com/manatlan/reqman4/blob/main/scenario.yml)

If you use [uvx](https://docs.astral.sh/uv/guides/tools/), you cant test this scenario in your context :

    uvx reqman4 https://raw.githubusercontent.com/manatlan/reqman4/refs/heads/main/scenario.yml -o

It will open an html report in your default browser, and you can easily check what's going ...

## From github

### to test command line

    uvx --from git+https://github.com/manatlan/reqman4 rq --help

### to run a scenario

    uvx --from git+https://github.com/manatlan/reqman4 rq scenario.yml -o

## From pypi

### to test command line

    uvx reqman4 --help

### to run a scenario with a local scenario

    uvx reqman4 scenario.yml -o


#### For [jules](https://jules.google.com/)

This project use "uv":

 - use "uv sync --dev" to setup the ".venv" 
 - use "uv run pytest" to validate all unittests

## reqman4 built with nuitka
To test, create file `cmdline.py`
```python3
from src.reqman4 import main
if __name__=="__main__":
    main.command()
```
and in console:
```
uv pip install nuitka
uv run nuitka cmdline.py 
```
it will produce a executable `cmdline.bin`, which works !

## Majors changes from reqman3

If you come from reqman v3

### rename `reqman.conf` to `reqman.yml`

now, the conf is in an yml file

### translate "switchs"

```yaml
...
switchs:
    env1:
        doc: test the env 1
        root: http://localhost
...
```
to
```yaml
...
--env1:
    doc: test the env 1
    root: http://localhost
...
```

It's simpler, clearer ... and the first one will be auto-selected (if nos supplied) as the default one !

### everything in `<<var>>` or `{{var}}` is python3 evaluated

no more "own substitution language" ... everything is python3

```yaml
...
- GET: /path?var=<<value|method>>
  doc: test
...
```
to
```yaml
...
- GET: /path?var=<<method(value)>>
  doc: test
...
```

### tests are python3 evaluated

no more "own test language" ... everything is python3

```yaml
...
- GET: /path
  tests:
    - json.value: "toto"
...
```
to
```yaml
...
- GET: /path
  tests:
    - R.json.value == "toto"
...
```

`R` is always the last http response.

### "call" is now "CALL"

todo ...

### no more "save" in http or call

use a new step `SET`, like that

```yaml
...
- GET: /path
  tests:
    - R.json.value == "toto"

- SET:
    saved_value: <<R.json.value>>
...
```
