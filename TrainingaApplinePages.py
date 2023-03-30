import time

from BasePage import SearchHelper
from selenium.webdriver.common.by import By


class Locators:
    LOGIN = (By.ID, "prependedInput")
    PASSWORD = (By.ID, "prependedInput2")
    BUT_AUTH = (By.ID, "_submit")
    SUBTITLE = (By.XPATH, "//h1[@class='oro-subtitle']")
    EXPENSES = (By.XPATH, "//*[@id='main-menu']/ul/li[2]/a/span[text()='Расходы']")
    MENU_BUSSINES_TRIP = (By.XPATH,
                     "//*[@id='main-menu']/ul/li[2]/a/span/ancestor::li//ul[@class='dropdown-menu menu_level_1']")
    NEW_BUSSINES_TRIP = (By.XPATH, "//a[@title='Создать командировку']")


class Steps(SearchHelper):

    def authorization(self):
        auth_page = SearchHelper(self)
        auth_page.go_to_site()
        auth_page.enter_word(Locators.LOGIN, "Sekretar Kompanii")
        auth_page.enter_word(Locators.PASSWORD, "testing")
        auth_page.click_on_the_search_button(Locators.BUT_AUTH)


    def checking_heading(self):
        main_page = SearchHelper(self)
        heading_site = main_page.get_text(Locators.SUBTITLE)
        heading = 'Панель быстрого запуска'
        assert heading_site == heading, f'Заголовок сайта не совпадает: *{heading_site}*!'

    def new_business_trip(self):
        new_business_trip = SearchHelper(self)
        new_business_trip.click_on_the_search_button(Locators.EXPENSES)
        new_business_trip.click_on_the_search_button(Locators.MENU_BUSSINES_TRIP)
        new_business_trip.click_on_the_search_button(Locators.NEW_BUSSINES_TRIP)

        time.sleep(7)







