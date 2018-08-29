import unittest
import pytest
from operations.CreateSurvey import CreateSurvey


@pytest.mark.usefixtures("getLogin")
class TestCreateSurveyDemo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, getLogin):
        # self.loginobj = LoginOperation(getDriver)
        # self.loginobj.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
        self.createSurvey = CreateSurvey(getLogin)
        yield self.createSurvey

    def test_t1create_survey(self):
        #createSurvey = CreateSurvey(getDriver)
        assert self.createSurvey.clickCreateSurvey() == True

    #sendSyrveyTitle

    def test_t2send_survey_title(self):
        #createSurvey = CreateSurvey(getDriver)
        assert self.createSurvey.sendSyrveyTitle() == True

    #surveyCategory

    def test_t3survey_category(self):
        #createSurvey = CreateSurvey(getDriver)
        assert self.createSurvey.surveyCategory()

    #buttonCreateSurvey
    def test_t4button_create_survey(self):
        #createSurvey = CreateSurvey(getDriver)
        assert self.createSurvey.buttonCreateSurvey()

    #handlePopup
    def test_t5handle_popup(self):
        #createSurvey = CreateSurvey()
        assert self.createSurvey.handlePopup()