import pytest

from conftest import *
from pages.AddEmployeePage import AddEmployeePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Add_Employee:

    valid_username = "Admin"
    valid_password = "admin123"

    first_name = "John"
    last_name = "Doe"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)
        self.add_emp_page = AddEmployeePage(self.driver)

    # Logging in
    # Middle we have a test case

    def test_add_employee(self):
        print("Employee Add OrangeHRM portal")
        self.login_page.login(self.valid_username, self.valid_password)
        self.add_emp_page.addemployee(self.first_name, self.last_name)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
