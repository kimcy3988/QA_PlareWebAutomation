import time
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class CouponPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        wrap = self.driver.find_element(By.CSS_SELECTOR, ".css-fyqlz2")
        self.list_coupon = wrap.find_elements(By.CSS_SELECTOR, ".couponItemWrap.ItemWrap.css-1hxveoq")

    def download_allcoupon(self):
        from selenium.webdriver import ActionChains
        #cnt = len(self.list_coupon)//3
        list_cp = self.list_coupon
        print(len(list_cp))
        for i in range(len(list_cp)):
            btn_download = list_cp[i].find_element(By.CSS_SELECTOR, ".downLoad.css-178ppky")
            print((i+1), "번째 쿠폰 확인")
            """
            btn_download.click()
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(By.XPATH, "//*[text()='할인 쿠폰을 받았어요.']"))
            try:
                #download end btn
                self.list_coupon[i].find_element(By.CSS_SELECTOR, ".downLoad.css-ysn4df")
            except NoSuchElementException as ne:
                print("쿠폰 다운로드 실패", format(ne))
            """

            #3배수 스크롤 다운
            if (i+1)%3 == 0:
                actions = ActionChains(self.driver)
                if (i+3) >= len(list_cp):
                    actions.move_to_element(list_cp[i]).perform()
                else:
                    actions.move_to_element(list_cp[i + 3]).perform()
                print((i+1), "번째에서 스크롤 실행")

        return list_cp


    def __del__(self):
        print("CouponPage 객체 소멸")



