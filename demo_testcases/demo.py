def clickLoginButton(self):

    print("Trying to click login button")

    element = self.driver.find_element(
        By.XPATH,
        self.LOGIN_BUTTON
    )

    print("Element Found")

    element.click()

    print("Clicked Successfully")