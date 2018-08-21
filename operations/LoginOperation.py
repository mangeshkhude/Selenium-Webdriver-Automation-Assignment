"""
Login Operations
"""
from selenium.webdriver.common.by import By
from utilities import GetConfigurationDetails
import pytest

class LoginOperation(object):

    _nav_login_button = "//a[contains(text(), 'LOG IN')]"
    _username = "username"
    _password = "password"
    _login_button = "//button[contains(@type,'submit')]"

    def navToLogin(driver):
        loginButton = driver.find_element(By.XPATH, LoginOperation()._nav_login_button)
        loginButton.click()
        return True


    def sendUsernameAndPass(driver):
        userNameElement = driver.find_element(By.ID, LoginOperation()._username)
        userNameElement.send_keys(GetConfigurationDetails.GetConfigurationDetails.getUserName(GetConfigurationDetails))
        return True

    def sendPassword(driver):
        passwordElement = driver.find_element(By.ID, LoginOperation()._password)
        passwordElement.send_keys(GetConfigurationDetails.GetConfigurationDetails.getPassword(GetConfigurationDetails))
        return True

    def clicklogIn(driver):
        loginButton = driver.find_element(By.XPATH, LoginOperation()._login_button)
        loginButton.click()
        return True