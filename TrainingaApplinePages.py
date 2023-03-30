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
    BUSSINES_TRIP_HEADING = (By.XPATH, "//h1[@class='user-name']")
    DIVISION = (By.XPATH, "//option[@value='1']")
    SHOW_COMPANY = (By.XPATH, "//a[@id='company-selector-show']")
    CHOOSE_SELECT = (By.XPATH, "//span[@class='select2-chosen']")
    CHROME_SELECTED = (By.XPATH, "//div[text()='(Хром) Призрачная Организация Охотников']")
    CHECK_BOX_TICKETS = (By.XPATH, "//input[@data-name='field__1']")
    ARRIVAL_CITY = (By.XPATH, "//input[@name='crm_business_trip[arrivalCity]']")
    DEPARTURE_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_departureDatePlan')]")
    RETURN_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_returnDatePlan')]")
    CLOSE_CALENDAR_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_returnDatePlan')]")




class Steps(SearchHelper):

    def authorization(self):
        auth_page = SearchHelper(self)
        auth_page.go_to_site()
        auth_page.enter_word(Locators.LOGIN, "Sekretar Kompanii")
        auth_page.enter_word(Locators.PASSWORD, "testing")
        auth_page.click_on_the_search(Locators.BUT_AUTH)


    def checking_heading(self):
        main_page = SearchHelper(self)
        heading_site = main_page.get_text(Locators.SUBTITLE)
        heading = 'Панель быстрого запуска'
        assert heading_site == heading, f'Заголовок сайта не совпадает: *{heading_site}*!'

    def new_business_trip(self):
        new_business_trip = SearchHelper(self)
        new_business_trip.click_on_the_search(Locators.EXPENSES)
        new_business_trip.click_on_the_search(Locators.MENU_BUSSINES_TRIP)
        new_business_trip.click_on_the_search(Locators.NEW_BUSSINES_TRIP)


    def checking_creater_bussines_trip(self):
        bt_page = SearchHelper(self)
        bt_heading = bt_page.get_text(Locators.BUSSINES_TRIP_HEADING)
        heading = 'Создать командировку'
        assert bt_heading == heading, f'Заголовок сайта не совпадает: *{bt_heading}*!'

    def fill_application(self):
        fill_application = SearchHelper(self)
        fill_application.click_on_the_search(Locators.DIVISION)
        fill_application.click_on_the_search(Locators.SHOW_COMPANY)
        fill_application.click_on_the_search(Locators.CHOOSE_SELECT)
        fill_application.click_on_the_search(Locators.CHROME_SELECTED)
        fill_application.click_on_the_search(Locators.CHECK_BOX_TICKETS)
        fill_application.enter_word(Locators.ARRIVAL_CITY, "Санкт-Петербург")
        fill_application.enter_word(Locators.DEPARTURE_DATE_PLAN, "06.03.2023")
        fill_application.enter_word(Locators.RETURN_DATE_PLAN, "05.04.2023")
        fill_application.get_escape(Locators.CLOSE_CALENDAR_DATE_PLAN)
        time.sleep(10)

    #def assert_aclication(self):












