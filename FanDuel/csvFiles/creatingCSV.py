import pandas as pd

def createCSV():

        needCSVList = ["Spreads.csv", "Moneyline.csv", "OverUnder.csv" ]
        for i in range(len(needCSVList)):
                tempList = []

                emptyString = ""

                dict = {"Team Name": emptyString,
                        "Fanduel": emptyString,
                        "Fanduel Odds": emptyString}

                tempList.append(dict)

                df = pd.DataFrame(tempList)
                df.to_csv(needCSVList[i], index=False)

createCSV()