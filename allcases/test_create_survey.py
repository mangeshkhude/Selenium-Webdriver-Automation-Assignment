import unittest
import pytest
from operations.CreateSurvey import CreateSurvey

@pytest.mark.usefixtures("getDriver")
class TestCreateSurveyDemo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, getDriver):
        self.createSurvey = CreateSurvey(getDriver)

    @pytest.mark.run(order=1)
    def test_create_survey(self):
        assert self.createSurvey.clickCreateSurvey() == True

    #sendSyrveyTitle
    @pytest.mark.run(order=2)
    def test_send_survey_title(self):
        assert self.createSurvey.sendSyrveyTitle() == True

    #surveyCategory
    @pytest.mark.run(order=3)
    def test_survey_category(self):
        assert self.createSurvey.surveyCategory()

    #buttonCreateSurvey
    @pytest.mark.run(order=4)
    def test_button_create_survey(self):
        assert self.createSurvey.buttonCreateSurvey()

    #handlePopup
    @pytest.mark.run(order=5)
    def test_handle_popup(self):
        assert self.createSurvey.handlePopup()