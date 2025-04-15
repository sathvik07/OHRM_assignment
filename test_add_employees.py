from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage
from pages.logout_page import LogoutPage

# Initialize the WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Going to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

# Login process here
login = LoginPage(driver)
login.login("Admin", "admin123")
time.sleep(3)

# Navigating to PIM
dashboard = DashboardPage(driver)
dashboard.go_to_pim()
time.sleep(2)

# Adding Employees in PIM
pim = PimPage(driver)
employees = [("some", "oneelse"), ("John", "wick"), ("kieron", "smith")]
for fname, lname in employees:
    pim.add_employee(fname, lname)

# Verifying Employees
pim.open_employee_list()
for fname, lname in employees:
    pim.verify_employee_in_list(f"{fname} {lname}")

# Logout
logout = LogoutPage(driver)
logout.logout()

# Close the browser
driver.quit()
