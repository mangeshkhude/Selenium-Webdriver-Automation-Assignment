"""
Class to get the fields mentioned in configuration file
"""

from utilities import IOConfiguration


class GetConfigurationDetails(object):

    def getURL(self):

        return IOConfiguration.IOConfiguration.URL

    def getUserName(self):

        return IOConfiguration.IOConfiguration.userName

    def getPassword(self):

        return IOConfiguration.IOConfiguration.password

    def getEmailQuestion(self):

        return IOConfiguration.IOConfiguration.emailQuestion
