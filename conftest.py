import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome("driver/chromedriver.exe")
    driver.maximize_window()
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    driver.quit()
