
import pytest
from utilities.FromBrowser import FromBrowser
from operations.LoginOperation import LoginOperation
from operations.CreateSurvey import CreateSurvey
import time
@pytest.fixture(scope='module')
def getDriver():
    driver = FromBrowser.getFromChrome(FromBrowser)
    return driver

@pytest.mark.run(order=1)
def test_nav_to_login(getDriver):
    assert LoginOperation.navToLogin(getDriver) == True

@pytest.mark.run(order=2)
def test_send_username(getDriver):
    assert LoginOperation.sendUsernameAndPass(getDriver) == True

@pytest.mark.run(order=3)
def test_send_password(getDriver):
    assert LoginOperation.sendPassword(getDriver) == True

@pytest.mark.run(order=4)
def test_click_login(getDriver):
    assert LoginOperation.clicklogIn(getDriver) == True

@pytest.mark.run(order=5)
def test_create_survey(getDriver):
    assert CreateSurvey.clickCreateSurvey(getDriver) == True

#sendSyrveyTitle
@pytest.mark.run(order=6)
def test_send_survey_title(getDriver):
    assert CreateSurvey.sendSyrveyTitle(getDriver) == True

#surveyCategory
@pytest.mark.run(order=7)
def test_survey_category(getDriver):
    assert CreateSurvey.surveyCategory(getDriver)

#buttonCreateSurvey
@pytest.mark.run(order=8)
def test_button_create_survey(getDriver):
    assert CreateSurvey.buttonCreateSurvey(getDriver)

#handlePopup
@pytest.mark.run(order=9)
def test_handle_popup(getDriver):
    assert CreateSurvey.handlePopup(getDriver)