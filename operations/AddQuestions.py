"""
Adding Questions
"""
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.GetConfigurationDetails import GetConfigurationDetails
from base.basepage import BasePage

class AddQuestion(BasePage):

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

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def emailQuestion(self):

        # Adding email question
        self.sendKeys(GetConfigurationDetails.getEmailQuestion(GetConfigurationDetails), locator=self._add_question_text2, locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._select_single_textbox, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def ratingQuestion(self):

        # Adding Rating question
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getRating(GetConfigurationDetails), locator=self._add_question_text2, locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._select_star_rating, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def dateOfUsing(self):

        # Adding date of using question
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getRating(GetConfigurationDetails), locator=self._add_question_text2,locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._select_date, locatorType="xpath")
        self.elementClick(self._time_field, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def meaningfulData(self):
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getMeaningfulData(GetConfigurationDetails), locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._dropdown, locatorType="xpath")
        self.elementClick(self._select_dropdown_type, locatorType="xpath")
        self.elementClick(self._select_yes_no, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")

    def recomandFriendsQuestion(self):

        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getRecomendToFriends(GetConfigurationDetails),
                      locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._radio, locatorType="xpath")
        self.elementClick(self._select_dropdown_type, locatorType="xpath")
        self.elementClick(self._select_yes_no, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def useSurveyMonkeyQuestion(self):

        # Use Of Survey Monkey
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getUseSurveymonkey(GetConfigurationDetails),
                      locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._radio, locatorType="xpath")
        self.elementClick(self._select_dropdown_type, locatorType="xpath")
        self.elementClick(self._always_never, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def commentsFeedbackQuestion(self):

        # Comment and Feedback
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getCommentsFeedback(GetConfigurationDetails),
                      locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._comment_box, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def featureQuestion(self):

        # Features of Survey monkey
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getFeatures(GetConfigurationDetails),
                      locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._checkboxes, locatorType="xpath")
        self.elementClick(self._add_options, locatorType="xpath")
        self.elementClick(self._add_options, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getQuestionBank(GetConfigurationDetails),locator=self._question_bank_option, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getThemes(GetConfigurationDetails),
                      locator=self._themes, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getGraphical(GetConfigurationDetails),
                      locator=self._graphical_results, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getTemplate(GetConfigurationDetails),
                      locator=self._template, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getCollectors(GetConfigurationDetails),
                      locator=self._collectors, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def matrixRatingQuestion(self):

        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getRateFeatures(GetConfigurationDetails),
                      locator=self._add_question_text2,
                      locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._matrix_rating_scale, locatorType="xpath")

        self.sendKeys(GetConfigurationDetails.getService(GetConfigurationDetails),
                      locator=self._service, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getSupport(GetConfigurationDetails),
                      locator=self._support, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getResponsive(GetConfigurationDetails),
                      locator=self._responsive, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getVeryGood(GetConfigurationDetails),
                      locator=self._very_good, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getGood(GetConfigurationDetails),
                      locator=self._good, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getAvarage(GetConfigurationDetails),
                      locator=self._avarage, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getBelowAvarage(GetConfigurationDetails),
                      locator=self._below_avarage, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getBelowAvarage(GetConfigurationDetails),
                      locator=self._below_avarage, locatorType="xpath")
        self.elementClick(self._remove_option, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True

    def ratefeatureQuestion(self):

        # Multiple Text box of Survey monkey
        self.elementClick(locator=self._new_question, locatorType="xpath")
        self.sendKeys(GetConfigurationDetails.getRateFeatures(GetConfigurationDetails),
                      locator=self._add_question_text2, locatorType="xpath")
        self.elementClick(self._change_type_of_question, locatorType="xpath")
        self.elementClick(self._multiple_text_boxes, locatorType="xpath")

        self.sendKeys("Feature 1", locator=self._most_like_feature1, locatorType="xpath")
        self.sendKeys("Feature 2", locator=self._most_like_feature2, locatorType="xpath")
        self.sendKeys("Feature 3", locator=self._most_like_feature3, locatorType="xpath")
        self.elementClick(self._save_question, locatorType="xpath")
        return True


