import pytest
from selenium import webdriver
from pages import AuthPage, MainPage, ItemPage, AddItemPage
from config import Config


conf = Config()

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    yield driver
    driver.close()


@pytest.fixture()
def login(driver):
    # url = "https://funnyoctopus.xyz/auth/login"
    # url = "http://127.0.0.1:5000/auth/login"
    url = conf.base_url + "auth/login"
    login = conf.login
    password = conf.password
    driver.get(url)
    ap = AuthPage(driver)
    ap.auth(login, password)


@pytest.fixture()
def auth_page(driver):
    return AuthPage(driver)


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def item_page(driver):
    return ItemPage(driver)


@pytest.fixture()
def add_item_page(driver):
    return AddItemPage(driver)

