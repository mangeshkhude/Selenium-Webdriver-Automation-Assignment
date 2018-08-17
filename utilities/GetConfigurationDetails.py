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

    def getQuestionBank(self):

        return IOConfiguration.questionBank

    def getThemes(self):

        return  IOConfiguration.themes

    def getGraphical(self):

        return IOConfiguration.graphical

    def getTemplate(self):

        return IOConfiguration.template

    def getCollectors(self):

        return IOConfiguration.collectors

    def getService(self):

        return  IOConfiguration.service

    def getSupport(self):

        return IOConfiguration.support

    def getResponsive(self):

        return  IOConfiguration.responsive

    def getVeryGood(self):

        return IOConfiguration.veryGood

    def getGood(self):

        return IOConfiguration.good

    def getAvarage(self):

        return IOConfiguration.avarage

    def getBelowAvarage(self):

        return IOConfiguration.belowAvarage

    def getFeatureList(self):

        return IOConfiguration.featureList