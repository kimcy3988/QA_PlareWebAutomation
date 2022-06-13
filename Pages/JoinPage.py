from selenium import webdriver
from selenium.webdriver.common.by import By


class JoinPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.btn_login = self.driver.find_element(By.CSS_SELECTOR, "span.text.button3")
        self.driver.implicitly_wait(10)

    def click_login(self):
        self.btn_login.click()

    def __del__(self):
        print("JoinPage 객체 소멸")