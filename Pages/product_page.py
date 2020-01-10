from .locators import ProductPageLocators
from .base_page import BasePage

class ProductPage(BasePage):
    def add_product_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON)
        button.click()

    def assert_product_was_added(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME_FULL_MESSAGE).text, \
            "The product name in the basket does not match what is added"

    def assert_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text in self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, \
            "The total sum in the basket does not match with product price"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message should disappear"
