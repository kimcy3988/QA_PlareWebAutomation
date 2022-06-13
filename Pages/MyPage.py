import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.btn_join = self.driver.find_element(By.XPATH, "//*[text()='로그인 / 회원가입 하기']")
        self.driver.implicitly_wait(10)

    def click_join(self):
        self.btn_join.click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))


    def click_home(self):
        self.tab_home = self.driver.find_element(By.XPATH, "//*[text()='홈']")
        self.tab_home.click()
        time.sleep(5)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))

    def __del__(self):
        print("MyPage 소멸")
