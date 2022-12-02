import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome("C:/basketball/venv/Scripts/chromedriver.exe")


driver.get("https://sportsbook.fanduel.com/basketball/nba/dallas-mavericks-@-detroit-pistons-31940969")

time.sleep(5)
firstButton = driver.find_element_by_xpath("//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[2]/span")

print(firstButton.get_attribute("innerHTML"))