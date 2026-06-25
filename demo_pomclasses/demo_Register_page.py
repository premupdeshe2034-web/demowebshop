from selenium.webdriver.common.by import By

class Register_page_of_demo:
    Gender="//input[@id='gender-male']"
    Firstname="//input[@id='FirstName']"
    LASTNAME="//input[@id='LastName']"
    Email="//input[@id='Email']"
    Password="//input[@id='Password']"
    confirm_Password="//input[@id='ConfirmPassword']"
    Registerbutton="//input[@id='register-button']"

    continuebutton="//input[@class='button-1 register-continue-button']"


    def __init__(self,driver):
        self.driver=driver

    def clickon_Gender(self):
        self.driver.find_element(By.XPATH,self.Gender).click()

    def enter_Firstname(self,firstname_value):
        self.driver.find_element(By.XPATH,self.Firstname).send_keys(firstname_value)

    def enter_Lastname(self,lastname_value):
        self.driver.find_element(By.XPATH,self.LASTNAME).send_keys(lastname_value)

    def enter_Email(self,email_value):
        self.driver.find_element(By.XPATH,self.Email).send_keys(email_value)

    def enter_Password(self,password_value):
        self.driver.find_element(By.XPATH,self.Password).send_keys(password_value)

    def enter_confirm_Password(self,confirm_password_value):
        self.driver.find_element(By.XPATH,self.confirm_Password).send_keys(confirm_password_value)

    def clickon_Registerbutton(self):
        self.driver.find_element(By.XPATH,self.Registerbutton).click()

    # def click_continuebutton(self):
    #     self.driver.find_element(By.XPATH,self.continuebutton).click()