
from utilities import ChromeUtility
from utilities import GetConfigurationDetails
from selenium.webdriver.common.by import By
import time

from operations.LoginOperation import LoginOperation
from operations.CreateSurvey import CreateSurvey

class SeleniumWebdriverAutomationAssignment(object):

    def __init__(self):
        driver = ChromeUtility.ChromeUtility.getChromeDriver(self)
        url = GetConfigurationDetails.GetConfigurationDetails.getURL(self)
        driver.get(url)

        #Login Operations
        LoginOperation.navToLogin(self, driver)
        time.sleep(2)
        LoginOperation.sendUsernameAndPass(self, driver)
        time.sleep(2)
        LoginOperation.sendPassword(self, driver)
        time.sleep(2)
        LoginOperation.clicklogIn(self, driver)

        #Survay Operations
        CreateSurvey.clickCreateSurvey(self, driver)
        CreateSurvey.sendSyrveyTitle(self, driver)
        CreateSurvey.surveyCategory(self, driver)
        CreateSurvey.buttonCreateSurvey(self, driver)


startt = SeleniumWebdriverAutomationAssignment()
