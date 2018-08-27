
import pytest
from utilities.FromBrowser import FromBrowser
import utilities.CustomLogger as cl
import logging
from operations.LoginOperation import LoginOperation
from utilities.GetConfigurationDetails import GetConfigurationDetails as gcd

@pytest.yield_fixture(scope="module")
def getDriver():
    log = cl.customLogger(logging.DEBUG)
    log.info("*#" * 20)
    log.info("Get Driver")
    driver = FromBrowser.getFromChrome(FromBrowser)
    # login = LoginOperation(driver)
    # login.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
    return driver


# def getSurvey(getDriver):
#
#     login = LoginOperation(getDriver)
#     login.login(gcd.getUserName(gcd), gcd.getPassword(gcd))
#     return getDriver



