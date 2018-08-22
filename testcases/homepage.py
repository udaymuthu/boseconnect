import unittest
from appium.webdriver.common.mobileby import MobileBy
from webdriver.webdriver import Driver


class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = Driver()

    def test_home_screen(self):
        self.driver.instance.find_element(MobileBy.ID, "privacy_takeover_title").click()

    def tearDown(self):
        "Tear down the test"
        self.driver.instance.quit()

    if __name__ == '__main__':
        suite = unittest.TestLoader().loadTestsFromTestCase(TestHomePage)
        unittest.TextTestRunner(verbosity=2).run(suite)
