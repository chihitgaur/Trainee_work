import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()


@pytest.fixture()
def initiate_driver():
    driver.get("https://www.bcbsil.com/find-care/providers-in-your-network/find-a-doctor-or-hospital")
    driver.maximize_window()
    yield driver

    driver.close()
