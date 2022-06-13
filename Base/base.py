import unittest
from selenium import webdriver
import chromedriver_autoinstaller

# DEFINE

class Base(unittest.TestCase):
    def setUp(self):
        chromedriver_autoinstaller.install()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        print("현재 크롬 드라이버 버전: ", chromedriver_autoinstaller.get_chrome_version())
        self.driver.set_window_size(1920, 1080)
        self.driver.implicitly_wait(30)


    def tearDown(self) -> None:
        if self.driver is not None:
            print("-----------------------------")
            print("Tests is finished")
            self.driver.close()
            self.driver.quit()
