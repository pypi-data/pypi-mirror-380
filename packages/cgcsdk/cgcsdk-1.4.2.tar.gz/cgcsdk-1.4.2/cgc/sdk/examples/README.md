# CGC SDK Examples

This directory contains example scripts demonstrating how to use the CGC SDK.

## Setup

Before running the examples, you need to set up a virtual environment and install the CGC package:

### 1. Create and activate a virtual environment

```bash
# From the project root directory
cd cgc-client-k8s-cloud

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install the CGC package in development mode

```bash
# Install the package and its dependencies
pip install -e .

# Or install dependencies manually:
pip install -r requirements.txt
```

### 3. Run the examples

```bash
# Volume workflow example
python cgc/sdk/examples/volume_workflow.py

# Basic compute example
python cgc/sdk/examples/basic_compute.py

# Job workflow example
python cgc/sdk/examples/job_workflow.py

# Port management example
python cgc/sdk/examples/port_management.py

# Database connection example
python cgc/sdk/examples/database_connection.py
```

## Available Examples

- **volume_workflow.py**: Complete volume lifecycle demonstration (create → mount → unmount → delete)
- **basic_compute.py**: Basic compute resource creation and management
- **job_workflow.py**: Job creation and monitoring
- **port_management.py**: Port configuration for resources
- **database_connection.py**: Database resource setup and connection

## Troubleshooting

If you encounter import errors:

1. **Ensure virtual environment is activated**: You should see `(venv)` in your command prompt
2. **Install the package**: Run `pip install -e .` from the project root
3. **Check dependencies**: Run `pip install -r requirements.txt`
4. **Verify installation**: Run `python -c "import cgc.sdk.volume; print('CGC SDK imported successfully')"`

## Authentication

Make sure you have CGC configured with proper authentication before running the examples:

```bash
cgc auth login
cgc contexts
```
