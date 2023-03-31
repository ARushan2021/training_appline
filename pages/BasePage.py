from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators.training_appline_locators import Locators

class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def go_to_site(self):
        self.driver.get(self.base_url)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не удается найти элемент по локатору {locator}")

    def loading(self, time=15):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(Locators.LOADER_MASK),
                                               message=f'Страница не успела загрузиться!')
