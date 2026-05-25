from datetime import datetime
import os

import pytest
import time
from utils.logger import logger
from src.core.driver_factory import DriverFactory
from utils.config_reader import ConfigReader

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = getattr(item, "driver", None)

        if driver:
            screenshot_dir = os.path.join("reports", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            file_name = f"{item.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
            file_path = os.path.join(screenshot_dir, file_name)

            driver.save_screenshot(file_path)

            pytest_html = item.config.pluginmanager.getplugin("html")

            if pytest_html:
                extra = getattr(report, "extra", [])
                extra.append(pytest_html.extras.image(os.path.abspath(file_path)))
                report.extra = extra

            
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="run test in which browser chrome firefox, edge"
    )
    parser.addoption(
        "--headless",
        action="store",
        default=False,
        help="to run the test in head mode or headless mode"
    )


@pytest.fixture(scope='function')
def open_browser(request):
    file_config = ConfigReader.load_config()
    browser = request.config.getoption("--browser")
    head = request.config.getoption("--headless")
    driver = DriverFactory.get_driver(browser,head)
    driver.get(file_config['ui_url'])
    request.node.driver = driver # to use this in report generation
    yield driver
    driver.quit()

@pytest.fixture(scope="function")    
def get_user(request):
    users = ConfigReader.load_users()
    user = request.param.get("user")
    return users[user]