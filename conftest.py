import time
import pytest
from selenium import webdriver

from demo_utilities.readproperties_of_demo import  get_demo_webshop


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(get_demo_webshop("demo_webshop","url"))

    driver.maximize_window()
    driver.set_page_load_timeout(50)
    driver.implicitly_wait(10)

    yield driver
    driver.quit()
