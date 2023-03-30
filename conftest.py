import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    drv = webdriver.Chrome("driver/chromedriver.exe")
    drv.maximize_window()
    yield drv
    drv.quit()
