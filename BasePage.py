from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import conftest


class BasePage:

    def __init__(self, drv):
        self.drv = drv
        self.base_url = "http://training.appline.ru/user/login"

    def find_element(self, locator, time=15):
        return WebDriverWait(self.drv, time).until(EC.presence_of_element_located(locator),
                                                   message=f"Не удается найти элемент по локатору {locator}")

    def go_to_site(self):
        return self.drv.get(self.base_url)


class SearchHelper(BasePage):

    def enter_word(self, locator, word):
        search_field = self.find_element(locator)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self, locator):
        return self.find_element(locator, time=15).click()

    def get_text(self, locator):
        return self.find_element(locator, time=15).text
