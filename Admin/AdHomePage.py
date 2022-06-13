import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AdHomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_coupon(self):
        self.driver.find_element(By.XPATH, "//*[text()='기획전/쿠폰관리 ']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//*[@id='left-menu']/li[13]/ul/li[4]/a").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'page-container')))

    def __del__(self):
        print("AdHomePage 객체 소멸")
