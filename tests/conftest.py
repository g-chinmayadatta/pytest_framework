


import yaml
from src.core.driver_factory import DriverFactory
from src.util.logger import logger
import pytest
import os
from datetime import datetime


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = None

        if "open_browser" in item.funcargs:
            open_browser = item.funcargs["open_browser"]

            if isinstance(open_browser, dict):
                driver = open_browser.get("driver")
            else:
                driver = open_browser

        if driver:

            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)

            # attach screenshot to pytest-html report
            pytest_html = item.config.pluginmanager.getplugin("html")

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(file_path))
            report.extra = extra

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="run test in which browser chrome firefox, edge"
    ),
    (
        parser.addoption(
            "--headless",
            action="store",
            default=False,
            help="run the test in headless mode so no browser will be opened"
        )
    )

@pytest.fixture(scope='function')
def open_browser(request):
    logger.info("this is conftest open browser fixture")
    browser = request.config.getoption("--browser")
    head = request.config.getoption("--headless")
    user = getattr(request, 'param', "standard")
    with open("testdata/users.yaml",'r') as f:
        data = yaml.safe_load(f)
    user_key = data[user]
    logger.info(f"user name and password is {user_key}")
    driver = DriverFactory.get_driver(browser, head)
    driver.get("https://www.saucedemo.com/")
    yield {"driver":driver,"user":user_key['username'], "password":user_key['password']}
    driver.close()
    logger.info("end of open browser fixture")
