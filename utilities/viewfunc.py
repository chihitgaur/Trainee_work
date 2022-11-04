from selenium.webdriver.common.by import By
from conftest import driver
from locators.locatosweb import *
import time
from openpyxl import Workbook

fix_data=[]
class click_view():
    def click_on_view_profile(self):
        data=[]
        name_variable=driver.find_elements(by=By.XPATH,value=name_credntial)[0]
        data.append(name_variable.text)
        contact= driver.find_elements(by=By.XPATH,value=contact_no)[0]
        data.append(contact.text)
        adress= driver.find_elements(by=By.XPATH,value=adress_detail)[0]
        data.append(adress.text)
        fix_data.append(data)
        wb = Workbook()
        ws = wb.active
        for rows in fix_data:
            ws.append(rows)
        wb.save("excelfile.xlsx")
        time.sleep(4)

        print(data)

