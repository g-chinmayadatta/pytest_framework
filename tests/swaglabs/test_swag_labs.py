import time

import pytest
from src.pages.checkout_page import CheckOut
from src.pages.inventory_page import Inventory
from src.pages.login_page import LoginPage
from src.pages.payment_page import Payment
from src.pages.shopping_cart_page import ShoppingCart
from src.util.soft_assertions import SoftAssertion
from src.util.logger import logger
from src.util.wait_utils import WaitUtils


class TestSwagLabs:

    def setup(self, open_browser):
        self.custom_driver = open_browser['driver']
        self.user = open_browser['user']
        self.password = open_browser['password']
        self.login_page = LoginPage(self.custom_driver)
        self.inventory = Inventory(self.custom_driver)
        self.shopping_cart_page = ShoppingCart(self.custom_driver)
        self.checkout_page = CheckOut(self.custom_driver)
        self.payment_page = Payment(self.custom_driver)
        self.soft_assert = SoftAssertion()
        self.wait_util = WaitUtils(self.custom_driver)

    @pytest.mark.login
    @pytest.mark.smoke
    def test_login_valid(self, open_browser):
        self.setup(open_browser)
        login_page_displayed = self.login_page.check_login_page_displayed()
        self.login_page.login(self.user, self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        self.soft_assert.assert_equal(login_page_displayed,True,"verifying login page is displayed")
        self.soft_assert.assert_equal(inventory_page_displayed, True, "verifying after login inventory page is displayed")
        self.soft_assert.assert_all()

    @pytest.mark.login
    @pytest.mark.parametrize("open_browser", ["locked"], indirect=True)
    def test_login_locked(self, open_browser):
        self.setup(open_browser)
        expected_message = "Epic sadface: Sorry, this user has been locked out."
        self.login_page.login(self.user,self.password)
        error_displayed = self.login_page.check_error_message()
        message = self.login_page.get_error_message()
        self.soft_assert.assert_equal(error_displayed, True,"Verifying error message is displayed for locked user")
        self.soft_assert.assert_equal(message,expected_message,"verifying the error message for locked user")
        self.soft_assert.assert_all()

    @pytest.mark.login
    def test_login_invalid_input(self, open_browser):
        self.setup(open_browser)
        expected_message = "Epic sadface: Username and password do not match any user in this service"
        invalid_password = self.password+"asd"
        login_page_displayed = self.login_page.check_login_page_displayed()
        self.login_page.login(self.user,password=invalid_password)
        error_displayed = self.login_page.check_error_message()
        message = self.login_page.get_error_message()
        self.soft_assert.assert_equal(login_page_displayed, True, "verifying if login page is displayed")
        self.soft_assert.assert_equal(error_displayed, True, "Verifying if error message is displayed after providing invalid credentials")
        self.soft_assert.assert_in(message, expected_message,"verifying th error message after providing invalid credentials ")
        self.soft_assert.assert_all()

    @pytest.mark.login
    def test_login_empty_user_input(self, open_browser):
        self.setup(open_browser)
        self.user = ''
        expected_message = "Epic sadface: Username is required"
        login_page_displayed = self.login_page.check_login_page_displayed()
        self.login_page.login(self.user, self.password)
        error_displayed = self.login_page.check_error_message()
        message = self.login_page.get_error_message()
        self.soft_assert.assert_equal(login_page_displayed, True, "Verifying if login page is displayed")
        self.soft_assert.assert_equal(error_displayed, True,"Verifying if error message is displayed after providing empty user name is provided")
        self.soft_assert.assert_in(message, expected_message, "Verifying th error message after providing empty user name is provided")
        self.soft_assert.assert_all()

    @pytest.mark.login
    def test_login_empty_password_input(self, open_browser):
        self.setup(open_browser)
        self.password = ''
        expected_message = "Epic sadface: Password is required"
        login_page_displayed = self.login_page.check_login_page_displayed()
        self.login_page.login(self.user, self.password)
        error_displayed = self.login_page.check_error_message()
        message = self.login_page.get_error_message()
        self.soft_assert.assert_equal(login_page_displayed, True, "Verifying if login page is displayed")
        self.soft_assert.assert_equal(error_displayed, True,"Verifying if error message is displayed after providing empty password is provided")
        self.soft_assert.assert_in(message, expected_message, "Verifying th error message after providing empty password is provided")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_inventory_products(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        inventory_products_count = self.inventory.get_products_count()
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verifying inventory page is displayed after login")
        self.soft_assert.assert_equal(inventory_products_count, 6, "Verify products count in inventory page")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_inventory_products_titles(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        expected_products_titles = ["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]
        product_titles = self.inventory.get_product_titles()
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed")
        self.soft_assert.assert_equal(product_titles, expected_products_titles, "Verify product titles")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_inventory_products_price(self, open_browser):
        self.setup(open_browser)
        expected_price = [29.99,9.99,15.99,49.99,7.99,15.99]
        self.login_page.login(self.user,self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        product_price = self.inventory.get_products_price()
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed after login")
        self.soft_assert.assert_equal(product_price, expected_price, "Verifying teh product prices displayed")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_sort_titles(self,open_browser):
        self.setup(open_browser)
        sort_type = "Name (A to Z)"
        self.login_page.login(self.user, self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        product_titles = self.inventory.get_product_titles()
        self.inventory.select_sort_option(sort_type)
        sorted_titles = self.inventory.get_product_titles()
        sorting_check = self.inventory.check_sort_titles(product_titles, sorted_titles,sort_type)
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed after login")
        self.soft_assert.assert_equal(sorting_check, True, "Verifying the sorting titles")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_sort_titles_reverse(self, open_browser):
        self.setup(open_browser)
        sort_type = "Name (Z to A)"
        self.login_page.login(self.user, self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        product_titles = self.inventory.get_product_titles()
        self.inventory.select_sort_option(sort_type)
        sorted_titles = self.inventory.get_product_titles()
        sorting_check = self.inventory.check_sort_titles(product_titles, sorted_titles, sort_type)
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed after login")
        self.soft_assert.assert_equal(sorting_check, True, "Verifying the sorting titles")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_sort_price(self, open_browser):
        self.setup(open_browser)
        sort_type = "Price (low to high)"
        self.login_page.login(self.user, self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        product_price = self.inventory.get_products_price()
        logger.info(f"ui normal list {product_price}")
        self.inventory.select_sort_option(sort_type)
        sorted_price = self.inventory.get_products_price()
        logger.info(f"ui sorted list {sorted_price}")
        sorting_check = self.inventory.check_sort_titles(product_price, sorted_price, sort_type)
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed after login")
        self.soft_assert.assert_equal(sorting_check, True, "Verifying the sorting price")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_sort_price_reverse(self, open_browser):
        self.setup(open_browser)
        sort_type = "Price (high to low)"
        self.login_page.login(self.user, self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        product_price = self.inventory.get_products_price()
        logger.info(f"ui normal list {product_price}")
        self.inventory.select_sort_option(sort_type)
        sorted_price = self.inventory.get_products_price()
        logger.info(f"ui sorted list {sorted_price}")
        sorting_check = self.inventory.check_sort_titles(product_price, sorted_price, sort_type)
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verify inventory page is displayed after login")
        self.soft_assert.assert_equal(sorting_check, True, "Verifying the sorting price")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_product_add_to_cart(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user, self.password)
        product = "Sauce Labs Onesie"
        add_products = self.inventory.add_products_to_cart([product])
        cart_count = self.inventory.get_cart_count()
        product2 = "Sauce Labs Fleece Jacket"
        add_products2 = self.inventory.add_products_to_cart([product2])
        after_add = self.inventory.get_cart_count()
        self.soft_assert.assert_equal(add_products, True, "Verify products are added to cart")
        self.soft_assert.assert_equal(add_products2, True, "Verify product is added to cart")
        self.soft_assert.assert_true(after_add > cart_count, "Verifying the count of cart after adding products is increasing")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_product_remove_from_cart(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        product = ["Sauce Labs Fleece Jacket","Sauce Labs Onesie"]
        add_product = self.inventory.add_products_to_cart(product)
        cart_count = self.inventory.get_cart_count()
        remove_product = self.inventory.add_products_to_cart(["Sauce Labs Onesie"])
        after_remove = self.inventory.get_cart_count()
        self.soft_assert.assert_equal(add_product, True, "Verify product is added to cart")
        self.soft_assert.assert_equal(remove_product, True, "Verify product is removed")
        self.soft_assert.assert_true(after_remove<cart_count, "Verifying the cart count is decreasing after removing product")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    @pytest.mark.smoke
    def test_product_add_multiple(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        products = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack","Sauce Labs Bike Light"]
        self.inventory.add_products_to_cart(products)
        cart_count = self.inventory.get_cart_count()
        self.soft_assert.assert_equal(len(products), cart_count, "Verify the cart count after adding products")
        self.soft_assert.assert_all()

    @pytest.mark.inventory
    def test_cart_navigation(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user, self.password)
        self.inventory.click_cart()
        cart_page_displayed = self.shopping_cart_page.check_checkout_page()
        self.soft_assert.assert_true(cart_page_displayed, "Verifying cart navigation happening")
        self.soft_assert.assert_all()

    def test_logout(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        inventory_page_displayed = self.inventory.check_inventory_page_displayed()
        self.inventory.click_menu()
        self.inventory.click_menu_option("Logout")
        login_page_displayed = self.login_page.check_login_page_displayed()
        self.soft_assert.assert_equal(inventory_page_displayed, True, "Verifying inventory page is displayed after login")
        self.soft_assert.assert_equal(login_page_displayed, True, "Verify login page is displayed after logout")
        self.soft_assert.assert_all()

    @pytest.mark.cart
    @pytest.mark.smoke
    def test_order_summary(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        products = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack"]
        details = {"first name":"chinmaya",
                   "last name":"gunturu",
                   "postal":"522101"}
        self.inventory.add_products_to_cart(products)
        self.inventory.click_cart()
        total_price = self.shopping_cart_page.get_total_price()
        self.shopping_cart_page.click_checkout()
        self.checkout_page.fill_details(details)
        self.checkout_page.click_continue_btn()
        summary_page_displayed = self.payment_page.check_summary_page()
        tax = self.payment_page.get_tax()
        total_amount = self.payment_page.get_total_cart_amount()
        self.soft_assert.assert_equal(summary_page_displayed, True,"Verify summary page is displayed after moving form cart")
        self.soft_assert.assert_equal(total_amount, total_price+tax, "Verifying the total cost of products")
        self.soft_assert.assert_all()

    @pytest.mark.cart
    def test_checkout_empty_user_details(self, open_browser):
        self.setup(open_browser)
        self.login_page.login(self.user,self.password)
        products = ["Sauce Labs Bolt T-Shirt","Sauce Labs Backpack"]
        self.inventory.add_products_to_cart(products)
        self.inventory.click_cart()
        self.shopping_cart_page.click_checkout()
        self.checkout_page.click_continue_btn()
        logger.info(self.checkout_page.get_error_message())
        error_display = self.checkout_page.check_error_messages()
        self.soft_assert.assert_equal(error_display, True, "Verify error message is displayed for not providing user details in checkout page")
        self.soft_assert.assert_all()
