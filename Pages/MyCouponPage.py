import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class MyCouponPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get("https://web-sprint.plare.co.kr/mypage/coupon")
        self.driver.implicitly_wait(10)
        self.tab_usable = self.driver.find_element(By.CSS_SELECTOR, ".swiper-slide.swiper-slide-active.active")
        wrap = self.driver.find_element(By.CSS_SELECTOR, ".couponItemWrap.css-13zr15h")
        self.usablelist = wrap.find_elements(By.CSS_SELECTOR, ".couponItemWrap.itemWrap.css-1hxveoq")

    def get_usablelist(self):
        cnt = self.tab_usable.text.index('(')+1
        print(self.tab_usable.text[cnt])
        print(len(self.usablelist))
        try:
            if self.tab_usable.text[cnt] == len(self.usablelist):
                return self.usablelist
        except Exception as e:
            raise
            print("Usable Coupon List Error", format(e))

    def __del__(self):
        print("MyCouponPage 객체 소멸")
