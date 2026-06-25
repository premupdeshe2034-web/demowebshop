
from selenium.webdriver.common.by import By

class product_page:


    notebook="//img[@alt='Picture for category Notebooks']"


    def __init__(self,driver):
        self.driver=driver


    def clickoncomputerlink(self):
        self.driver.find_element(By.XPATH,self.notebook).click()


