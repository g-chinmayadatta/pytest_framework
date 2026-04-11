from selenium.webdriver.common.by import By
from src.core.base_page import BasePage


class ShoppingCart:
    cart_item_price = (By.XPATH,"//div[@class='cart_list']//div[@class='inventory_item_price']")
    cart_remove_by_name = (By.XPATH,"//div[@class='inventory_item_name' and text() ='{}']/ancestor::div[@class='cart_item_label']//button[contains(@class,'cart_button')]")
    cart_item_name = (By.XPATH,"//div[@class='inventory_item_name']")
    cart_checkout_btn = (By.XPATH,"//button[@id='checkout']")
    cart_title = (By.XPATH,"//div[@class='header_secondary_container']//span[@class='title' and text() ='Your Cart']")
    def __init__(self, driver):
        self.base_page = BasePage(driver)

    def get_items_names(self):
        el = self.base_page.get_all_elements(self.cart_item_name)
        names = []
        for i in el:
            names.append(self.base_page.get_text(i))
        return names

    def get_total_price(self):
        total = 0
        el = self.base_page.get_all_elements(self.cart_item_price)
        for i in el:
            t = self.base_page.get_text(i).split('$')[-1]
            total+=float(t)
        return total

    def click_checkout(self):
        self.base_page.click_element(self.cart_checkout_btn, True)

    def remove_item(self, name):
        products = self.get_items_names()
        for i in name:
            if i in products:
                self.base_page.click_element((self.cart_remove_by_name[0],self.cart_remove_by_name[-1].format(i)),True)

    def check_checkout_page(self):
        return self.base_page.is_element_visible(self.cart_title)