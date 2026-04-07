from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class CheckOut:
    first_name_field = (By.XPATH,"//input[ @ id = 'first-name']")
    last_name_field = (By.XPATH,"//input[ @ id = 'last-name']")
    postal_code_field = (By.XPATH,"//input[ @ id = 'postal-code']")
    continue_btn =  (By.XPATH,"// input[ @ id = 'continue']")
    cancel_btn = (By.XPATH,"// button[ @ id = 'cancel']")
    error_container = (By.XPATH,"//div[contains(@class,'error')]/h3")

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def fill_details(self, data):
        self.base_page.enter_text(self.first_name_field,data['first name'])
        self.base_page.enter_text(self.last_name_field,data['last name'])
        self.base_page.enter_text(self.postal_code_field,data['postal'])

    def click_continue_btn(self):
        self.base_page.click_element(self.continue_btn,True)

    def check_error_messages(self):
        return self.base_page.is_element_visible(self.error_container)

    def get_error_message(self):
        return self.base_page.get_text(self.error_container)