"""
Operations on Survey
"""

from selenium.webdriver.common.by import By
from base.basepage import BasePage
import time

class OperationsOnSurvey(BasePage):

    _survey_title_click = "//span[@class='title-text']"
    _survey_title = "surveyTitle"
    _save_edited_survey = "//form[@id='surveyTitleForm']//a[contains(text(),'SAVE')]"
    #_page_title_button = "//h2[@class='page-title-wrapper clearfix']"
    _page_title_text = "//div[@id='pageTitle']"
    _save_page_title = "//form[@id='pageTitleForm']//a[contains(text(),'SAVE')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def editAndSaveSurveyTitle(self):

        #Clicking element to edit
        self.elementClick(self._survey_title_click, locatorType="xpath")

        # Editing Element
        surveyTitleText = self.getElement(self._survey_title)

        # clear existing title
        surveyTitleText.clear()
        self.sendKeys("Changed Survey Title", surveyTitleText)

        # Saving edited element
        self.elementClick(self._save_edited_survey, locatorType="xpath")

        return True



    # def addPageTitle(self, driver):
    #     # Clicking page title button
    #     #pageTitleButton = driver.find_element(By.XPATH, OperationsOnSurvey()._page_title_button)
    #     #pageTitleButton.click()
    #     driver.execute_script("document.getElementsByClassName('page-title user-generated empty wds-button wds-button--ghost-filled wds-button--sm')[0].click();")
    #     time.sleep(5)
    #
    #     # Adding Page Text
    #     pageText = driver.find_element(By.XPATH, OperationsOnSurvey()._page_title_text)
    #     pageText.send_keys("Page Title from Selenium")
    #     time.sleep(2)
    #
    #     # Saving page title
    #     savePagetitle = driver.find_element(By.XPATH, OperationsOnSurvey()._save_page_title)
    #     savePagetitle.click()
    #     time.sleep(5)