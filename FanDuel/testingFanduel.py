import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



driver = webdriver.Chrome("C:/basketball/venv/Scripts/chromedriver.exe")


driver.get("https://sportsbook.fanduel.com/basketball/nba/atlanta-hawks-@-philadelphia-76ers-31935782")

#driver.maximize_window()
driver.implicitly_wait(5)
#time.sleep(1000)
#driver.find_element(By.XPATH, '//span[@class="cw cx ae aj hr hs ht kl gh s fy ei h i j ak l m al o am q an bt"]')
#time.sleep(5)


#myElem = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div[1]/div/div[1]/span')))
#print(myElem.get_attribute("innerHTML"))

# I will need to send the keys in order to open up the inspector tool - that is what will load the
# elements in order to be able to retrieve them - will need to do this for every page that is loaded


# getting certain stats - they are all in <span> objects - i can get them all - but in order for
# it to get what I want, I may need to exclude the things that I do not need, and then perform the correct
# functionality .... i.e getting alt passing yards - get those elements with span - exclude everything but what "alt passing yards"
# I will need a way to categorize this in order to be able to compare it to other sports books that may not use the same exact name

# EAch page will needs its own functions - there may be shared similarities between pages, but some will be unique in their own way
time.sleep(10)
allTags = driver.find_elements(By.CSS_SELECTOR, "span")
allElements = []
for tags in allTags:
    # This will print all of the elements that are gotten
    #print(tags.get_attribute("innerHTML"))
    #putting all of the elements into a list
    allElements.append(tags.get_attribute("innerHTML"))

# This will get me the index of what I want - I just have to edit the string that is in there
# Once I have the index of the title, I will be able to get the information that i need about each player based off
# the pattern of the strings that are printed in the list for each player
passingProps = allElements.index("Player Passing Yds")
print(passingProps)





driver.close()