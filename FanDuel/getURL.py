from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class gettingPageURL():

    def __init__(self, driver):

        self.driver = driver

    # This is something that should only have to get run once a day becuase new links are provided everyday - just need a
    # way to store the data so I can then access it from another python script
    def gettingMatchup(self):
        self.driver.get("https://sportsbook.fanduel.com/navigation/nba")
        self.driver.maximize_window()
        allLinks = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")

        gameURLlist = []
        for i in range(1, len(allLinks), 2):

            #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/basketball/nba']" ))).click()

            allLinks = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/basketball/nba']")

            allLinks[i].click()
            #time.sleep(3)
            gameURLlist.append(self.driver.current_url)
            self.driver.back()
            #time.sleep(3)
        return gameURLlist