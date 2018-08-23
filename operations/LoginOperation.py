"""
Login Operations
"""
from selenium.webdriver.common.by import By
from utilities.GetConfigurationDetails import GetConfigurationDetails
from base.basepage import BasePage
import pytest

class LoginOperation(BasePage):

    _nav_login_button = "//a[contains(text(), 'LOG IN')]"
    _username = "username"
    _password = "password"
    _login_button = "//button[contains(@type,'submit')]"
    _login_success = "userAcctTab_MainMenu"
    _login_fail = "//div[@id='sign-in']//li[contains(text(),'The username or password you entered is incorrect')]"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navToLogin(self):
        self.elementClick(self._nav_login_button, locatorType="xpath")
        return True


    def sendUsernameAndPass(self, email):
        self.sendKeys(email, locator=self._username)
        return True

    def sendPassword(self, password):
        self.sendKeys(password, locator=self._password)
        return True

    def clicklogIn(self):
        self.elementClick(self._login_button, locatorType="xpath")
        return True

    def login(self, email="", password=""):
        LoginOperation.navToLogin(self)
        self.clearField(locator=self._username)
        LoginOperation.sendUsernameAndPass(self,email)
        self.clearField(locator=self._password)
        LoginOperation.sendPassword(self, password)
        LoginOperation.clicklogIn(self)

    def verify_login_successful(self):
        self.waitForElement(locator=self._login_success, timeout=5, pollFrequency=1)
        result = self.isElementPresent(locator=self._login_success)
        return result

    def verify_login_failed(self):
        result = self.isElementPresent(locator=self._login_fail, locatorType="xpath")
        return result