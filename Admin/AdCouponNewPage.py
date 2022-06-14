import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AdCouponNewPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.implicitly_wait(10)

    def add_allitemcoupon(self, i):
        from selenium.webdriver import ActionChains
        from selenium.webdriver import Keys
        from datetime import datetime
        from datetime import timedelta
        actions = ActionChains(self.driver)

        #쿠폰명
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(2) > div > div > input").send_keys("전체 상품 쿠폰 (자동화) (" + str(i) + ")")
        self.btn_submit = self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-success")
        actions.move_to_element(self.btn_submit).perform()

        #상세설명
        self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(5) > div > table > tbody > tr:nth-child(5) > td:nth-child(2) > div > div > textarea").send_keys("쿠폰 자동 생성")

        #다운로드 시작일 > 현재 시각
        now = datetime.now()
        start = now.strftime('%Y-%m-%d %H:%M')
        self.start_dl = self.driver.find_element(By.CSS_SELECTOR, "tr.download_date > td:nth-child(2) > div > div > input:nth-child(1)")
        actions.click(self.start_dl).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).send_keys(Keys.BACKSPACE).perform()
        time.sleep(1)
        self.start_dl.send_keys(start)
        time.sleep(1)
        self.start_dl.send_keys(Keys.TAB)
        #print(self.startdate.text)

        #다운로드 종료일 > 현재 시각 +7일
        end = (now + timedelta(days=7)).strftime('%Y-%m-%d %H:%M')
        self.end_dl = self.driver.find_element(By.CSS_SELECTOR, "tr.download_date > td:nth-child(2) > div > div > input:nth-child(3)")
        actions.click(self.end_dl).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).send_keys(
            Keys.BACKSPACE).perform()
        time.sleep(1)
        self.end_dl.send_keys(end)
        time.sleep(1)
        self.end_dl.send_keys(Keys.TAB)
        #print(self.end_dl.get_attribute("data-day"))

        #쿠폰 시작일 > 다운로드 시작일과 동일
        self.start_cp = self.driver.find_element(By.CSS_SELECTOR, "tr.expire_date > td:nth-child(2) > div:nth-child(2) > div > input:nth-child(1)")
        actions.click(self.start_cp).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).send_keys(
            Keys.BACKSPACE).perform()
        time.sleep(1)
        self.start_cp.send_keys(start)
        time.sleep(1)
        self.start_cp.send_keys(Keys.TAB)

        #쿠폰 종료일 > 다운로드 종료일과 동일
        self.end_cp = self.driver.find_element(By.CSS_SELECTOR, "tr.expire_date > td:nth-child(2) > div:nth-child(2) > div > input:nth-child(3)")
        actions.click(self.end_cp).key_down(Keys.COMMAND).send_keys("a").key_up(Keys.COMMAND).send_keys(
            Keys.BACKSPACE).perform()
        time.sleep(1)
        self.end_cp.send_keys(end)
        time.sleep(1)
        self.end_cp.send_keys(Keys.TAB)
        #print(self.end_dl.get_attribute("data-day"))

        #할인금액 3천원
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(12) > td:nth-child(2) > div > div > div > input").send_keys("3000")

        #최소주문금액 2만원
        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(15) > td:nth-child(2) > div.col-md-2.pd-l-0.pd-r-0 > input").send_keys("20000")

        self.btn_submit.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
        self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-sm.btn-success.width-120").click()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'page-container')))


    def __del__(self):
        print("CouponNewPage 객체 소멸")