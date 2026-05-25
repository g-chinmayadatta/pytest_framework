# pytest_framework

Selenium-based test automation framework covering UI and API testing. UI tests target the [Sauce Labs demo app](https://www.saucedemo.com/); API tests target the [Rahul Shetty Academy Library API](https://rahulshettyacademy.com).

---

## Prerequisites

- Python 3.8+
- Google Chrome / Firefox / Edge installed

```bash
pip install -r requirements.txt
```

No manual driver installation needed — `webdriver-manager` downloads the correct driver automatically.

---

## Running Tests

```bash
# Run all tests
pytest

# Run a specific test file
pytest tests/test_swag_labs.py

# Run a single test by name
pytest tests/test_swag_labs.py::TestSwagLabs::test_name

# Run by marker
pytest -m smoke
pytest -m regression
pytest -m "login or cart"
pytest -m api

# Run on a specific browser (chrome | firefox | edge)
pytest --browser=firefox

# Run headless
pytest --browser=chrome --headless=True

# Generate HTML report with screenshots on failure
pytest --html=reports/report.html
```

### Available Markers

| Marker | Scope |
|---|---|
| `smoke` | Critical happy-path cases |
| `regression` | Full regression suite |
| `login` | Login-related tests |
| `inventory` | Inventory page tests |
| `cart` | Cart functionality |
| `api` | API tests (Library API) |
| `api_negative` | Negative API tests |
| `ui` | All UI cases |

---

## Framework Structure

```
├── config/
│   └── config.yaml          # api_url and ui_url (only place to change environments)
├── test_data/
│   └── users.yaml           # Credentials for all user types + checkout form data
├── src/
│   ├── core/
│   │   ├── base_page.py     # BasePage: wraps all Selenium interactions
│   │   └── driver_factory.py# Browser setup (Chrome/Firefox/Edge, headless)
│   ├── pages/               # Page Objects — locators + actions, no assertions
│   │   ├── login_page.py
│   │   ├── inventory_page.py
│   │   ├── shopping_cart_page.py
│   │   ├── checkout_page.py
│   │   └── payment_page.py
│   └── api/                 # API layer (Library API)
│       ├── api_client.py    # requests wrapper (get/post/delete)
│       ├── api_endpoint.py  # Endpoint paths
│       ├── api_payloads.py  # Random test data generators
│       ├── api_assertions.py# Static assertion helpers for responses
│       └── api_logger.py    # Request/response logging
├── tests/
│   ├── conftest.py          # Fixtures: open_browser, get_user; failure screenshot hook
│   └── test_swag_labs.py    # All test cases
└── utils/
    ├── soft_assertions.py   # Collect failures; raise at end with assert_all()
    ├── wait_utils.py        # WebDriverWait wrapper (10s default)
    ├── config_reader.py     # Loads config.yaml and users.yaml
    └── logger.py            # Shared logger instance
```

---

## Key Design Decisions

- **Page Object Model**: All pages inherit from `BasePage`. Pages hold locators and actions only — assertions live in tests.
- **Soft assertions**: Use `SoftAssertions` from `utils/soft_assertions.py` when validating multiple conditions in one test; call `assert_all()` at the end.
- **Waits**: Always use `WaitUtils` instead of `time.sleep`. It wraps `WebDriverWait` with a 10-second default.
- **Failure screenshots**: `conftest.py` automatically captures a screenshot when a test fails and embeds it in the HTML report (requires `--html` flag).
- **User types**: `standard`, `locked`, `error`, `performance` — loaded from `test_data/users.yaml` via the `get_user` fixture with `@pytest.mark.parametrize`.
- **No `__init__.py`**: Module discovery is handled by `pythonpath = .` in `pytest.ini`.
- **Reports**: Written to `reports/` (gitignored, created at runtime).
