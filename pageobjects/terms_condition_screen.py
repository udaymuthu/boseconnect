from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TermsConditionScreen:

    def __init__(self, driver):
        self.driver = driver

        self.title = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "privacy_takeover_title")))

        self.privacymessage = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "privacy_takeover_primary_message")))

        self.iagreetext = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "links_message")))

        self.iagreecheckbox = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "privacy_policy_agreement_checkbox")))

        self.iagreebutton = self.driver.instance.find_element_by_id("button")

    def click_iagree(self):
        self.iagreebutton.click()

    def check_iagree(self):
        self.iagreecheckbox.click()
