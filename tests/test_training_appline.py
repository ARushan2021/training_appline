import allure
import pytest

from pages.TrainingApplinePages import Steps
from enviropments.training_appline_enviropments import EnvirTrainingAppline


@allure.suite("Портал: Training Appline")
class TestTrainingAppline():
    @allure.feature("Командировка")
    class TestBusinessTrip:

        @allure.title("Заведение новой заявки на командировку")
        @pytest.mark.parametrize('login, password',
                                 [(EnvirTrainingAppline.LOGIN1, EnvirTrainingAppline.PASSWORD1),
                                  (EnvirTrainingAppline.LOGIN2, EnvirTrainingAppline.PASSWORD2)]
                                 )
        def test_business_trip1(self, driver, screenshot, login, password):
            bussines_trip = Steps(driver, "http://training.appline.ru/user/login")
            bussines_trip.go_to_site()
            bussines_trip.authorization(login, password)
            bussines_trip.checking_heading()
            bussines_trip.new_business_trip()
            bussines_trip.checking_creater_bussines_trip()
            bussines_trip.fill_application()
            bussines_trip.assert_application()
            bussines_trip.save_and_close()
            bussines_trip.assert_validation_failed()


# pytest --alluredir=tests_reports .\tests\test_training_appline.py - запуск теста из терминала
# allure serve tests_reports - формирование allure в html
