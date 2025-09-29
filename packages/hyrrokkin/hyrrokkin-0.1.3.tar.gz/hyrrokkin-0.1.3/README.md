# hyrrokkin

```
 _                               _     _     _
| |__   _   _  _ __  _ __  ___  | | __| | __(_) _ __
| '_ \ | | | || '__|| '__|/ _ \ | |/ /| |/ /| || '_ \
| | | || |_| || |   | |  | (_) ||   < |   < | || | | |
|_| |_| \__, ||_|   |_|   \___/ |_|\_\|_|\_\|_||_| |_|
        |___/
```

A lightweight asynchronous directed acyclic graph (DAG) execution engine for Python (CPython) and Javascript (Deno)

* define packages of nodes using the python or javascript package API
* create topologies which link nodes together using the python topology API
* run topologies using the python topology API or CLI
* attach clients to communicate with nodes while a topology is running 

## Installation Options

Hyrrokkin supports linux for python versions >= 3.11

Installation without dependencies (no support for YAML import/export, JSON schema checking):

```
pip install hyrrokkin
```

Installation with optional dependencies for YAML import/export:

```
pip install hyrrokkin[YAML]
```

Installation with optional dependencies for JSON schema validation:

```
pip install hyrrokkin[VALIDATION]
```

Installation with all optional dependencies

```
pip install hyrrokkin[VALIDATION,YAML]
```

To run topologies using the javascript engine, install deno - https://deno.com/

## Documentation:

https://visualtopology.org/docs/hyrrokkin

## Unit tests:

### Python unit tests

These cover the hyrrokkin CLI and API, the python engine API, and the execution of textgraph topologies in various python and javascript engine configurations

Deno needs to be installed.

Create a fresh python environment (using python 3.11 or later), then... 

```
git clone https://codeberg.org/visual-topology/hyrrokkin.git
cd hyrrokkin
pip install -e .
pip install pytest
pip install pyyaml jsonschema
pytest
```

These cover the parts of the javascript engine APIs

```
cd test/javascript/unit_tests
./run_all.sh
```

### Building Documentation

Documentation is built using mkdocs which can be installed using:

```
pip install mkdocs
python -m pip install "mkdocstrings[python]"
python -m pip install mkdocs-material
```

Additional documentation for javascript APIs is buit using JSDoc - https://github.com/jsdoc/jsdoc

To build documentation:

```
cd docs
./build.sh
```



