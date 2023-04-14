import allure
from selenium.webdriver import Keys

from enviropments.training_appline_enviropments import EnvirTrainingAppline
from locators.training_appline_locators import Locators
from pages.BasePage import BasePage


class Steps(BasePage):
    @allure.step("Авторизация на сайте, пользователь - Sekretar Kompanii")
    def authorization1(self):
        self.find_element(Locators.LOGIN).send_keys(EnvirTrainingAppline.LOGIN1)
        self.find_element(Locators.PASSWORD).send_keys(EnvirTrainingAppline.PASSWORD)
        self.find_element(Locators.BUT_AUTH).click()

    @allure.step("Авторизация на сайте, пользователь - Taraskina Valeriya")
    def authorization2(self):
        self.find_element(Locators.LOGIN).send_keys(EnvirTrainingAppline.LOGIN2)
        self.find_element(Locators.PASSWORD).send_keys(EnvirTrainingAppline.PASSWORD)
        self.find_element(Locators.BUT_AUTH).click()

    @allure.step("Проверка заголовка 'Панель быстрого запуска'")
    def checking_heading(self):
        heading_site = self.find_element(Locators.SUBTITLE).text
        heading = 'Панель быстрого запуска'
        assert heading_site == heading, f'Заголовок сайта не совпадает: *{heading_site}*!'

    @allure.step("Заведение заявки новой командировки")
    def new_business_trip(self):
        self.find_element(Locators.EXPENSES).click()
        self.find_element(Locators.MENU_BUSSINES_TRIP).click()
        self.find_element(Locators.NEW_BUSSINES_TRIP).click()

    @allure.step("Проверка заголовка 'Создать командировку'")
    def checking_creater_bussines_trip(self):
        bt_heading = self.find_element(Locators.BUSSINES_TRIP_HEADING).text
        heading = 'Создать командировку'
        assert bt_heading == heading, f'Заголовок сайта не совпадает: *{bt_heading}*!'

    @allure.step("Заполнение полей новой командировки")
    def fill_application(self):
        self.find_element(Locators.DIVISION).click()
        self.find_element(Locators.SHOW_COMPANY).click()
        self.find_element(Locators.CHOOSE_SELECT).click()
        self.find_element(Locators.CHROME_SELECTED).click()
        self.find_element(Locators.CHECK_BOX_TICKETS).click()
        self.find_element(Locators.ARRIVAL_CITY).send_keys(EnvirTrainingAppline.ARRIVAL_CITY)
        self.find_element(Locators.DEPARTURE_DATE_PLAN).send_keys(EnvirTrainingAppline.DEPARTURE_DATE)
        self.find_element(Locators.RETURN_DATE_PLAN).send_keys(EnvirTrainingAppline.RETURN_DATE)
        self.find_element(Locators.CLOSE_CALENDAR_DATE_PLAN).send_keys(Keys.ESCAPE)
        self.find_element(Locators.SAVE_BUTTON).click()

    @allure.step("Проверка заполненых полей")
    def assert_application(self):
        self.loading()
        self.find_element(Locators.MAIN_INFORMATION).click()
        assert EnvirTrainingAppline.DIVISION == self.find_element(Locators.DIVISION).text, \
            f"Поле *{EnvirTrainingAppline.DIVISION}* заполненно не верно!"
        assert EnvirTrainingAppline.ORGANIZATION == self.find_element(Locators.BUSINESS_TRIP_COMPANY).get_attribute\
            ("value"), f"Поле *{EnvirTrainingAppline.ORGANIZATION}* заполненно не верно!"
        assert "true" == self.find_element(Locators.CHECK_BOX_TICKETS).get_attribute("checked"), \
            "В поле *Задачи* Чек-бокс должен стоять на *Заказ билетов*!"
        self.find_element(Locators.INFORMATION_BUTTON).click()
        assert EnvirTrainingAppline.DEPARTURE_CITY == self.find_element(Locators.DEPARTURE_CITY).get_attribute\
            ("value"), f"Поле *{EnvirTrainingAppline.DEPARTURE_CITY}* заполненно не верно!"
        assert EnvirTrainingAppline.ARRIVAL_CITY == self.find_element(Locators.ARRIVAL_CITY).get_attribute("value"), \
            f"Поле *{EnvirTrainingAppline.ARRIVAL_CITY}* заполненно не верно!"
        assert EnvirTrainingAppline.DEPARTURE_DATE == self.find_element(Locators.DEPARTURE_DATE_PLAN).get_attribute(
            "value"), \
            f"Поле *{EnvirTrainingAppline.DEPARTURE_DATE}* заполненно не верно!"
        assert EnvirTrainingAppline.RETURN_DATE == self.find_element(Locators.RETURN_DATE_PLAN).get_attribute\
            ("value"), f"Поле *{EnvirTrainingAppline.RETURN_DATE}* заполненно не верно!"

    @allure.step("Сохранение заполненных полей")
    def save_and_close(self):
        self.find_element(Locators.SAVE_CLOSE_BUTTON).click()
        self.loading()

    @allure.step("Проверка сообщение: 'Список командируемых сотрудников не может быть пустым'")
    def assert_validation_failed(self):
        self.find_element(Locators.BUTTON_EMPLOYEES).click()
        assert EnvirTrainingAppline.VALIDATION_FAILED == self.find_element(Locators.VALIDATION_FAILED).text, \
            "Поле об ошибке заполненно не верно!"
