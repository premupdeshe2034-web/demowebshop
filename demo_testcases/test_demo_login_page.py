from demo_pomclasses.Notebooks_position_of_demo import notebook_postion
from demo_pomclasses.add_to_cart_page import add_to_cart_page_of_demo
from demo_pomclasses.demo_Register_page import Register_page_of_demo
from demo_pomclasses.demo_login_page import loginpage_of_demowebshop
import time

from demo_pomclasses.demo_register_link import register_link_of_demo
from demo_pomclasses.home_page_of_demoweb import home_page
from demo_pomclasses.product_page_of_demo import product_page
from demo_pomclasses.product_pagesize import product_page_size_of_demo
from demo_pomclasses.scroll_the_demo_page import scroll_down_to_end_ofthe_page
from demo_utilities.screenshots import BugScreenshot


def test_demowebshop(driver):               #register link open
    # regi=register_link_of_demo(driver)
    # regi.clickRegisterButton()
    # time.sleep(3)


    # regidetail=Register_page_of_demo(driver)
    # regidetail.clickon_Gender()
    # regidetail.enter_Firstname("prem")
    # regidetail.enter_Lastname("updeshe")
    # regidetail.enter_Email("prem.updeshe07@gmail.com")
    # regidetail.enter_Password("prem@0039")
    # regidetail.enter_confirm_Password("prem@0039")
    # time.sleep(3)
    # regidetail.clickon_Registerbutton()
    # time.sleep(3)



    login=loginpage_of_demowebshop(driver)           #login page
    login.enteremail("prem.updeshe2034@gmail.com")
    login.enterpassword("prem@0039")
    login.clickLoginButton()
    print("Step 1 Login Done")
    time.sleep(3)

    homeobj=home_page(driver)                          #home page
    homeobj.clickoncomputerlink()
    print("Step 2 Home Click Done")
    # time.sleep(3)

    prodobj=product_page(driver)                       #pdoduct page
    prodobj.clickoncomputerlink()
    print("Step 3 product Click Done")
    # time.sleep(3)

    notpos= notebook_postion(driver)                   #notebook price
    notpos.clickonnotebookpostion()
    print("Step 4 Notebook Click Done")
    # time.sleep(3)

    productsizeobj=product_page_size_of_demo(driver)
    productsizeobj.clickonproductsize()
    print("Step 5 Size Select Done")
    time.sleep(3)

    addtocartobj=add_to_cart_page_of_demo(driver)
    addtocartobj.click_add_to_cart_page_button()
    print("Step 6 Add To Cart Done")
    time.sleep(3)

    scrollobj=scroll_down_to_end_ofthe_page(driver)
    scrollobj.scroll_bar()
    print("Step 7 Scroll Done")
    time.sleep(3)

    scrennobj=BugScreenshot(driver)
    scrennobj.screenshotsave()
    print("Step 8 Screenshot save Done")
    print("231233231")

    







