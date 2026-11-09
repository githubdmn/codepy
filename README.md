# AI Chat API

## Features

## pyenv - install python locally

```bash
curl https://pyenv.run | bash
```

## Setup

In case `virtualenv` is not installed

```bash 
pip install virtualenv 
```

*or*

```bash
pip install virtualenv --break-system-packages
```

Inside of the project

```bash
virtualenv .venv 
```

1. **Activate your virtual environment** (you should have done this already):

   ```bash
   source .venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Remove the broken virtual environment

```bash 
   rm -rf .venv
   ```

### Create a fresh virtual environment

```bash
python3 -m venv .venv
```

### Activate it

```bash
source .venv/bin/activate
```

### Upgrade pip and reinstall your dependencies (if you have a requirements.txt)

```bash 
pip install --upgrade pip if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```