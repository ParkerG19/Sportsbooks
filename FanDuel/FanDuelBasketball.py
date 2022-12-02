import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from getURL import gettingPageURL
from selenium.common.exceptions import NoSuchElementException




class FanduelBasketball():

    def __init__(self, driver):
        self.driver = driver
        # These are the xpaths for the popular page goes in order of away team spread, odds, moneyline, over, odds, and then
        # home team spread, odds, moneyline, under, odds
        self.popularLiveX = ["//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span",  # Away Team Name
                            "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/span[1]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/span[2]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[2]/span",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[3]/span[1]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[3]/span[2]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span",   # Home Team Name
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/span[1]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/span[2]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/span",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[3]/span[1]",
                             "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[4]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[3]/span[2]"
                             ]
        # These are the xpaths for the pre game odds - goes in the same order as the live xpaths
        self.popularPreGameX = ["//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[1]/div[1]/div/div/div/div/span",  # Away Team Name
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/span[1]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[1]/span[2]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[2]/span",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[3]/span[1]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[1]/div[3]/span[2]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div/div/div/div/span",   # Home Team Name
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/span[1]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[1]/span[2]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[2]/span",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[3]/span[1]",
                               "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[3]/div/div[2]/div/div[3]/div/div/div[2]/div[2]/div[3]/span[2]"
                                ]

    # This function will get the main game lines - this is displayed on the "popular" page of FanDuel ONLY GETTING THE LINES
    # This page is also the first one that appears when the url to a game is pressed - so it will be the
    # URL that is given from getURL method

    # This function will tell me if the game is live or not - and will be determine which xpath to use
    # If this function returns '1' that means that the game is live, else the game is not live
    def live(self, driver):
        liveX = "//*[@id='root']/div/div[2]/div[1]/div/div[2]/div[2]/div/div[3]/div[1]"
        try:
            self.driver.find_element_by_xpath(liveX)
        except NoSuchElementException:
            return 0
        return 1

    def popular(self, url):

        self.driver.get(url)

        # This should open the inspector page - which I think needs to happen in order to load the elements that are
        # on the page - because the page is dynamic. I am not seeing the inspector open - but it doesn't seem like it
        # has to on this computer - it may have to on my laptop becuase that is where I learned that this was a solution
        # to not being able to find the elements that are on the page
        ActionChains(self.driver).send_keys(Keys.F12)

        # Don't want to use all of the try loops if I don't have to. I can append to a list and make a dataframe from that information
        isItLive = self.live(self.driver)
        dataList = []

        if (isItLive == 1):

            for i in range(len(self.popularLiveX)):
                    try:
                        data = self.driver.find_element_by_xpath(self.popularLiveX[i]).get_attribute("innerHTML")
                        dataList.append(data)
                    except NoSuchElementException:
                        dataList.append("NA")

        else:
            for i in range(len(self.popularPreGameX)):
                    try:
                        data = self.driver.find_element_by_xpath(self.popularPreGameX[i]).get_attribute("innerHTML")
                        dataList.append(data)
                    except NoSuchElementException:
                        dataList.append("NA")


        awayTeamSpread = [dataList[0], dataList[1], dataList[2]]#fullSpreadAway]
        #tempList.append(awayTeamSpread)
        df1 = pd.DataFrame(awayTeamSpread)
        df1 = df1.transpose()

        df1.to_csv('csvFiles/Spreads.csv', mode='a', header=False, index=False)

        homeSpread = [dataList[6], dataList[7], dataList[8]]#fullSpreadHome]
        df2 = pd.DataFrame(homeSpread)
        df2 = df2.transpose()
        df2.to_csv('csvFiles/Spreads.csv', mode='a', header=False, index=False)


        #--------------------------------------------------------------------------------------------------------------#

        # This section is not necessary for functional use of comparing - it is simply displaying the information that is
        # being scraped from FanDuel - best for testing purposes... but won't have much of a use during implementation unless
        # my goal is to display all of the values
        #--------------------------------------------------------------------------------------------------------------#
        #data = [[awayTeamSpread, awayTeamSpreadOdds, awayTeamMoney,over, overOdds],
            #    [homeTeamSpread, homeTeamSpreadOdds, homeTeamMoney, under, underOdds]]

        #df = pd.DataFrame(dataList)
        #df.columns = ["|Spread|", "|Spread Odds|", "|MoneyLine", "|Over/Under|", "|Over/Under Odds|"]
        #print(df.transpose())
        #--------------------------------------------------------------------------------------------------------------#






def main():
    driver = webdriver.Chrome("C:/Sportsbooks/venv/Scripts/chromedriver.exe")

    # getting the list of basketball game url's and adding them to csv file to be accessed by functions
    urls = gettingPageURL(driver)
    urlList = urls.gettingMatchup()


    driver = webdriver.Chrome("C:/Sportsbooks/venv/Scripts/chromedriver.exe")
    page = FanduelBasketball(driver)
    for i in range(len(urlList)):
        popularPages = page.popular(urlList[i])
        #print(popularPages)    # THIS PRINT STATEMENT IS WHAT WIL PRINT THE NONE VALUE




if __name__ == "__main__":
    main()



