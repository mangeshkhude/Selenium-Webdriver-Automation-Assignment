
from utilities.FromBrowser import FromBrowser

class SeleniumWebdriverAutomationAssignment(object):

    def __init__(self):
        while True:
            browser = str(input("Enter Browser name: "))
            browser = browser.lower()
            if browser == 'chrome':
                FromBrowser.getFromChrome(self)
                break
            elif browser == 'firefox':
                FromBrowser.getFromFireFox(self)
                break
            elif browser == 'ie':
                FromBrowser.getFromIE(self)
                break
            else:
                print('Enter valid browser name')

startt = SeleniumWebdriverAutomationAssignment()