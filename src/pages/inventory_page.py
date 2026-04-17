from selenium.webdriver.common.by import By
from src.util.logger import logger
from src.core.base_page import BasePage
from src.util.wait_utils import WaitUtils


def _xpath_str(value):
    """Return an XPath string literal that safely handles single quotes."""
    if "'" not in value:
        return f"'{value}'"
    parts = value.split("'")
    return "concat('" + "', \"'\", '".join(parts) + "')"


class Inventory:
    product_titles = (By.XPATH,"//div[@class='inventory_item_name ']")
    product_add_cart_btn = (By.XPATH,"//div[@class='inventory_list']//div[@class='inventory_item_name ' and text()={}]/ancestor::div[@class='inventory_item']//button[contains(@class,'btn_inventory')]")
    shopping_cart = (By.XPATH,"//a[@class='shopping_cart_link']")
    menu_btn  = (By.XPATH,"//button[@id='react-burger-menu-btn']")
    menu_options = (By.XPATH,"//div[@class='bm-menu']//a[text()={}]")
    product_price = (By.XPATH,"//div[@class='inventory_item_price']")
    sort_btn = (By.XPATH,"//div[@class='right_component']//span[@class='select_container']")
    sort_dropdown = (By.XPATH,"//span[@class='select_container']//option[text()='{}']")
    cart_count = (By.XPATH,"//div[@class='shopping_cart_container']//span[@class='shopping_cart_badge']")

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.wait_util = WaitUtils(driver)
    def get_product_titles(self):
        el = self.base_page.get_all_elements(self.product_titles)
        names = []
        for i in el:
            names.append(self.base_page.get_text(i))
        return names

    def add_products_to_cart(self, name):
        try:
            for i in name:
                return self.base_page.click_element((self.product_add_cart_btn[0], self.product_add_cart_btn[-1].format(_xpath_str(i))), True)
        except Exception as e:
            logger.info(f" unable to add all th products to cart {e}")
            return False
        # products = self.get_product_titles()
        # try:
        #     for i in name:
        #         if i in products:
        #             self.base_page.click_element((self.product_add_cart_btn[0],self.product_add_cart_btn[-1].format(i)), True)
        # except Exception as e:
        #     logger.info(f"unable to add product to cart {e}")

    def click_cart(self):
        self.base_page.click_element(self.shopping_cart, True)

    def click_menu(self):
        self.base_page.click_element(self.menu_btn, True)

    def click_menu_option(self, option):
        self.base_page.click_element((self.menu_options[0], self.menu_options[-1].format(_xpath_str(option))), True)

    def get_products_count(self):
        return len(self.base_page.get_all_elements(self.product_titles))

    def get_products_price(self):
        el = self.base_page.get_all_elements(self.product_price)
        prices = []
        for i in el:
            prices.append(float(self.base_page.get_text(i).split('$')[-1]))
        return prices

    def get_cart_count(self):
        self.wait_util.wait_for_element_present(self.cart_count)
        return int(self.base_page.get_text(self.cart_count))

    def select_sort_option(self, option):
        self.base_page.click_element(self.sort_btn)
        try:
            self.base_page.click_element((self.sort_dropdown[0],self.sort_dropdown[-1].format(option)), True)
        except Exception as e:
            logger.info(f"unable to click option in dropdown {e}")

    def check_inventory_page_displayed(self):
        return self.base_page.is_element_visible(self.product_titles)

    def check_sort_titles(self,l1 , l2, sort_type):
        if sort_type == 'Name (A to Z)':
            l1.sort()
            logger.info(f"sorted list is {l1}")
            return l1 == l2
        elif sort_type == 'Name (Z to A)':
            l1.sort(reverse=True)
            logger.info(f"sorted list is {l1}")
            return l1 == l2
        elif sort_type == 'Price (low to high)':
            l1.sort()
            logger.info(f"sorted list is {l1}")
            return l1 == l2
        elif sort_type == 'Price (high to low)':
            l1.sort(reverse=True)
            logger.info(f"sorted list is {l1}")
            return l1 == l2
        else:
            logger.info("unable to check sorting ")
            return False

    def check_cart_count(self):
        return self.base_page.is_element_visible(self.cart_count)
