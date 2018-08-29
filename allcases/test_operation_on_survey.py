import unittest
import pytest

from operations.OperationsOnSurvey import OperationsOnSurvey

@pytest.mark.usefixtures("getSurvey")
class TestOperationSurveyDemo(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, getLogin):
        self.osos = OperationsOnSurvey(getLogin)
        yield self.osos

    def test_t1edit_survey_title(self):
        #createSurvey = CreateSurvey(getDriver)
        assert self.osos.editAndSaveSurveyTitle() == True