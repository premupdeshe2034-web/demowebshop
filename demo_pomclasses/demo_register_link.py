import time
from selenium.webdriver.common.by import By


class register_link_of_demo:

    REGISTER="//a[@href='/register']"

    def __init__(self,driver):
        self.driver = driver


    def clickRegisterButton(self):
        self.driver.find_element(By.XPATH,self.REGISTER).click()
