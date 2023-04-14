from selenium.webdriver.common.by import By

from enviropments.training_appline_enviropments import EnvirTrainingAppline


class Locators:
    LOADER_MASK = (By.XPATH, "//div[@class='loader-mask shown']")
    LOGIN = (By.ID, "prependedInput")
    PASSWORD = (By.ID, "prependedInput2")
    BUT_AUTH = (By.ID, "_submit")
    SUBTITLE = (By.XPATH, "//h1[@class='oro-subtitle']")
    EXPENSES = (By.XPATH, "//div[@id='main-menu']/ul//a/span[text()='Расходы']")
    MENU_BUSSINES_TRIP = (By.XPATH, "//span[text()='Командировки']")
    NEW_BUSSINES_TRIP = (By.XPATH, "//a[@title='Создать командировку']")
    BUSSINES_TRIP_HEADING = (By.XPATH, "//h1[@class='user-name']")
    DIVISION = (By.XPATH, f"//option[text()='{EnvirTrainingAppline.DIVISION}']")
    SHOW_COMPANY = (By.XPATH, "//a[@id='company-selector-show']")
    CHOOSE_SELECT = (By.XPATH, "//span[@class='select2-chosen']")
    CHROME_SELECTED = (By.XPATH, f"//div[text()='{EnvirTrainingAppline.ORGANIZATION}']")
    CHECK_BOX_TICKETS = (By.XPATH, "//input[@data-name='field__1']")
    ARRIVAL_CITY = (By.XPATH, "//input[@name='crm_business_trip[arrivalCity]']")
    DEPARTURE_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_departureDatePlan')]")
    RETURN_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_returnDatePlan')]")
    CLOSE_CALENDAR_DATE_PLAN = (By.XPATH, "//input[contains(@id, 'date_selector_crm_business_trip_returnDatePlan')]")
    MAIN_INFORMATION = (By.XPATH, "//a[contains(text(), 'Основная информация')]")
    BUSINESS_TRIP_COMPANY = (By.XPATH, "//input[@data-ftid='crm_business_trip_company']")
    SAVE_BUTTON = (By.XPATH, "//button[@class='btn btn-success main-group action-button']")
    INFORMATION_BUTTON = (By.XPATH, "//a[contains(text(), 'Сведения')]")
    DEPARTURE_CITY = (By.XPATH, "//input[@name='crm_business_trip[departureCity]']")
    SAVE_CLOSE_BUTTON = (By.XPATH, "//button[contains(text(), 'Сохранить и закрыть')]")
    VALIDATION_FAILED = (By.XPATH, "//div/div/fieldset/div/div/div/span[@class='validation-failed']")
    BUTTON_EMPLOYEES = (By.XPATH, "//a[text()='Командированные сотрудники']")
