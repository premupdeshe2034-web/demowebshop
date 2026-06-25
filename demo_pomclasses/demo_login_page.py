
from selenium.webdriver.common.by import By

class loginpage_of_demowebshop:
    EMAIL="//input[@id='Email']"
    PASSWORD="//input[@id='Password']"
    LOGIN_BUTTON="//input[@value='Log in']"

    def __init__(self, driver):
        self.driver = driver



    def enteremail(self,email_value):
        self.driver.find_element(By.XPATH,self.EMAIL).send_keys(email_value)

    def enterpassword(self,password_value):
        self.driver.find_element(By.XPATH,self.PASSWORD).send_keys(password_value)

    def clickLoginButton(self):
        #self.driver.find_element(By.XPATH,self.LOGIN_BUTTON).click()
        print("Before finding login button")

        loginbtn = self.driver.find_element(By.XPATH, self.LOGIN_BUTTON)

        print("Login button found")

        loginbtn.click()

        print("Login button clicked")


