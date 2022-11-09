import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators.locatosweb import view_profile, back_button, xbutton, tab
from utilities.viewfunc import click_view
class run():
    def working(self):
        for i in range(0, 9):
            try:

                elem = driver.find_element(by=By.XPATH, value=tab)
                if elem.is_displayed():

                    driver.find_element(by=By.XPATH,value=xbutton).click()

            except NoSuchElementException:

                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, view_profile)))
                driver.find_elements(by=By.XPATH, value=view_profile)[i].click()
                time.sleep(3)

                click_view().click_on_view_profile()
                WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, back_button)))
                driver.find_element(by=By.XPATH, value=back_button).click()
                time.sleep(3)

