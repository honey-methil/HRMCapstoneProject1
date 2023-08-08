from selenium.webdriver.common.by import By
from config.selenium_helper import Selenium_Helper


class EditEmployeePage(Selenium_Helper):

    pim_ele = (By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span")
    edit_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[2]/div/div[9]/div/button[2]")

    firstname_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input")
    lastname_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input")
    save_ele = (By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button")

    def __init__(self, driver):
        super().__init__(driver)

    def editemployee(self, firstname, lastname):
        self.webelement_click(self.pim_ele)                     # Step 1
        self.webelement_click(self.edit_ele)                    # Step 2

        self.webelement_enter(self.firstname_ele, firstname)    # Step 3
        self.webelement_enter(self.lastname_ele, lastname)      # Step 4
        self.webelement_click(self.save_ele)                    # Step 5


