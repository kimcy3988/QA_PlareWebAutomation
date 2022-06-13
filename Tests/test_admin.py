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
        ad_cplist.click_new()
        ad_cpnew = AdCouponNewPage(driver)
        ad_cpnew.enter_values()
        time.sleep(15)
