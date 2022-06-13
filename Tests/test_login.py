import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Pages.MyPage import MyPage
from Pages.JoinPage import JoinPage
from Base.base import Base

#DEFINE
HOME_URL = 'https://web-sprint.plare.co.kr/'

class TestLogin(Base):
    def test_login_success(self):
        driver = self.driver
        driver.get(HOME_URL)
        home = HomePage(driver)

        try:
            assert home.txt_title == driver.title
        except Exception as e:
            raise
            print("Title is wrong", format(e))

        home.click_mypage()
        my = MyPage(driver)
        my.click_join()
        join = JoinPage(driver)
        join.click_login()
        login = LoginPage(driver)
        login.enter_account()
        login.click_login()
        WebDriverWait(self.driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='wrap']")))
        #time.sleep(20)

if __name__ == '__main__':
    unittest.main()