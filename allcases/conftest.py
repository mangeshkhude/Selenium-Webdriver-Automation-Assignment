
import pytest
from utilities.FromBrowser import FromBrowser
import utilities.CustomLogger as cl
import logging
from operations.LoginOperation import LoginOperation
from operations.CreateSurvey import CreateSurvey
from utilities.GetConfigurationDetails import GetConfigurationDetails as gcd

@pytest.yield_fixture(scope="class")
def getDriver():
    log = cl.customLogger(logging.DEBUG)
    log.info("=" * 20)
    log.info("Get Driver")
    driver = FromBrowser.getFromChrome(FromBrowser)
    yield driver
    driver.close()


@pytest.yield_fixture(scope="class")
def getLogin(getDriver):
    log = cl.customLogger(logging.DEBUG)
    log.info("=" * 20)
    log.info("Get Login")
    loginobj = LoginOperation(getDriver)
    loginobj.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
    yield getDriver

@pytest.yield_fixture(scope="class")
def getSurvey(getDriver):
    log = cl.customLogger(logging.DEBUG)
    log.info("=" * 20)
    log.info("Get Survey")
    loginobj = LoginOperation(getDriver)
    loginobj.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
    cs = CreateSurvey(getDriver)
    cs.createSurvey()
    yield getDriver

