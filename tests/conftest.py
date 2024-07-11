import allure
import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    with allure.step("Открываем главую страницу GitHub"):
        browser.config.base_url = 'https://github.com'
        browser.config.window_width = 1920
        browser.config.window_height = 1080
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        # driver_options.add_argument("--headless")
        browser.config.driver_options = driver_options

        yield
        browser.quit()
