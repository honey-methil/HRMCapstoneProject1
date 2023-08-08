from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class AddEmployeePage(Selenium_Helper):
    pim_ele = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
    add_ele = (By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a")

    firstname_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    lastname_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
    save_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]")

    def __init__(self, driver):
        super().__init__(driver)

    def addemployee(self, firstname, lastname):
        self.webelement_click(self.pim_ele)                     # Step 1
        self.webelement_click(self.add_ele)                     # Step 2

        self.webelement_enter(self.firstname_ele, firstname)    # Step 3
        self.webelement_enter(self.lastname_ele, lastname)      # Step 4
        self.webelement_click(self.save_ele)                    # Step 5

