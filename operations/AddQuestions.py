"""
Adding Questions
"""
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.GetConfigurationDetails import GetConfigurationDetails

from utilities.GetConfigurationDetails import GetConfigurationDetails

class AddQuestion(object):

    _add_question_text1 = "//div[@id='questionTitleWrap']//div[@id ='editTitle']"
    _add_question_text2 = "//div[@id='editTitle']"
    _change_type_of_question = "//a[@id='changeQType' and @class='sm-input']"
    _select_single_textbox = "//ul[@class='add-q-menu-left']//a[text()='Single Textbox']"
    _select_star_rating = "//a[contains(text(),'Star Rating')]"
    _select_date = "//a[contains(text(),'Date / Time')]"
    _time_field = "//table[@id='rows']//label[@for='toggleTimeVisible'][contains(text(),'Time Info')]"
    _dropdown = "//a[@class='option add-q-item selected']"
    _select_dropdown_type = "//div[@id='editQuestionContent']//select[@id='answerBankCategorySelect']"
    _select_yes_no = "//option[contains(text(),'Yes - No')]"
    _radio = "//a[contains(@class,'option add-q-item selected')]"
    _checkboxes = "//a[contains(text(),'Checkboxes')]"
    _always_never = "//option[contains(text(),'Always - Never')]"

    _save_question = "//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"

    _new_question = "//a[@class='main-add-question-cta wds-button wds-button--primary wds-button--icon-left']"

    def enterQuestion(self, driver):

        # Adding first question
        time.sleep(2)
        add_que1 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        time.sleep(1)
        add_que1.send_keys(GetConfigurationDetails.getEmailQuestion(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_single_textbox).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._save_question ).click()
        time.sleep(5)

        # Adding Rating question
        newQuestion = driver.find_element(By.XPATH, AddQuestion._new_question)
        newQuestion.click()
        time.sleep(5)
        # adding question details
        add_que4 = driver.find_element(By.XPATH, AddQuestion._add_question_text2)
        add_que4.send_keys(GetConfigurationDetails.getRating(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._select_star_rating).click()
        time.sleep(2)

        # Saving question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        # Adding date of using question
        newQuestion.click()

        # Adding Question details
        time.sleep(2)
        add_que3 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        add_que3.send_keys(GetConfigurationDetails.getFromWhen(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._select_date).click()
        time.sleep(5)

        # UnSelect time
        timeField = driver.find_element(By.XPATH, AddQuestion._time_field)
        timeField.click()
        time.sleep(2)

        #Saving Question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        newQuestion.click()
        time.sleep(5)
        # Meaningful data question
        add_que5 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        add_que5.send_keys(GetConfigurationDetails.getMeaningfulData(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._dropdown).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_dropdown_type).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_yes_no).click()
        time.sleep(2)

        # Saving Question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        newQuestion.click()
        time.sleep(5)
        # Friend refer Question
        add_que9 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        add_que9.send_keys(GetConfigurationDetails.getRecomendToFriends(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._radio).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_dropdown_type).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_yes_no).click()
        time.sleep(2)

        # Saving Question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        # Use Of Survey Monkey
        newQuestion.click()
        time.sleep(5)
        # Friend refer Question
        add_que10 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        add_que10.send_keys(GetConfigurationDetails.getUseSurveymonkey(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._radio).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._select_dropdown_type).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._always_never).click()
        time.sleep(2)

        # Saving Question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)
