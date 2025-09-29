# Sheet Edit Example

## Local Development Setup


1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install univer-use in editable mode(optional):
   ```bash
   pip install -e ...
   ```

3. Install example dependencies:
   ```bash
   pip install -e .
   ```

## Run the example

1. Copy the environment configuration:
   ```bash
   cp .env_example .env
   # Edit the .env file, add the necessary API keys
   ```

2. Start the LangGraph development server:
   ```bash
   langgraph dev
   ```