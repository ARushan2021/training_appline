from pages.TrainingaApplinePages import Steps


class TestBusinessTrip:
    def test_business_trip(self, driver):
        bussines_trip = Steps(driver, "http://training.appline.ru/user/login")
        bussines_trip.go_to_site()
        bussines_trip.authorization()
        bussines_trip.checking_heading()
        bussines_trip.new_business_trip()
        bussines_trip.checking_creater_bussines_trip()
        bussines_trip.fill_application()
        bussines_trip.assert_application()
        bussines_trip.save_and_close()
        bussines_trip.assert_validation_failed()
