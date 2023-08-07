import pytest

from conftest import *
from pages.LoginPage import LoginPage


@pytest.mark.usefixtures("browser_setup")
class Test_Login:

    valid_username = "Admin"
    valid_password = "admin123"

    # Opening a browser
    def setup_class(self):
        self.driver.get(BaseUrl)
        self.login_page = LoginPage(self.driver)

    # Logging in
    # Middle we have a test case

    def test_valid_login(self):
        print("Successful Employee Login to OrangeHRM portal")
        self.login_page.login(self.valid_username, self.valid_password)

    # Closing the browser
    # Lastly we have the tear down class
    def teardown_class(self):
        self.driver.quit()
