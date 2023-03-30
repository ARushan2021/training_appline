from TrainingaApplinePages import Steps


def test(browser):

    Steps.authorization(browser)
    Steps.checking_heading(browser)
    Steps.new_business_trip(browser)
    Steps.checking_creater_bussines_trip(browser)
    Steps.fill_application(browser)










