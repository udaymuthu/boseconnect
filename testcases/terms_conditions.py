import unittest
from appium.webdriver.common.mobileby import MobileBy
from pageobjects.terms_condition_screen import TermsConditionScreen
from webdriver.webdriver import Driver
from values import strings


class TestTermsCondition(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()
        self.driver.instance.reset()

    def test_terms_condition(self):
        termscondition = TermsConditionScreen(self.driver)
        self.assertEqual(strings.terms_condition_title, termscondition.title.get_attribute('text'))
        self.assertEqual(strings.terms_condition_iagree_text, termscondition.iagreetext.get_attribute('text'))
        self.assertEqual("false", termscondition.iagreebutton.get_attribute('enabled'))
        termscondition.check_iagree()
        self.assertEqual("true", termscondition.iagreebutton.get_attribute('enabled'))
        termscondition.click_iagree()

    def tearDown(self):
        "Tear down the test"
        self.driver.instance.quit()

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestTermsCondition)
        unittest.TextTestRunner(verbosity=2).run(suite)