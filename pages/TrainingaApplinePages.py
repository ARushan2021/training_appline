from selenium.webdriver import Keys

from enviropments.training_appline_enviropments import Enviropments
from locators.training_appline_locators import Locators
from pages.BasePage import BasePage


class Steps(BasePage):

    def authorization(self):
        self.find_element(Locators.LOGIN).send_keys(Enviropments.LOGIN)
        self.find_element(Locators.PASSWORD).send_keys(Enviropments.PASSWORD)
        self.find_element(Locators.BUT_AUTH).click()

    def checking_heading(self):
        heading_site = self.find_element(Locators.SUBTITLE).text
        heading = 'Панель быстрого запуска'
        assert heading_site == heading, f'Заголовок сайта не совпадает: *{heading_site}*!'

    def new_business_trip(self):
        self.find_element(Locators.EXPENSES).click()
        self.find_element(Locators.MENU_BUSSINES_TRIP).click()
        self.find_element(Locators.NEW_BUSSINES_TRIP).click()

    def checking_creater_bussines_trip(self):
        bt_heading = self.find_element(Locators.BUSSINES_TRIP_HEADING).text
        heading = 'Создать командировку'
        assert bt_heading == heading, f'Заголовок сайта не совпадает: *{bt_heading}*!'

    def fill_application(self):
        self.find_element(Locators.DIVISION).click()
        self.find_element(Locators.SHOW_COMPANY).click()
        self.find_element(Locators.CHOOSE_SELECT).click()
        self.find_element(Locators.CHROME_SELECTED).click()
        self.find_element(Locators.CHECK_BOX_TICKETS).click()
        self.find_element(Locators.ARRIVAL_CITY).send_keys(Enviropments.ARRIVAL_CITY)
        self.find_element(Locators.DEPARTURE_DATE_PLAN).send_keys(Enviropments.DEPARTURE_DATE)
        self.find_element(Locators.RETURN_DATE_PLAN).send_keys(Enviropments.RETURN_DATE)
        self.find_element(Locators.CLOSE_CALENDAR_DATE_PLAN).send_keys(Keys.ESCAPE)

    def assert_application(self):
        self.find_element(Locators.SAVE_BUTTON).click()
        self.loading()
        self.find_element(Locators.MAIN_INFORMATION).click()
        assert Enviropments.DIVISION == self.find_element(Locators.DIVISION).text, \
            f"Поле *{Enviropments.DIVISION}* заполненно не верно!"
        assert Enviropments.ORGANIZATION == self.find_element(Locators.BUSINESS_TRIP_COMPANY).get_attribute("value"), \
            f"Поле *{Enviropments.ORGANIZATION}* заполненно не верно!"
        assert "true" == self.find_element(Locators.CHECK_BOX_TICKETS).get_attribute("checked"), \
            "В поле *Задачи* Чек-бокс должен стоять на *Заказ билетов*!"
        self.find_element(Locators.INFORMATION_BUTTON).click()
        assert Enviropments.DEPARTURE_CITY == self.find_element(Locators.DEPARTURE_CITY).get_attribute("value"), \
            f"Поле *{Enviropments.DEPARTURE_CITY}* заполненно не верно!"
        assert Enviropments.ARRIVAL_CITY == self.find_element(Locators.ARRIVAL_CITY).get_attribute("value"), \
            f"Поле *{Enviropments.ARRIVAL_CITY}* заполненно не верно!"
        assert Enviropments.DEPARTURE_DATE == self.find_element(Locators.DEPARTURE_DATE_PLAN).get_attribute("value"), \
            f"Поле *{Enviropments.DEPARTURE_DATE}* заполненно не верно!"
        assert Enviropments.RETURN_DATE == self.find_element(Locators.RETURN_DATE_PLAN).get_attribute("value"), \
            f"Поле *{Enviropments.RETURN_DATE}* заполненно не верно!"

    def save_and_close(self):
        self.find_element(Locators.SAVE_CLOSE_BUTTON).click()
        self.loading()

    def assert_validation_failed(self):
        assert Enviropments.VALIDATION_FAILED == self.find_element(Locators.VALIDATION_FAILED).text, \
            "Поле об ошибке заполненно не верно!"
