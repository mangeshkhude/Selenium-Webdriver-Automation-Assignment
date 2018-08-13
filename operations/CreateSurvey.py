"""
Creating survey
"""
from selenium.webdriver.common.by import By
import time

class CreateSurvey(object):

    _nav_create_survey = "//a[contains(@class,'create-survey alt btn SL_split')]"
    _survey_title = "surveyTitle"
    _survey_category = "//div[@class='Select-placeholder']"
    _select_survey = "react-select-2--option-4"
    _button_create_survey = "//button[@class='wds-button']"
    _survey_from_scratch = "//button[@class='wds-button']//span[contains(text(),'START FROM SCRATCH')]"

    def clickCreateSurvey(self, driver):
        createSurveyElement = driver.find_element(By.XPATH, CreateSurvey()._nav_create_survey)
        createSurveyElement.click()

    def sendSyrveyTitle(self, driver):
        surveyTitle = driver.find_element(By.ID, CreateSurvey()._survey_title)
        surveyTitle.send_keys("Test Title from Selenium")
        time.sleep(2)

    def surveyCategory(self, driver):
        surveyCategory = driver.find_element(By.XPATH, CreateSurvey()._survey_category)
        surveyCategory.click()
        selectSurvey = driver.find_element(By.ID, CreateSurvey()._select_survey)
        time.sleep(2)
        selectSurvey.click()

    def buttonCreateSurvey(self, driver):
        if driver.find_element(By.XPATH, CreateSurvey()._button_create_survey) is not None:
            createSurvey = driver.find_element(By.XPATH, CreateSurvey()._button_create_survey)
            createSurvey.click()
            time.sleep(60)
        elif driver.find_element(By.XPATH, CreateSurvey()._survey_from_scratch) is not None :
            createSurvey = driver.find_element(By.XPATH, CreateSurvey()._survey_from_scratch)
            createSurvey.click()
            time.sleep(60)