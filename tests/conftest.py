import sys
import os

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


@pytest.fixture
def driver() -> WebDriver:
    # Initialize the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # Headless mode - browser with UI (faster)
    # options.add_experimental_option("detach", True)  # Leave browser open

    # Connect to Selenium Hub
    # Instead of localhost, change it to the name of the server running Selenium hub
    if 'SELENIUM_URL' in os.environ:
        hub_url = os.environ['SELENIUM_URL']
        driver = webdriver.Remote(command_executor=hub_url, options=options)
    else:
        driver = webdriver.Chrome(options=options)

    yield driver
    # Quit the WebDriver
    driver.quit()


def pytest_exception_interact(node, call, report):
    if report.failed:
        driver = node.funcargs['driver']
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="screenshot", attachment_type=allure.attachment_type.PNG)
