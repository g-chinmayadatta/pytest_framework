from selenium.webdriver.common.by import By

from src.core.base_page import BasePage
from utils.logger import logger

class LoginPage:
    user_name_field = (By.XPATH,"//input[@id='user-name']")
    password_field = (By.XPATH,"//input[@id='password']")
    login_btn = (By.XPATH,"//input[@id='login-button']")
    error_msg = (By.XPATH,"//div[contains(@class, 'error-message-container')]")
    users_list = (By.XPATH,"//div[@class='login_credentials_wrap']//div[@class='login_credentials']")
    password_ui = (By.XPATH,"//div[@class='login_credentials_wrap']//div[@class='login_password']")

    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def get_password(self):
        data = self.base_page.get_text(self.password_ui)
        data = data.split('\n')
        return data[-1]

    def get_user_name(self, name):
        names = self.base_page.get_text(self.users_list).split('\n')
        for i in names:
            if name in i:
                return i
        else:
            return None

    def login(self, user, password):
        try:
            self.base_page.enter_text(self.user_name_field, user)
            self.base_page.enter_text(self.password_field, password)
            self.base_page.click_element(self.login_btn)
        except Exception as e:
            logger.info(f"unable to login {e}")

    def check_error_message(self):
        return self.base_page.is_element_visible(self.error_msg)

    def get_error_message(self):
        return self.base_page.get_text(self.error_msg)

    def check_login_page_displayed(self):
        return self.base_page.is_element_visible(self.login_btn)