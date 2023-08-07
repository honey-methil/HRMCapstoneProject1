import pytest

from conftest import *
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:

    invalid_username = "Admin"
    invalid_password = "Invalid Password"

    # Opening a browser - changed comment
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    # Logging in
    # Middle we have a test case
    def test_invalid_login(self):
        print("Invalid Employee Login to OrangeHRM portal")
        self.login_page.login(self.invalid_username, self.invalid_password)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
