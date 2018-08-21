"""
Adding Questions
"""
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utilities.GetConfigurationDetails import GetConfigurationDetails

class AddQuestion(object):

    _add_question_text1 = "//div[@id='questionTitleWrap']//div[@id ='editTitle']"
    _add_question_text2 = "//div[@id='editTitle']"
    _change_type_of_question = "//a[@id='changeQType' and @class='sm-input']"
    _select_single_textbox = "//a[contains(text(),'Single Textbox')]"
    _select_star_rating = "//a[contains(text(),'Star Rating')]"
    _select_date = "//a[contains(text(),'Date / Time')]"
    _time_field = "//table[@id='rows']//label[@for='toggleTimeVisible'][contains(text(),'Time Info')]"
    _dropdown = "//a[@class='option add-q-item selected']"
    _select_dropdown_type = "//div[@id='editQuestionContent']//select[@id='answerBankCategorySelect']"
    _select_yes_no = "//option[contains(text(),'Yes - No')]"
    _radio = "//a[contains(@class,'option add-q-item selected')]"
    _checkboxes = "//a[contains(text(),'Checkboxes')]"
    _always_never = "//option[contains(text(),'Always - Never')]"
    _comment_box = "//a[contains(text(),'Comment Box')]"
    _add_options = "//tbody[contains(@class,'answerSetting singleLine')]//tr[4]//td[4]//a[1]"
    _question_bank_option = "//table[@class='answersTable choicesTable']/tbody[@class='answerSetting singleLine']/tr[4]/td[2]/div[1]/div[1]"
    _themes = "//table[@class='answersTable choicesTable']/tbody[@class='answerSetting singleLine']/tr[5]/td[2]/div[1]/div[1]"
    _graphical_results = "//table[@class='answersTable choicesTable']/tbody[@class='answerSetting singleLine']/tr[6]/td[2]/div[1]/div[1]"
    _template = "//table[@class='answersTable choicesTable']/tbody[@class='answerSetting singleLine']/tr[7]/td[2]/div[1]/div[1]"
    _collectors = "//table[@class='answersTable choicesTable']/tbody[@class='answerSetting singleLine']/tr[8]/td[2]/div[1]/div[1]"
    _matrix_rating_scale = "//a[contains(text(),'Matrix / Rating Scale')]"
    _save_question = "//div[@id='editQuestion']/section[@class='t1']//a[text()='SAVE']"
    _service = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _support = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _responsive = "//section[2]/div[2]/div[2]/div[1]/div[2]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _very_good = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[1]"
    _good = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _avarage = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _below_avarage = "//section[2]/div[2]/div[2]/div[1]/div[3]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _remove_option = "//tr[6]//a[@title='Delete this choice.']"
    _multiple_text_boxes = "//a[contains(text(),'Multiple Textboxes')]"
    _most_like_feature1 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[1]/div[1]/div[1]"
    _most_like_feature2 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[1]/div[1]/div[1]"
    _most_like_feature3 = "//section[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[1]/div[1]/div[1]"
    _new_question = "//a[@class='main-add-question-cta wds-button wds-button--primary wds-button--icon-left']"

    def enterQuestion(self, driver):

        # Adding email question
        add_que1 = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, AddQuestion._add_question_text1)))
        add_que1.send_keys(GetConfigurationDetails.getEmailQuestion(self))
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, AddQuestion._change_type_of_question))).click()
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

        newQuestion.click()
        time.sleep(5)

        # Comment and Feedback
        add_que1 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        time.sleep(1)
        add_que1.send_keys(GetConfigurationDetails.getCommentsFeedback(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._comment_box).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        newQuestion.click()
        time.sleep(5)
        # Features of Survey monkey
        add_que1 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        time.sleep(1)
        add_que1.send_keys(GetConfigurationDetails.getFeatures(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._checkboxes).click()
        time.sleep(2)
        # Adding options
        driver.find_element(By.XPATH, AddQuestion._add_options).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._add_options).click()
        time.sleep(2)
        questionBankk = driver.find_element(By.XPATH, AddQuestion._question_bank_option)
        time.sleep(2)
        questionBankk.send_keys(GetConfigurationDetails.getQuestionBank(self))
        time.sleep(2)
        themess = driver.find_element(By.XPATH, AddQuestion._themes)
        themess.send_keys(GetConfigurationDetails.getThemes(self))
        time.sleep(2)
        graphicalResultss = driver.find_element(By.XPATH, AddQuestion._graphical_results)
        graphicalResultss.send_keys(GetConfigurationDetails.getGraphical(self))
        time.sleep(2)
        templatee = driver.find_element(By.XPATH, AddQuestion._template)
        templatee.send_keys(GetConfigurationDetails.getTemplate(self))
        time.sleep(2)
        collectorss = driver.find_element(By.XPATH, AddQuestion._collectors)
        collectorss.send_keys(GetConfigurationDetails.getCollectors(self))
        time.sleep(2)
        # saving question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        newQuestion.click()
        time.sleep(5)
        # Matrix Rating of Survey monkey
        add_que1 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        time.sleep(1)
        add_que1.send_keys(GetConfigurationDetails.getRateFeatures(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._matrix_rating_scale).click()
        time.sleep(2)
        servicee = driver.find_element(By.XPATH, AddQuestion._service)
        servicee.send_keys(GetConfigurationDetails.getService(self))
        time.sleep(2)
        supportt = driver.find_element(By.XPATH, AddQuestion._support)
        supportt.send_keys(GetConfigurationDetails.getSupport(self))
        time.sleep(2)
        responsiveness = driver.find_element(By.XPATH, AddQuestion._responsive)
        responsiveness.send_keys(GetConfigurationDetails.getResponsive(self))
        time.sleep(2)
        veryGoodd = driver.find_element(By.XPATH, AddQuestion._very_good)
        veryGoodd.send_keys(GetConfigurationDetails.getVeryGood(self))
        time.sleep(2)
        godd = driver.find_element(By.XPATH, AddQuestion._good)
        godd.send_keys(GetConfigurationDetails.getGood(self))
        time.sleep(2)
        avaragee = driver.find_element(By.XPATH, AddQuestion._avarage)
        avaragee.send_keys(GetConfigurationDetails.getAvarage(self))
        time.sleep(2)
        belowAvaragee = driver.find_element(By.XPATH, AddQuestion._below_avarage)
        belowAvaragee.send_keys(GetConfigurationDetails.getBelowAvarage(self))
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._remove_option).click()
        time.sleep(2)
        # saving question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)

        # Multiple Text box of Survey monkey
        newQuestion.click()
        time.sleep(5)
        add_que1 = driver.find_element(By.XPATH, AddQuestion._add_question_text1)
        time.sleep(1)
        add_que1.send_keys(GetConfigurationDetails.getFeatureList(self))
        time.sleep(5)
        driver.find_element(By.XPATH, AddQuestion._change_type_of_question).click()
        time.sleep(2)
        driver.find_element(By.XPATH, AddQuestion._multiple_text_boxes).click()
        time.sleep(2)
        featureLits1 = driver.find_element(By.XPATH, AddQuestion._most_like_feature1)
        featureLits1.send_keys("Feature 1")
        time.sleep(2)
        featureLits2 = driver.find_element(By.XPATH, AddQuestion._most_like_feature2)
        featureLits2.send_keys("Feature 2")
        time.sleep(2)
        featureLits3 = driver.find_element(By.XPATH, AddQuestion._most_like_feature3)
        featureLits3.send_keys("Feature 3")
        time.sleep(2)

        # saving question
        driver.find_element(By.XPATH, AddQuestion._save_question).click()
        time.sleep(5)