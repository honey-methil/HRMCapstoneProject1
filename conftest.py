import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# Base configuration
BaseUrl = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
Username = "Admin"
Password = "admin123"


# Driver setup
@pytest.fixture(scope="class", autouse=True)
def browser_setup(request):
    service = Service(executable_path=r'D:/GUVI/chromedriver_win32/chromedriver.exe')
    options = webdriver.ChromeOptions()
    # chrome_options = Options()
    # request.cls.driver = webdriver.Chrome("D:/GUVI/chromedriver_win32/chromedriver.exe", options=chrome_options)
    request.cls.driver = webdriver.Chrome(service=service, options=options)
    # print('Honey')
