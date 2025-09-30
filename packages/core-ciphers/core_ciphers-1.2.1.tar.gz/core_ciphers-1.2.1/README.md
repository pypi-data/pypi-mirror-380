# core-ciphers
_______________________________________________________________________________

This project/library contains common elements related to ciphers...


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
python manager.py run-test
python manager.py run-coverage
```

## Security

### Cryptographic Library

This project uses **`pycryptodome`** (version >=3.21.0) for cryptographic operations, not the deprecated `pycrypto` library.

**Important Note:** Security scanners like `bandit` may report false positives (B413 warnings) when scanning this codebase. This occurs because both `pycrypto` (deprecated) and `pycryptodome` (actively maintained) use the same `Crypto` import namespace, causing scanners to incorrectly flag the imports as deprecated.

**Verification:**
- Check `pyproject.toml` dependencies: `pycryptodome>=3.21.0`
- `pycryptodome` is actively maintained and regularly updated
- It is the recommended drop-in replacement for the deprecated `pycrypto`

The B413 bandit warnings can be safely ignored as they are false positives.
