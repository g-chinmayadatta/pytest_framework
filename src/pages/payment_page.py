from decimal import Decimal
from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class Payment:
    finish_btn = (By.XPATH,"//button[@id='finish']")
    success_msg = (By.XPATH,"//h2[@class='complete-header']")
    go_home_btn = (By.XPATH,"//button[@id='back-to-products']")
    item_total_price = (By.XPATH,"//div[@class='summary_subtotal_label']")
    tax_on_items = (By.XPATH,"//div[@class='summary_tax_label']")
    total_cart_amount = (By.XPATH,"//div[@class='summary_total_label']")
    summary_title = (By.XPATH,"//div[@class='header_secondary_container']//span[@class='title' and text()='Checkout: Overview']")
    def __init__(self, driver):
        self.base_page = BasePage(driver)


    def get_success_msg(self):
        return self.base_page.get_text(self.success_msg)

    def click_finish(self):
        self.base_page.click_element(self.finish_btn)

    def click_go_home(self):
        self.base_page.click_element(self.go_home_btn,True)

    def get_tax(self):
        return float(Decimal(self.base_page.get_text(self.tax_on_items).split('$')[-1]))

    def get_total_cart_amount(self):
        return float(Decimal(self.base_page.get_text(self.total_cart_amount).split('$')[-1]))

    def check_summary_page(self):
        return self.base_page.is_element_visible(self.summary_title)