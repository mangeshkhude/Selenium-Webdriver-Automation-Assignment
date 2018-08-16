"""
Class to get the fields mentioned in configuration file
"""

from utilities.IOConfiguration import IOConfiguration


class GetConfigurationDetails(object):

    def getURL(self):

        return IOConfiguration.URL

    def getUserName(self):

        return IOConfiguration.userName

    def getPassword(self):

        return IOConfiguration.password

    def getEmailQuestion(self):

        return IOConfiguration.emailQuestion

    def getUseSurveymonkey(self):

        return  IOConfiguration.useSurveyMonkey

    def getFromWhen(self):

        return  IOConfiguration.fromWhen

    def getRating(self):

        return IOConfiguration.ratings

    def getMeaningfulData(self):

        return IOConfiguration.meaningfulData

    def getFeatures(self):

        return IOConfiguration.features

    def getRateFeatures(self):

        return IOConfiguration.rateFeatures

    def getMostLikedFeatures(self):

        return IOConfiguration.mostLikedFeatures

    def getRecomendToFriends(self):

        return IOConfiguration.recomendToFriends

    def getCommentsFeedback(self):

        return IOConfiguration.commentsFeedback