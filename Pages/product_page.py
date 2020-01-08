from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button.click()

    def assert_product_was_added(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text in self.browser.find_element(*ProductPageLocators.BOOK_NAME_FULL_MESSAGE).text, "The product name in the basket does not match what is added"

    def assert_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, "The total sum in the basket does not match with product price"
