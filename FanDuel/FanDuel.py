import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class FanDuel():

    def __init__(self, driver):
        self.driver = driver

    def getGameURL(self):
        allLinks = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")

        gameURLlist = []
        for i in range(1, len(allLinks), 2):
            allLinks = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")

            allLinks[i].click()
            time.sleep(3)
            gameURLlist.append(self.driver.current_url)
            self.driver.back()
            time.sleep(3)
        return gameURLlist

def main():
    driver = webdriver.Chrome("C:/basketball/venv/Scripts/chromedriver.exe")

    driver.get("https://sportsbook.fanduel.com/navigation/nba")

    driver.maximize_window()

    fanduel = FanDuel(driver)

    print(fanduel.getGameURL())
if __name__ == "__main__":
    main()
