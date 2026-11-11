# AI Chat API

## Features

_(TODO: list the features here.)_

## Install Python Locally with `pyenv`

```bash
curl https://pyenv.run | bash
```

## Setup

### 1. Install `virtualenv` (if not already available)

```bash
pip install virtualenv
```

_Or, if your system Python is externally managed (e.g. on Debian/Ubuntu):_

```bash
pip install virtualenv --break-system-packages
```

### 2. Create a virtual environment inside the project

```bash
virtualenv .venv
```

### 3. Activate the virtual environment

```bash
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Recovering From a Broken Virtual Environment

If your virtual environment is corrupted, delete and recreate it.

### 1. Remove the broken virtual environment

```bash
rm -rf .venv
```

### 2. Create a fresh virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate it
can 
```bash
source .venv/bin/activate
```

### 4. Upgrade `pip` and reinstall dependencies

```bash
pip install --upgrade pip
if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```

