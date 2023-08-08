import pytest

from conftest import *
from pages.EditEmployeePage import EditEmployeePage
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Edit_Employee:

    valid_username = "Admin"
    valid_password = "admin123"

    first_name = "Honey"
    last_name = "Methil"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)
        self.edit_emp_page = EditEmployeePage(self.driver)

    # Logging in
    # Middle we have a test case

    def test_edit_employee(self):
        print("Employee Edit OrangeHRM portal")
        self.login_page.login(self.valid_username, self.valid_password)
        self.edit_emp_page.editemployee(self.first_name, self.last_name)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
