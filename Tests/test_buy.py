import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.RankingPage import RankingPage
from Pages.ProductDetailPage import ProductDetailPage
from Base.base import Base

#DEFINE
HOME_URL = 'https://web-staging.plare.co.kr/ranking/all'

class TestBuy(Base):
    def test_buy_naverpay(self):
        driver = self.driver
        driver.get(HOME_URL)
        driver.implicitly_wait(30)
        rank = RankingPage(driver)

        try:
            print(rank.tab_ranking.get_attribute('class'))
            assert " active" in rank.tab_ranking.get_attribute('class')
        except Exception as e:
            raise
            print("Tab_Ranking Is Disabled", format(e))

        #임시 1위 상품 선택
        rank.click_item(rank.first)
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "productDetail")))

        detail = ProductDetailPage(driver)
        detail.buy_item(detail.btn_buy)
        time.sleep(10)

if __name__ == '__main__':
    unittest.main()