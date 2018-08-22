from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HelpScreen:

    def __init__(self, driver):
        self.driver = driver
        self.headphone_image = WebDriverWait(self.driver.instance, 5).until(
            EC.visibility_of_element_located((
                MobileBy.ID, "carousel_headphone_image")))

    def click_iagree(self):
        self.iagreebutton.click()

    def check_iagree(self):
        self.iagreecheckbox.click()