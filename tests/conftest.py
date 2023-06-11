import pytest
from selene import browser
from selenium import webdriver

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_conf():
    chrome_options = webdriver.ChromeOptions()
    browser.config.driver_options = chrome_options
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    browser.quit()