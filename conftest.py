import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def screenshot(driver):
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)



