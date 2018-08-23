"""
Creating survey
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.basepage import BasePage
import time

class CreateSurvey(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    _nav_create_survey = "//a[contains(@class,'create-survey alt btn SL_split')]"
    _survey_title = "surveyTitle"
    _survey_category = "//div[@class='Select-placeholder']"
    _select_survey = "react-select-2--option-4"
    _button_create_survey = "//button[@class='wds-button']"
    _survey_from_scratch = "//button[@class='wds-button']//span[contains(text(),'START FROM SCRATCH')]"
    _popupRemove = "//a[@class='wds-button wds-button--sm wds-button--ghost'][contains(text(),'REMOVE')]"

    def clickCreateSurvey(self):
        self.elementClick(self._nav_create_survey,locatorType="xpath")
        return True

    def sendSyrveyTitle(self):
        self.sendKeys("Test Title from Selenium",self._survey_title)
        return True

    def surveyCategory(self):
        self.elementClick(self._survey_category, locatorType="xpath")
        self.elementClick(self._select_survey)
        return True

    def buttonCreateSurvey(self):
        self.elementClick(self._button_create_survey, locatorType="xpath")
        return True

    def handlePopup(self):
        self.elementClick(self._popupRemove, locatorType="xpath")
        return True