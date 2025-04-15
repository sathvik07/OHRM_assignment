from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.pim_menu = (By.XPATH, "//span[text()='PIM']")

    def go_to_pim(self):
        time.sleep(2)
        pim_element = self.driver.find_element(*self.pim_menu)
        ActionChains(self.driver).move_to_element(pim_element).click().perform()
