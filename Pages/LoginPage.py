import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.id = 'kimde12'
        self.pw = 'qwer1234!'
        self.driver.implicitly_wait(10)

    def enter_account(self):
        self.driver.find_element(By.NAME, "nickname").send_keys(self.id)
        self.driver.find_element(By.NAME, "password").send_keys(self.pw)

    def click_login(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.loginBtn.css-9n9rcn").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))

    def __del__(self):
        print("LoginPage 객체 소멸")