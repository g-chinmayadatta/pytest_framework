import time

import pytest

from src.pages.checkout_page import CheckOut
from src.pages.inventory_page import Inventory
from src.pages.login_page import LoginPage
from src.pages.payment_page import Payment
from src.pages.shopping_cart_page import ShoppingCart
from src.util.assertions import Assertion
from src.util.logger import logger
from src.util.soft_assertions import SoftAssertion


class TestDemo:
    def setup(self, open_browser):
        self.custom_driver = open_browser['driver']
        self.user = open_browser['user']
        self.password = open_browser['password']
        self.login_page =LoginPage(self.custom_driver)
        self.inventory_page = Inventory(self.custom_driver)
        self.shopping_cart_page = ShoppingCart(self.custom_driver)
        self.checkout_page = CheckOut(self.custom_driver)
        self.payment_page = Payment(self.custom_driver)
        self.soft_assert = SoftAssertion()

    @pytest.mark.parametrize("open_browser",[{"user":"standard"}],indirect=True)
    def test_standard(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user, self.password)
        self.inventory_page.add_products_to_cart(["Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)","Sauce Labs Bike Light"])
        self.inventory_page.click_cart()
        logger.info(self.shopping_cart_page.get_items_names())
        self.shopping_cart_page.remove_item(["Test.allTheThings() T-Shirt (Red)"])
        logger.info(self.shopping_cart_page.get_items_names())
        total = self.shopping_cart_page.get_total_price()
        self.shopping_cart_page.click_checkout()
        details = {
            "first name":"chinmaya",
            "last name":"gunturu",
            "postal":"522101"
        }
        self.checkout_page.fill_details(details)
        self.checkout_page.click_continue_btn()
        self.payment_page.click_finish()
        self.payment_page.get_success_msg()
        self.payment_page.click_go_home()

    @pytest.mark.parametrize("open_browser", [{"user": "locked"}], indirect=True)
    def test_locked(self, open_browser):
        self.setup(open_browser)


    def test_xyz(self, open_browser):
        self.setup(open_browser)
        time.sleep(5)
        Assertion.assert_true(False,"adsfgd")
