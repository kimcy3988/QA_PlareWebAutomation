import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdCouponNewPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def enter_values(self):
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2) > div > div > input").send_keys("전체 상품 쿠폰 (자동화)")

    def __del__(self):
        print("CouponNewPage 객체 소멸")