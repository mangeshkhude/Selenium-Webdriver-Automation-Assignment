

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
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

    def getFirefoxDriver(self):
        driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver

    def getIEDriver(self):
        driverlocation = "D:\\Selenium IE Driver\\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = driverlocation
        driver = webdriver.Ie(driverlocation)
        return driver