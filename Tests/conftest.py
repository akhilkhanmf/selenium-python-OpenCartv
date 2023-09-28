import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities import ReadConfigurations

@pytest.fixture()
def setup(request):
    browser= ReadConfigurations.read_configuration("Basic Info","browser")
    driver = None
    if browser.__eq__("chrome"):
        driver =webdriver.Chrome()
    elif browser.__eq__("edge"):
        driver =webdriver.Edge()
    elif browser.__eq__("firefox"):
        driver=webdriver.Firefox()
    else:
        print("Please pick any browser from the list")

    driver.maximize_window()
    app_url= ReadConfigurations.read_configuration("Basic Info","url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
