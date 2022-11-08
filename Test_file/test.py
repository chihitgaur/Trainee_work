import time
import pytest
import smoke

from selenium.webdriver.common.by import By

from locators.locatosweb import *
from ult.doingprocess import processing
from ult.switchingtabs import switching
import openpyxl
import util
from utilities.values import run
from utilities.viewfunc import click_view
path = "C:\\Users\\chihi\\Downloads\\list-cities-us-30j.xlsx"
r = util.get_row_count(path,'list-cities-us-30j')
class TestSearchdr():
    @pytest.mark.smoke
    @pytest.mark.usefixtures("initiate_driver")
    def test_end_to_end(self,initiate_driver):
        driver= initiate_driver
        driver.find_element(by=By.XPATH,value=guest_search).click()
        time.sleep(5)
        switching().switching_tabs(1)
        time.sleep(10)
        driver.find_element(by=By.XPATH,value=state_city).send_keys("Birmingham,AL")
        time.sleep(5)
        driver.find_element(by=By.XPATH,value=select_state).click()
        time.sleep(2)
        driver.find_element(by=By.XPATH,value=Continue_button).click()
        time.sleep(3)

        driver.find_element(by=By.XPATH, value=primary_care).click()
        time.sleep(3)
        driver.find_element(by=By.XPATH, value=family_practice).click()
        time.sleep(3)

        run().working()

        # driver.back()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=primary_care).click()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH,value=general_practice).click()
        #
        # run().working()
        #
        # driver.back()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=primary_care).click()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=internal_medicine).click()
        #
        # run().working()
        #
        # driver.back()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=primary_care).click()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=obstetrics_gynecology).click()
        #
        # run().working()
        #
        # driver.back()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=primary_care).click()
        # time.sleep(3)
        # driver.find_element(by=By.XPATH, value=pediatrics).click()
        #
        # run().working()
        time.sleep(5)
        driver.back()
        time.sleep(5)
        processing().bgprocessing()

