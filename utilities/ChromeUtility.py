

"""
Chrome Driver
"""
from selenium import webdriver
import os

class ChromeUtility(object):

    def getChromeDriver(self):
        driverLocation = 'D:\Selenium Chrome Driver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.implicitly_wait(0.5)
        driver.maximize_window()
        return driver