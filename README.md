# 🚀 Selenium + Pytest Automation Framework (UI + API + CI/CD)

## 📌 Overview

This project is a **full-fledged automation framework** built using **Python, Selenium, and Pytest** to automate both:

- 🌐 UI Testing → SauceDemo (Swag Labs)
- 🔗 API Testing → Library API (Rahul Shetty Academy)

The framework follows **Page Object Model (POM)** and includes reusable utilities for logging, reporting, API handling, and CI/CD integration.

---

## 🔥 Key Features

### UI Automation
- Page Object Model (POM)
- Selenium WebDriver
- Modular test structure
- Wait utilities
- Screenshot on failure

### API Automation
- REST API testing using `requests`
- Reusable API client
- Dynamic payload generation
- API logging (like Postman)
- Positive + Negative test coverage
- Custom API assertions

### Framework Capabilities
- YAML-based configuration
- YAML-based test data
- Custom assertions (UI + API)
- Soft assertions support
- Logging support
- HTML test reports

### CI/CD
- GitHub Actions integration
- Automated test execution on push
- Headless browser execution
- Report artifact upload

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python | Programming |
| Selenium | UI Automation |
| Pytest | Test Framework |
| Requests | API Testing |
| Pytest-html | Reporting |
| PyYAML | Config/Test Data |
| GitHub Actions | CI/CD |

---
## 🏗️ Framework Architecture
```text
Test Layer
│
├── UI Tests (Selenium + Pytest)
├── API Tests (Requests + Pytest)
│
Page Layer (POM)
│
├── Login Page
├── Inventory Page
├── Cart Page
│
Core Layer
│
├── Driver Factory
├── Base Page
│
API Layer
│
├── API Client
├── Endpoints
├── Payloads
├── API Logger
├── API Assertions
│
Utility Layer
│
├── Logger
├── Wait Utils
├── Assertions
├── Config Reader
│
Test Data Layer
│
├── YAML Test Data
```
---

## 📁 Project Structure
```text
pytest_framework
│
├── src
│ ├── core
│ ├── pages
│ ├── util
│ └── api
│       ├── api_client.py
│       ├── api_logger.py
│       ├── api_assertions.py
│       ├── api_endpoints.py
│       └── api_payloads.py
│
├── tests
│ ├── swaglabs (UI)
│ └── api
│       ├── test_library_api.py
│       └── test_library_negative.py
│       └── conftest.py
│       
├── config
├── testdata
├── reports
├── logs
│
├── .github/workflows/automation.yml
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```
---

## 🧪 Test Coverage

### UI Tests
- Login scenarios (valid, locked, negative)
- Inventory validation
- Sorting functionality
- Cart operations
- Checkout flow

### API Tests
- Add Book (POST)
- Get Book (GET)
- Delete Book (POST)

### Negative Tests
- Missing payload fields
- Duplicate book creation
- Invalid book ID retrieval
- Invalid delete operation

---
## 👨‍💻 Author

Chinmaya Gunturu
Automation QA Engineer