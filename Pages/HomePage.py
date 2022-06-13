from selenium import webdriver
from selenium.webdriver.common.by import By

TXT_TITLE = "30대 패션 쇼핑앱 - 플레어"

class HomePage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.txt_title = driver.title
        self.tab_home = driver.find_element(By.XPATH, "//*[@id='container']/div/section[1]/div[2]/div/section/div/div/div[1]/a")
        self.tab_event = driver.find_element(By.XPATH, "//*[@id='container']/div/section[1]/div[2]/div/section/div/div/div[3]/a")
        self.tab_store = driver.find_element(By.XPATH, "//*[@id='container']/div/section[1]/div[2]/div/section/div/div/div[4]/a")
        #self.nav_home = driver.find_element(By.XPATH, '//a[contains(@href,"/")]')
        self.nav_categories = driver.find_element(By.XPATH, "//*[@id='wrap']/div[4]/section/nav/div[2]/a/button")
        self.nav_favor = driver.find_element(By.XPATH, "//*[@id='wrap']/div[4]/section/nav/div[3]/a/button")
        self.nav_mypage = driver.find_element(By.XPATH, "//*[@id='wrap']/div[4]/section/nav/div[4]/a/button")
        self.driver.implicitly_wait(10)

    def click_categories(self):
        self.nav_categories.click()
        self.driver.implicitly_wait(10)

    def click_favor(self):
        self.nav_favor.click()
        self.driver.implicitly_wait(10)

    def click_mypage(self):
        self.nav_mypage.click()
        self.driver.implicitly_wait(10)

    def click_ranking(self):
        self.tab_ranking = self.driver.find_element(By.XPATH, "//*[@id='container']/div/section[1]/div[2]/div/section/div/div/div[2]/a")
        self.tab_ranking.click()
        self.driver.implicitly_wait(10)

    def __del__(self):
        print("HomePage 객체 소멸")