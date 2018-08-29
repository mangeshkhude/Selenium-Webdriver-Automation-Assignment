import unittest
import pytest
from operations.LoginOperation import LoginOperation
from utilities.GetConfigurationDetails import GetConfigurationDetails as gcd
import utilities.CustomLogger as cl
import logging
pytestmark = pytest.mark.random_order(disabled=True)

@pytest.mark.usefixtures("getDriver")
class TestLoginn(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, getDriver):
        log = cl.customLogger(logging.DEBUG)
        log.info("=" * 20)
        log.info("Login Operation")
        self.lo = LoginOperation(getDriver)

    @pytest.mark.run(order=1)
    def test_nav_to_login(self):
        #lo = LoginOperation(getDriver)
        assert self.lo.navToLogin() == True

    @pytest.mark.run(order=2)
    def test_invalidLogin(self):
        print("test_invalidLogin started")
        #lo = LoginOperation(getDriver)
        self.lo.login(gcd.getUserName(gcd), gcd.getInvalidPassword(gcd))
        result = self.lo.verify_login_failed()
        assert result == True

    @pytest.mark.run(order=3)
    def test_validLogin(self):
        print("test_validLogin started")
        #lo = LoginOperation(getDriver)
        self.lo.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
        result = self.lo.verify_login_successful()
        print("Result: " + str(result))
        assert result == True

