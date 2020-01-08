import selenium
from selenium import webdriver
import pytest
import time
from .Pages.product_page import ProductPage
from .Pages.base_page import BasePage


def test_guest_can_add_product_to_basket(browser):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.assert_product_was_added()
    page.assert_product_price()
    time.sleep(2)
