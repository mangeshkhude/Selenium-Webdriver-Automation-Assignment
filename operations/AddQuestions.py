"""
Adding Questions
"""
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.GetConfigurationDetails import GetConfigurationDetails

class AddQuestion(object):

    _add_question_text = "//div[@id='editTitle']"
    _type_of_email_question = "changeQType"
    _save_question = "//div[@id='editQuestion']//section[contains(@class,'t1')]//a[contains(@class,'wds-button wds-button--sm save')][contains(text(),'SAVE')]"

    def enterQuestion(self, driver):

        # Adding question
        try:
            addQuestionText = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, AddQuestion()._add_question_text)))
            addQuestionText.send_keys(GetConfigurationDetails.getEmailQuestion(self))

            #Adding Type of question

            questionType = driver.find_element(By.ID, AddQuestion()._type_of_email_question)
            questionType.click()

            # Save Question
            driver.execute_script("window.scrollBy(0, 200);")
            saveQuestion = driver.find_element(By.ID, AddQuestion()._save_question)
            saveQuestion.click()
            time.sleep(2)
        except:
            addQuestionText = WebDriverWait(driver, 120).until(
                EC.presence_of_element_located((By.XPATH, AddQuestion()._add_question_text)))
            addQuestionText.send_keys(GetConfigurationDetails.getEmailQuestion(self))