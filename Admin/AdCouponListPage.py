import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdCouponListPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def click_new(self):
        btn_new = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-success")
        self.driver.execute_script('arguments[0].click();', btn_new)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'page-container')))


    def __del__(self):
        print("CouponListPage 객체 소멸")