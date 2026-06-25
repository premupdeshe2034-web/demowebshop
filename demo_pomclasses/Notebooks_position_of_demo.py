from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
class notebook_postion:

    notebook="//select[@id='products-orderby']"

    def __init__(self,driver):
        self.driver=driver

    def clickonnotebookpostion(self):

        #1st aproach
        # dropdown = Select(self.driver.find_element(By.XPATH, self.notebook) )
        # dropdown.select_by_visible_text("Price: Low to High")
        # dropdown.select_by_index(3)

        notebook_element=self.driver.find_element(By.XPATH,self.notebook)
        dropdown=Select(notebook_element)
        dropdown.select_by_index(3)


