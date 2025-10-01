# Costmodels Package Development Guide

This document outlines the general structure of the `costmodels` package and the development process.

## Package Structure

The `costmodels` package is organized as follows:

*   **`src/`**: Contains the main source code of the package.
    *   **`costmodels/cmodel.py`**: Base classes for cost models. New models should subclass the `CostModel` class.
    *   **`costmodels/models/`**: Directory with existing model implementations.
        *   `battery_cost.py`: A simple battery cost model.
        *   `dtu_offshore.py`: A detailed offshore wind turbine cost model from DTU.
        *   `minimalistic.py`: A minimalistic offshore wind farm cost model.
        *   `nrel.py`: NREL's offshore wind turbine cost model.
        *   `p2h2_cost.py`: A power-to-hydrogen cost model.
        *   `pv.py`: A simple photovoltaic plant cost model.
        *   `shared_cost.py`: A model for shared costs in a hybrid power plant.
*   **`tests/`**: Contains all the unit tests for the package.
*   **`examples/`**: Contains example usage and extension of the package.
*   **`pyproject.toml`**: Defines project metadata, dependencies, and build system configurations.

## Development Process

### 1. Install Dependencies

To set up your development environment and install the package in editable mode along with its testing dependencies, navigate to the project's root directory and execute the following command:

```bash
pip install -e ".[test]"
```

This command installs the package itself, making your local changes immediately available. It also installs dependencies listed under `[project.dependencies]` and the testing-specific dependencies listed under `[project.optional-dependencies.test]` in the `pyproject.toml` file.

### 2. Running Tests

Tests are managed and executed using `pytest`. After successfully installing the dependencies, you can run the test suite from the project's root directory with:

```bash
pytest
```

Pytest will automatically discover and run all tests located within the `tests/` directory. The configuration for pytest, including test paths and other options, can be found in the `pyproject.toml` file under the `[tool.pytest.ini_options]` section.

## Pre-commit Hooks

This project utilizes pre-commit hooks to ensure code quality and consistency before commits are made. These hooks, defined in the `.pre-commit-config.yaml` file, typically handle tasks like code formatting.

To set up pre-commit hooks:

1.  **Install the git hooks:**
    ```bash
    pre-commit install
    ```

Once installed, the hooks will run automatically before each commit. However it's preffered to run `pre-commit run --all-files` before commiting anything.

## Mypy Type Checking

Project uses `mypy` to enforce consistent type hint annotation for the source code. Before commiting developer should make sure that `mypy` run successfully.

```
mypy src/
```