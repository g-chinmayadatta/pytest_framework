from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement

from src.util.wait_utils import WaitUtils


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitUtils(driver)

    def open_url(self, url):
        self.driver.get(url)

    def get_element(self, locator):
        try:
            element = self.wait.wait_for_element_present(locator)
            return element
        except TimeoutException:
            print(f"Element not found: {locator}")
            return None

    def get_all_elements(self, locator):
        try:
            self.wait.wait_for_all_elements(locator)
            elements = self.driver.find_elements(*locator)
            return elements
        except TimeoutException:
            print(f"No elements found: {locator}")
            return []

    def click_element(self, locator, scroll = False):
        element = self.wait.wait_for_element_clickable(locator)
        if scroll:
            self.scroll_to_view(element)
        element.click()

    def enter_text(self, locator, text):
        element = self.wait.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator_or_element):

        try:
            # If it's a WebElement, get text directly
            if isinstance(locator_or_element, WebElement):
                self.scroll_to_view(locator_or_element)
                return locator_or_element.text

            # If it's a locator tuple, find element first
            else:
                element = self.wait.wait_for_element_present(locator_or_element)
                self.scroll_to_view(element)
                return element.text
        except TimeoutException:
            print(f"Element not found: {locator_or_element}")
            return None

    def is_element_visible(self, locator):
        try:
            self.wait.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def scroll_to_view(self, el):
        script = "arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});"
        self.driver.execute_script(script, el)