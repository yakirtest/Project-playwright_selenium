import pytest
from wh_selenium.selenium_Edge import *

@pytest.fixture()
def driver(url):
    driver =driver_edge()
    driver.open_edge_brow(url)
    yield driver

@pytest.fixture()
def url():
    url ="http://automationpractice.com/index.php"
    yield url

def test_close_edge_brow(driver):
    assert driver.close_edge_brow()

def test_open_edge_brow(driver,url):
    assert driver.open_edge_brow(url)
    driver.close_edge_brow()

def test_login(driver,url):
    driver.open_edge_brow(url)
    assert driver.login()=="SubmitLogin"
    driver.close_edge_brow()


def test_search_summer(driver,url):
    driver.open_edge_brow(url)
    driver.login()
    assert driver.search_summer()=="submit"
    driver.close_edge_brow()

def test_add_to_cart_summer_dress_min_price(driver,url):
    driver.open_edge_brow(url)
    driver.login()
    driver.search_summer()
    assert driver.add_to_cart_summer_dress_min_price()==16.4
    driver.close_edge_brow()

def test_pay_dress(driver,url):
    driver.open_edge_brow(url)
    driver.login()
    driver.search_summer()
    driver.add_to_cart_summer_dress_min_price()
    assert driver.pay_dress()
    driver.close_edge_brow()
