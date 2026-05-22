# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Selenium-based UI automation framework for the Sauce Labs demo e-commerce app (`saucedemo.com`). Uses Python, pytest, and the Page Object Model pattern.

## Commands

```bash
# Install dependencies
pip install -r requirements.txt

# Run all tests
pytest

# Run a specific test file
pytest tests/test_swag_labs.py

# Run a single test by name
pytest tests/test_swag_labs.py::TestSwagLabs::test_name

# Run by marker
pytest -m smoke
pytest -m "login or cart"

# Run with specific browser (chrome, firefox, edge)
pytest --browser=firefox

# Run headless
pytest --browser=chrome --headless=True

# Generate HTML report (auto-configured in pytest.ini)
pytest --html=reports/report.html
```

Markers available: `smoke`, `regression`, `login`, `inventory`, `cart`, `api`, `api_negative`, `ui`

## Architecture

### Page Object Model

All pages inherit from `BasePage` ([src/core/base_page.py](src/core/base_page.py)), which wraps Selenium interactions (find, click, type, scroll, visibility). Pages live in [src/pages/](src/pages/) and contain locators and actions — no assertions.

Browser setup is in `DriverFactory` ([src/core/driver_factory.py](src/core/driver_factory.py)), which supports Chrome, Firefox, and Edge with optional headless mode.

### Test Layer

- **[tests/conftest.py](tests/conftest.py)**: Two fixtures — `open_browser` (launches driver, navigates to `ui_url`, tears down after test) and `get_user` (loads credentials from YAML by user type). Both accept CLI args via `pytest_addoption`.
- **[tests/test_swag_labs.py](tests/test_swag_labs.py)**: All test cases in one file, covering login, inventory sorting/display, cart operations, and checkout flow.

### Utilities

- **[utils/soft_assertions.py](utils/soft_assertions.py)**: Collect multiple assertion failures within a test; call `assert_all()` at the end to raise. Use this instead of bare `assert` when validating multiple conditions.
- **[utils/wait_utils.py](utils/wait_utils.py)**: Wraps `WebDriverWait` with a 10s default timeout. Always use `WaitUtils` for element interactions rather than `time.sleep`.
- **[utils/config_reader.py](utils/config_reader.py)**: Loads `config/config.yaml` (URLs) and `test_data/users.yaml` (credentials and checkout data).

### Configuration

- **[config/config.yaml](config/config.yaml)**: `api_url` and `ui_url` — the only place to change target environments.
- **[test_data/users.yaml](test_data/users.yaml)**: User credentials (standard, locked, error, performance glitch users) and checkout form data.
- **[pytest.ini](pytest.ini)**: Sets `testpaths=tests/`, verbose output (`-vvvs`), INFO logging, and registers all markers.

## Key Conventions

- No `__init__.py` files — pytest discovers modules via `pythonpath = .` in `pytest.ini`.
- Reports are written to `reports/` (gitignored, created at runtime).
- `DriverFactory` uses `webdriver-manager` for automatic chromedriver/geckodriver downloads — no manual driver installation needed.
