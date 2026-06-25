from selenium import webdriver

from selenium.webdriver.common.by import By

class home_page:

    COMPUTER='(//a[@href="/computers"])[3]'

    def __init__(self,driver):
        self.driver = driver

    def clickoncomputerlink(self):
        self.driver.find_element(By.XPATH,self.COMPUTER).click()


