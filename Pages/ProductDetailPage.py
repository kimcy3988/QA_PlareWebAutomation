import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class ProductDetailPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.btn_buy = self.driver.find_element(By.XPATH, "//*[text()='구매하기']")
        self.btn_datail = self.driver.find_element(By.XPATH, "//*[text()='상품정보']")
        self.driver.implicitly_wait(10)

    def buy_item(self, item):
        self.item = item
        self.item.click()

    def click_coupon(self):
        from selenium.webdriver import ActionChains
        try:
            self.btn_coupon = self.driver.find_element(By.XPATH, "//*[text()='할인 쿠폰 받기']")
            actions = ActionChains(self.driver)
            actions.move_to_element(self.btn_datail).perform()
            time.sleep(2)
            self.btn_coupon.click()
            WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))
        except NoSuchElementException as ne:
            print("쿠폰 다운로드 완료", format(ne))
            #No Such or 클릭 불가로 쿠폰 다운로드 완료 판단 가능
        except TimeoutException as te:
            print("Time Out", format(te))

    def __del__(self):
        print("ProductDetailPage 객체 소멸")


