import time
from selenium.webdriver.common.by import By

import util
from conftest import driver
from locators.locatosweb import *
from ult.switchingtabs import switching
from utilities.values import run
path = "C:\\Users\\chihi\\Downloads\\list-cities-us-30j.xlsx"
r = util.get_row_count(path,'list-cities-us-30j')


class processing():

    def bgprocessing(self):

        for i in range(3, r + 1):
            acc = driver.find_element(by=By.XPATH, value=Search_boxxx)
            acc.clear()
            city_name = util.read_data(path, 'list-cities-us-30j', i, 2)
            state_name = util.read_data(path, 'list-cities-us-30j', i, 4)
            Searching = city_name + "," + state_name



            acc.send_keys(Searching)
            time.sleep(5)
            driver.find_element(by=By.XPATH, value=taking_loc).click()
            time.sleep(3)

            driver.find_element(by=By.XPATH, value=primary_care).click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=family_practice).click()
            time.sleep(3)

            run().working()

            driver.back()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=primary_care).click()
            time.sleep(3)
            driver.find_element(by=By.XPATH,value=general_practice).click()

            run().working()

            driver.back()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=primary_care).click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=internal_medicine).click()

            run().working()

            driver.back()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=primary_care).click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=obstetrics_gynecology).click()

            run().working()

            driver.back()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=primary_care).click()
            time.sleep(3)
            driver.find_element(by=By.XPATH, value=pediatrics).click()

            run().working()
            driver.back()
