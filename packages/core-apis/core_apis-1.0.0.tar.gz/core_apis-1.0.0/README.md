# core-apis
_______________________________________________________________________________

This project/library contains useful elements related 
to APIs and provides basic structures to speed up 
the implementation of an API service using
the FastApi framework as base...


## How to use it

### Create the virtual environment
```shell
virtualenv .venv
source .venv/bin/activate
pip install core-apis
```

The simple way to spin up the FastAPI server and running it
locally using `uvicorn`...
```python
# -*- coding: utf-8 -*-
from core_apis.api import server
server.run()
```

Adding custom routers...
```python
# -*- coding: utf-8 -*-

from fastapi import APIRouter

from core_apis.api import server
from core_apis.api.routers import add_router

router = APIRouter()
add_router(router)

@router.get(path="/server_status")
def new_router():
    return {"status": "OK"}

server.run()
```

For an example of the structure of a production-ready project 
check: https://gitlab.com/bytecode-solutions/examples/fastapi-project


## Execution Environment

### Install libraries
```shell
pip install --upgrade pip
pip install virtualenv
```

### Create the Python Virtual Environment.
```shell
virtualenv --python=python3.11 .venv
```

### Activate the Virtual Environment.
```shell
source .venv/bin/activate
```

### Install required libraries.
```shell
pip install .
pip install .[test]
```

### Check tests and coverage...
```shell
python manager.py run-tests
python manager.py run-coverage
```

### Run FastAPI server...
```shell
python manager.py run-api
```
