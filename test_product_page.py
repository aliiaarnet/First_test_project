from .Pages.locators import ProductPageLocators
from .Pages.product_page import ProductPage
from .Pages.base_page import BasePage
from selenium import webdriver
import selenium
import pytest
import time

# @pytest.mark.parametrize('promo_offer', [0, 1, 2, 3, "4", "5", "6",
#                                         pytest.param(7, marks=pytest.mark.xfail),
#                                         "8", "9"])
@pytest.mark.parametrize('promo_offer', [0])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.assert_product_was_added()
    page.assert_product_price()

@pytest.mark.parametrize('promo_offer', [0])
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.parametrize('promo_offer', [0])
def test_guest_cant_see_success_message(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.parametrize('promo_offer', [0])
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_disappear_success_message()