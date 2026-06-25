
from selenium.webdriver.common.by import By

class add_to_cart_page_of_demo:

    addtocartelement="//input[@class='button-2 product-box-add-to-cart-button']"

    def __init__(self,driver):
        self.driver=driver


    def click_add_to_cart_page_button(self):
        self.driver.find_element(By.XPATH,self.addtocartelement).click()




