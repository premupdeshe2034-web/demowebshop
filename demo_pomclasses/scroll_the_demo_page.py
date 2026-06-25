from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




class scroll_down_to_end_ofthe_page:

    def __init__(self,driver):
        self.driver=driver

    def scroll_bar(self):

        act=ActionChains(self.driver)
        act.scroll_by_amount(0,300).perform()

        product_name = self.driver.find_element(
        By.XPATH,
        "(//a[@href='/141-inch-laptop'])[4]"
        ).text

        assert product_name == "14.1-inch Laptop"

        print("Product Found")

