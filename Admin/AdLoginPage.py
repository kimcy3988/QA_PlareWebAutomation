import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class AdLoginPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://admin-sprint.plare.co.kr/login")
        self.driver.implicitly_wait(10)
        self.id = 'kimde6990@brandi.co.kr'
        self.pw = '!Mint07180525'

    def enter_adaccount(self):
        self.driver.find_element(By.ID, "username").send_keys(self.id)
        self.driver.find_element(By.NAME, "password").send_keys(self.pw)
        self.btn_login = self.driver.find_element(By.ID, "btn_login")
        self.driver.execute_script('arguments[0].click();', self.btn_login)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))

    def __del__(self):
        print("AdLoginPage 객체 소멸")