import yaml
from src.core.driver_factory import DriverFactory
from src.util.logger import logger
import pytest
import os
from datetime import datetime
from src.api.api_client import APIClient
from src.util.config_reader import ConfigReader

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

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(os.path.abspath(file_path)))
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
        ),
        parser.addoption(
            "--env",
            action="store",
            default="qa",
            help="run the test in which env qa or dev"
        )
    )

@pytest.fixture(scope='function')
def open_browser(request):
    cli_env = request.config.getoption("--env")
    file_config = ConfigReader.load_config(cli_env)
    logger.info("this is conftest open browser fixture")
    logger.info(f"running all teh tests in {cli_env} environment")
    cli_browser = request.config.getoption("--browser")
    browser = cli_browser if cli_browser else file_config['browser']
    cli_head = request.config.getoption("--headless")
    head = cli_head if cli_browser else file_config['head']
    user = getattr(request, 'param', "standard")
    with open("testdata/users.yaml",'r') as f:
        data = yaml.safe_load(f)
    user_key = data[user]
    logger.info(f"user name and password is {user_key}")
    driver = DriverFactory.get_driver(browser, head)
    driver.get(file_config['url'])
    request.node.driver = driver # to use this in report generation
    yield {"driver":driver,"user":user_key['username'], "password":user_key['password']}
    driver.close()
    logger.info("end of open browser fixture")

@pytest.fixture
def api_client():

    config = ConfigReader.load_config()
    base_url = config["api_url"]

    return APIClient(base_url)
