# core-auth
_______________________________________________________________________________

This project/library contains common elements related to 
authentication & authorization...


## Execution Environment

### Install libraries
```shell
pip install --upgrade pip
pip install virtualenv
```

### Create the Python Virtual Environment.
```shell
virtualenv --python={{python-version}} .venv
virtualenv --python=python3.11 .venv
```

### Activate the Virtual Environment.
```shell
source .venv/bin/activate
```

### Install required libraries.
```shell
pip install .
```

### Check tests and coverage...
```shell
python manager.py run-tests
python manager.py run-coverage
```

## Current implementations

### JwtToken
This is a wrapper to simplify the encoding and
decoding process for JWT tokens using PyJWT library.

Example...
```python
# -*- coding: utf-8 -*-

from core_auth.auth.jwt_token.jwt_auth import JwtToken 

client = JwtToken(private_key="S3cr3t")
token = client.encode(subject="SomeSubject")
print(client.decode(token))
```
