from appium import webdriver


class Driver:

    def __init__(self):

        "Setup for the test"
        desired_caps = {'platformName': 'Android', 'platformVersion': '5.1', 'deviceName': 'TA98901EQB',
                        'appPackage': 'com.bose.monet', 'appActivity': '.activity.discovery.SplashSearchingActivity'}
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)