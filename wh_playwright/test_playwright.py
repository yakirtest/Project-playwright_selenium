from Playwright import *
import pytest

def test_login(page:Page):
    page.goto('http://automationpractice.com/index.php')
    assert login(page) == "My Store"


def test_search_summer(page:Page):
    page.goto('http://automationpractice.com/index.php?controller=my-account')
    assert search_summer(page) == '"summer"'


def test_add_to_cart_and_pay(page:Page):
    page.goto('http://automationpractice.com/index.php')
    login(page)
    search_summer(page)
    test_url,test_title = add_to_cart_and_pay(page)
    assert test_url=='http://automationpractice.com/index.php?controller=order&ipa=7'and test_title == "Order confirmation - My Store"

