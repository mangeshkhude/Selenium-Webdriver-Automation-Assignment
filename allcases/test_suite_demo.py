# Combining Test Suites - unittest

#  ----------------- Unit test framework
import unittest


#  ----------------  Individual test suites
from allcases.test_login import TestLoginn
from allcases.test_create_survey import TestCreateSurveyDemo

# -----------------  Load all the test cases
suiteList = []
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestLoginn))
suiteList.append(unittest.TestLoader().loadTestsFromTestCase(TestCreateSurveyDemo))
print(suiteList)

# ----------------   Join them together ane run them
comboSuite = unittest.TestSuite(suiteList)
unittest.TextTestRunner(verbosity=2).run(comboSuite)