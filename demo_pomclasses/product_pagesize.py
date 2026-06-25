from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class product_page_size_of_demo:

      productsize="//select[@id='products-pagesize']"


      def __init__(self,driver):
          self.driver=driver


      def clickonproductsize(self):
         productsize_element= self.driver.find_element(By.XPATH,self.productsize)
         dropdown=Select(productsize_element)
         dropdown.select_by_index(1)



