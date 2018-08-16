"""
Operations on Survey
"""

from selenium.webdriver.common.by import By
import time

class OperationsOnSurvey(object):

    _survey_title_click = "//span[@class='title-text']"
    _survey_title = "surveyTitle"
    _save_edited_survey = "//form[@id='surveyTitleForm']//a[contains(text(),'SAVE')]"
    #_page_title_button = "//h2[@class='page-title-wrapper clearfix']"
    _page_title_text = "//div[@id='pageTitle']"
    _save_page_title = "//form[@id='pageTitleForm']//a[@class='wds-button wds-button--sm save'][contains(text(),'SAVE')]"



    def editAndSaveSurveyTitle(self, driver):
        #Clicking element to edit
        surveyTitleClick = driver.find_element(By.XPATH, OperationsOnSurvey()._survey_title_click)
        surveyTitleClick.click()
        time.sleep(2)

        # Editing Element
        surveyTitleText = driver.find_element(By.ID, OperationsOnSurvey()._survey_title)
        # clear existing title
        surveyTitleText.clear()
        surveyTitleText.send_keys("Changed Survey Title")
        time.sleep(2)

        # Saving edited element
        saveEditedSurvey = driver.find_element(By.XPATH, OperationsOnSurvey()._save_edited_survey)
        saveEditedSurvey.click()
        time.sleep(2)

    def addPageTitle(self, driver):
        # Clicking page title button
        #pageTitleButton = driver.find_element(By.XPATH, OperationsOnSurvey()._page_title_button)
        #pageTitleButton.click()
        driver.execute_script("document.getElementsByClassName('page-title user-generated empty wds-button wds-button--ghost-filled wds-button--sm')[0].click();")
        time.sleep(5)

        # Adding Page Text
        pageText = driver.find_element(By.XPATH, OperationsOnSurvey()._page_title_text)
        pageText.send_keys("Page Title from Selenium")
        time.sleep(2)

        # Saving page title
        savePagetitle = driver.find_element(By.XPATH, OperationsOnSurvey()._save_page_title)
        savePagetitle.click()
        time.sleep(5)