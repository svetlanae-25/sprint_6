import pytest
# import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.main_page_locators import MainPageLocators

from curl import *

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.get(main_site)
    yield driver
    driver.quit()

@pytest.fixture
def accept_cookies(driver):
    try:
        cookie_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable(MainPageLocators.COOKIE_ACCEPT_BUTTON))
        cookie_button.click()
    except:
        pass  # Если cookies нет, просто продолжаем




