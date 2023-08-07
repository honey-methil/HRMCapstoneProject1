from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Selenium_Helper:

    # Driver
    def __init__(self, driver):
        self.driver = driver

    # Method to enter in web element
    def webelement_enter(self, locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).send_keys(text)

    # Method to click on web element
    def webelement_click(self, locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator)).click()


