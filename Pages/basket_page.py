from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket item is presented, but should not be"

    def user_can_see_message_about_empty_basket(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text, \
            "The user don't see the message that basket is empty"
