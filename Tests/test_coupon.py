import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Admin.AdCouponListPage import AdCouponListPage
from Admin.AdHomePage import AdHomePage
from Admin.AdCouponNewPage import AdCouponNewPage
from Admin.AdLoginPage import AdLoginPage
from Pages.MyCouponPage import MyCouponPage
from Pages.CouponPage import CouponPage
from Pages.ProductDetailPage import ProductDetailPage
from Pages.RankingPage import RankingPage
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.MyPage import MyPage
from Pages.JoinPage import JoinPage
from Base.base import Base

#DEFINE
HOME_URL = 'https://web-sprint.plare.co.kr/'

class TestCoupon(Base):
    def test_detail_coupon(self):
        driver = self.driver
        driver.get(HOME_URL)
        home = HomePage(driver)

        # 로그인
        home.click_mypage()
        my = MyPage(driver)
        driver.implicitly_wait(10)
        my.click_join()
        join = JoinPage(driver)
        driver.implicitly_wait(10)
        join.click_login()
        join.__del__()
        login = LoginPage(driver)
        driver.implicitly_wait(10)
        login.enter_account()
        login.click_login()
        login.__del__()
        my.click_home()
        WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))
        home.click_ranking()

        # 랭킹 1위 상품 상세
        rank = RankingPage(driver)

        try:
            print(rank.tab_ranking.get_attribute('href'))
            assert "/ranking/all" in rank.tab_ranking.get_attribute('href')
        except Exception as e:
            raise
            print("Tab_Ranking Is Disabled", format(e))

        # 임시 1위 상품 선택
        rank.click_item(rank.first)
        WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "productDetail")))
        rank.__del__()
        detail = ProductDetailPage(driver)
        driver.implicitly_wait(10)
        detail.click_coupon()
        #detail.buy_item(detail.btn_buy)
        coupon = CouponPage(driver)
        download_coupon = coupon.download_allcoupon()
        #{발급대상}“쿠폰” / {정액/정율}{“원” or “%”} / {쿠폰명} / 최소사용가능금액 true > {금액}“원 이상 상품 구매 시 적용” / false > “금액 제한 없음” / {다운로드 기간}“까지” /
        mycoupon = MyCouponPage(driver)
        usable_coupon = mycoupon.get_usablelist()

        self.driver.execute_script("window.open('about:blank', '_blank');")
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[1])
        ad_login = AdLoginPage(driver)
        ad_login.enter_adaccount()
        ad_home = AdHomePage(driver)
        ad_home.click_coupon()
        #ad_newcp = AdCouponNewPage(driver)
        time.sleep(15)

if __name__ == '__main__':
    unittest.main()