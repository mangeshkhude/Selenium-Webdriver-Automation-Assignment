"""
Login Operations
"""
from selenium.webdriver.common.by import By
from utilities import GetConfigurationDetails

class LoginOperation(object):

    _nav_login_button = "//a[@class='log-in static-buttons']"
    _username = "username"
    _password = "password"
    _login_button = "//button[contains(@type,'submit')]"

    def navToLogin(self, driver):
        loginButton = driver.find_element(By.XPATH, LoginOperation()._nav_login_button)
        loginButton.click()


    def sendUsernameAndPass(self, driver):
        userNameElement = driver.find_element(By.ID, LoginOperation()._username)
        userNameElement.send_keys(GetConfigurationDetails.GetConfigurationDetails.getUserName(self))

    def sendPassword(self, driver):
        passwordElement = driver.find_element(By.ID, LoginOperation()._password)
        passwordElement.send_keys(GetConfigurationDetails.GetConfigurationDetails.getPassword(self))

    def clicklogIn(self, driver):
        loginButton = driver.find_element(By.XPATH, LoginOperation()._login_button)
        loginButton.click()
