from selenium.webdriver.common.by import By
import time

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.user_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.LINK_TEXT, "Logout")

    def logout(self):
        time.sleep(2)
        self.driver.find_element(*self.user_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_button).click()
