import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Admin.AdCouponListPage import AdCouponListPage
from Admin.AdHomePage import AdHomePage
from Admin.AdCouponNewPage import AdCouponNewPage
from Admin.AdLoginPage import AdLoginPage
from Base.base import Base

class TestAdmin(Base):
    def test_admin_coupon(self):
        driver = self.driver
        ad_login = AdLoginPage(driver)
        ad_login.enter_adaccount()
        ad_home = AdHomePage(driver)
        ad_home.click_coupon()
        ad_cplist = AdCouponListPage(driver)
        ad_cpnew = AdCouponNewPage(driver)
        for i in range(1, 3):
            ad_cplist.click_new()
            time.sleep(2)
            ad_cpnew.add_allitemcoupon(i)
            time.sleep(2)
        time.sleep(15)
