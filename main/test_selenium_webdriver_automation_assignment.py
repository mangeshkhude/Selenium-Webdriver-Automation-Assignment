
from utilities.FromBrowser import FromBrowser
from operations.LoginOperation import LoginOperation
import pytest



class test_selenium_webdriver_automation_assignment(object):

    chromeDriver = ""

    def __init__(self):
        while True:
            #browser = str(input("Enter Browser name: "))
            #browser = browser.lower()
            browser = 'chrome'
            if browser == 'chrome':
                self.chromeDriver = FromBrowser.getFromChrome(self)
                break
            elif browser == 'firefox':
                FromBrowser.getFromFireFox(self)
                break
            elif browser == 'ie':
                FromBrowser.getFromIE(self)
                break
            else:
                print('Enter valid browser name')


    def test_login(self):
        assert LoginOperation.navToLogin(self.chromeDriver) == 1



#startt = test_selenium_webdriver_automation_assignment()