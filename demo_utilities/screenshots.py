from selenium import webdriver

class BugScreenshot:

    def __init__(self,driver):
        self.driver=driver

    def screenshotsave(self):
        self.driver.save_screenshot("D:\\srenshotofdemo.png")