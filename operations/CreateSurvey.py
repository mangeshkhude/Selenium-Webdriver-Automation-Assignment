"""
Creating survey
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CreateSurvey(object):

    _nav_create_survey = "//a[contains(@class,'create-survey alt btn SL_split')]"
    _survey_title = "surveyTitle"
    _survey_category = "//div[@class='Select-placeholder']"
    _select_survey = "react-select-2--option-4"
    _button_create_survey = "//button[@class='wds-button']"
    _survey_from_scratch = "//button[@class='wds-button']//span[contains(text(),'START FROM SCRATCH')]"
    _popupRemove = "//a[@class='wds-button wds-button--sm wds-button--ghost'][contains(text(),'REMOVE')]"

    def clickCreateSurvey(self, driver):
        createSurveyElement = driver.find_element(By.XPATH, CreateSurvey()._nav_create_survey)
        createSurveyElement.click()

    def sendSyrveyTitle(self, driver):
        surveyTitle = driver.find_element(By.ID, CreateSurvey()._survey_title)
        surveyTitle.send_keys("Test Title from Selenium")

    def surveyCategory(self, driver):
        surveyCategory = driver.find_element(By.XPATH, CreateSurvey()._survey_category)
        surveyCategory.click()
        selectSurvey = driver.find_element(By.ID, CreateSurvey()._select_survey)
        selectSurvey.click()

    def buttonCreateSurvey(self, driver):
        createSurvey = driver.find_element(By.XPATH, CreateSurvey()._button_create_survey)
        createSurvey.click()

    def handlePopup(self, driver):
        #Wait till browser loads the element
        try:
            removePopup = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, CreateSurvey()._popupRemove)))
            removePopup.click()
        except:
            removePopup = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, CreateSurvey()._popupRemove)))
            removePopup.click()
