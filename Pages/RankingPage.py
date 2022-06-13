from selenium import webdriver
from selenium.webdriver.common.by import By

class RankingPage:
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.tab_ranking = self.driver.find_element(By.XPATH, '//*[text()="랭킹"]')
        self.first = self.driver.find_element(By.XPATH, "//*[@id='container']/div[2]/section[2]/div[1]")
        self.driver.implicitly_wait(10)

    def click_item(self, item):
        self.item = item
        self.item.click()

    def __del__(self):
        print("RankingPage 객체 소멸")