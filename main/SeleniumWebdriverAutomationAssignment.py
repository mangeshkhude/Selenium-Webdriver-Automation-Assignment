
from utilities import ChromeUtility
from utilities import GetConfigurationDetails
import time

from operations.LoginOperation import LoginOperation
from operations.CreateSurvey import CreateSurvey
from operations.OperationsOnSurvey import OperationsOnSurvey
from operations.AddQuestions import AddQuestion

class SeleniumWebdriverAutomationAssignment(object):

    def __init__(self):
        driver = ChromeUtility.ChromeUtility.getChromeDriver(self)
        url = GetConfigurationDetails.GetConfigurationDetails.getURL(self)
        driver.get(url)

        # Login Operations
        LoginOperation.navToLogin(self, driver)
        LoginOperation.sendUsernameAndPass(self, driver)
        LoginOperation.sendPassword(self, driver)
        LoginOperation.clicklogIn(self, driver)

        # Survay Operations
        CreateSurvey.clickCreateSurvey(self, driver)
        CreateSurvey.sendSyrveyTitle(self, driver)
        CreateSurvey.surveyCategory(self, driver)
        CreateSurvey.buttonCreateSurvey(self, driver)

        # Handle Popup
        CreateSurvey.handlePopup(self, driver)

        # Operations on created Survey.

        # Editing and saving survey title
        OperationsOnSurvey.editAndSaveSurveyTitle(self, driver)

        # Add Page Title
        #OperationsOnSurvey.addPageTitle(self, driver)

        # Add Questions
        AddQuestion.enterQuestion(self, driver)




startt = SeleniumWebdriverAutomationAssignment()