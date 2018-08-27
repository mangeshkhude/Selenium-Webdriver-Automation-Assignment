#
# import pytest
# from utilities.FromBrowser import FromBrowser
# from operations.LoginOperation import LoginOperation
# from operations.CreateSurvey import CreateSurvey
# from operations.AddQuestions import AddQuestion
# import utilities.CustomLogger as cl
# import logging
# from utilities.GetConfigurationDetails import GetConfigurationDetails as gcd
#
#
# @pytest.yield_fixture(scope="class")
# def getDriver():
#     log = cl.customLogger(logging.DEBUG)
#     log.info("*#" * 20)
#     log.info("Get Driver")
#     driver = FromBrowser.getFromChrome(FromBrowser)
#     yield driver
#
#
#
# @pytest.mark.run(order=1)
# def test_nav_to_login(getDriver):
#     lo = LoginOperation(getDriver)
#     assert lo.navToLogin() == True
#
# @pytest.mark.run(order=2)
# def test_invalidLogin(getDriver):
#     print("test_invalidLogin started")
#     lo = LoginOperation(getDriver)
#     lo.login(gcd.getUserName(gcd), gcd.getInvalidPassword(gcd))
#     result = lo.verify_login_failed()
#     assert result == True
#
# @pytest.mark.run(order=3)
# def test_validLogin(getDriver):
#     print("test_validLogin started")
#     lo = LoginOperation(getDriver)
#     lo.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
#     result = lo.verify_login_successful()
#     print("Result: " + str(result))
#     assert result == True
#
# @pytest.mark.run(order=4)
# def test_create_survey(getDriver):
#     createSurvey = CreateSurvey(getDriver)
#     assert createSurvey.clickCreateSurvey() == True
#
# #sendSyrveyTitle
# @pytest.mark.run(order=5)
# def test_send_survey_title(getDriver):
#     createSurvey = CreateSurvey(getDriver)
#     assert createSurvey.sendSyrveyTitle() == True
#
# #surveyCategory
# @pytest.mark.run(order=6)
# def test_survey_category(getDriver):
#     createSurvey = CreateSurvey(getDriver)
#     assert createSurvey.surveyCategory()
#
# #buttonCreateSurvey
# @pytest.mark.run(order=7)
# def test_button_create_survey(getDriver):
#     createSurvey = CreateSurvey(getDriver)
#     assert createSurvey.buttonCreateSurvey()
#
# #handlePopup
# @pytest.mark.run(order=8)
# def test_handle_popup(getDriver):
#     createSurvey = CreateSurvey(getDriver)
#     assert createSurvey.handlePopup()
#
# #enterQuestion
# @pytest.mark.run(order=9)
# def test_email_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.emailQuestion()
#
# @pytest.mark.run(order=10)
# def test_rating_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.ratingQuestion()
#
# @pytest.mark.run(order=11)
# def test_date_using_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.dateOfUsing()
#
# @pytest.mark.run(order=12)
# def test_meaningful_data_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.meaningfulData()
#
# @pytest.mark.run(order=13)
# def test_friend_recomanded_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.recomandFriendsQuestion()
#
# @pytest.mark.run(order=14)
# def test_use_survey_monkey_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.useSurveyMonkeyQuestion()
#
# @pytest.mark.run(order=15)
# def test_comments_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.commentsFeedbackQuestion()
#
# @pytest.mark.run(order=16)
# def test_featured_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.featureQuestion()
#
# @pytest.mark.run(order=17)
# def test_matrix_rating_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.matrixRatingQuestion()
#
# @pytest.mark.run(order=18)
# def test_rate_featured_question(getDriver):
#     addQuestion = AddQuestion(getDriver)
#     assert addQuestion.ratefeatureQuestion()
#
