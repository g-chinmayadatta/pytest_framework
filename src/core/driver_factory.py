from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


class DriverFactory:

    @staticmethod
    def get_driver(browser="chrome", headless=False):

        if browser.lower() == "chrome":
            options = ChromeOptions()
            prefs = {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False
            }
            if headless:
                options.add_argument("--headless=new")
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--disable-gpu")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            options.add_experimental_option("prefs", prefs)

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser.lower() == "firefox":
            options = FirefoxOptions()

            if headless:
                options.add_argument("--headless")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )

        elif browser.lower() == "edge":
            options = EdgeOptions()

            if headless:
                options.add_argument("--headless")

            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")

            driver = webdriver.Edge(
                service=EdgeService(EdgeChromiumDriverManager().install()),
                options=options
            )

        else:
            raise Exception(f"Browser '{browser}' not supported. Choose from: chrome, firefox, edge")

        driver.implicitly_wait(5)
        driver.maximize_window()
        return driver