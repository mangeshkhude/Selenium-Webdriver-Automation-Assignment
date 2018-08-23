
import pytest
from utilities.FromBrowser import FromBrowser
from operations.LoginOperation import LoginOperation
from operations.CreateSurvey import CreateSurvey
from operations.AddQuestions import AddQuestion
import utilities.CustomLogger as cl
import logging
from utilities.GetConfigurationDetails import GetConfigurationDetails as gcd

import time

@pytest.fixture(scope='module')
def getDriver():
    log = cl.customLogger(logging.DEBUG)
    log.info("*#" * 20)
    log.info("Get Driver")
    driver = FromBrowser.getFromChrome(FromBrowser)
    return driver

@pytest.mark.run(order=1)
def test_nav_to_login(getDriver):
    lo = LoginOperation(getDriver)
    assert lo.navToLogin() == True

@pytest.mark.run(order=2)
def test_invalidLogin(getDriver):
    print("test_invalidLogin started")
    lo = LoginOperation(getDriver)
    lo.login(gcd.getUserName(gcd), gcd.getInvalidPassword(gcd))
    result = lo.verify_login_failed()
    assert result == True

@pytest.mark.run(order=3)
def test_validLogin(getDriver):
    print("test_validLogin started")
    lo = LoginOperation(getDriver)
    lo.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
    result = lo.verify_login_successful()
    print("Result: " + str(result))
    assert result == True

@pytest.mark.run(order=4)
def test_create_survey(getDriver):
    createSurvey = CreateSurvey(getDriver)
    assert createSurvey.clickCreateSurvey() == True

#sendSyrveyTitle
@pytest.mark.run(order=5)
def test_send_survey_title(getDriver):
    createSurvey = CreateSurvey(getDriver)
    assert createSurvey.sendSyrveyTitle() == True

#surveyCategory
@pytest.mark.run(order=6)
def test_survey_category(getDriver):
    createSurvey = CreateSurvey(getDriver)
    assert createSurvey.surveyCategory()

#buttonCreateSurvey
@pytest.mark.run(order=7)
def test_button_create_survey(getDriver):
    createSurvey = CreateSurvey(getDriver)
    assert createSurvey.buttonCreateSurvey()

#handlePopup
@pytest.mark.run(order=8)
def test_handle_popup(getDriver):
    createSurvey = CreateSurvey(getDriver)
    assert createSurvey.handlePopup()

#enterQuestion
@pytest.mark.run(order=9)
def test_email_question(getDriver):
    addQuestion = AddQuestion(getDriver)
    assert addQuestion.emailQuestion()