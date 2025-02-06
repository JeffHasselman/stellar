## Setup Instructions(User): stellar CLI

This guide will walk you through the steps to set up the stellar cli on your local machine

### Step 1: Create a Python virtual environment

In the tools directory, create a Python virtual environment by running:

```bash
python -m venv venv
```

### Step 2: Activate the virtual environment
* On Linux/MacOS:

```bash
source venv/bin/activate
```

### Step 3: Run the build script
```bash
pip install stellar==0.1.9
```

## Uninstall Instructions: stellar CLI
```bash
pip uninstall stellar
```

## Setup Instructions (Dev): stellar CLI

This guide will walk you through the steps to set up the stellar cli on your local machine when you want to develop the stellargw CLI

### Step 1: Create a Python virtual environment

In the tools directory, create a Python virtual environment by running:

```bash
python -m venv venv
```

### Step 2: Activate the virtual environment
* On Linux/MacOS:

```bash
source venv/bin/activate
```

### Step 3: Run the build script
```bash
poetry install
```

### Step 4: build stellar
```bash
stellar build
```

### Step 5: download models
This will help download models so server can load faster. This should be done once.

```bash
stellar download-models
```

### Logs
`stellar` command can also view logs from gateway and server. Use following command to view logs,

```bash
stellar logs --follow
```

## Uninstall Instructions: stellar CLI
```bash
pip uninstall stellar
