from selenium.webdriver.common.by import By
import time


class PimPage:
    def __init__(self, driver):
        self.driver = driver
        self.add_employee_btn = (By.LINK_TEXT, "Add Employee")
        self.employee_list_btn = (By.LINK_TEXT, "Employee List")
        self.first_name_input = (By.NAME, "firstName")
        self.last_name_input = (By.NAME, "lastName")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.name_search_input = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.search_button = (By.XPATH, "//button[@type='submit']")


    def add_employee(self, first, last):
        self.driver.find_element(*self.add_employee_btn).click()
        time.sleep(2)
        self.driver.find_element(*self.first_name_input).send_keys(first)
        self.driver.find_element(*self.last_name_input).send_keys(last)
        self.driver.find_element(*self.save_button).click()
        time.sleep(2)

    def open_employee_list(self):
        self.driver.find_element(*self.employee_list_btn).click()
        time.sleep(2)

    def verify_employee_in_list(self, name):
        self.driver.find_element(*self.name_search_input).clear()
        self.driver.find_element(*self.name_search_input).send_keys(name)
        self.driver.find_element(*self.search_button).click()
        if name.lower() in self.driver.page_source.lower():
            print(f"Name Verified: {name}")
        else:
            print(f"Not Found: {name}")