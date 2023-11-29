import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray, red, black = 0,0,0
list = data["Primary Fur Color"].to_list()
for item in list:
    if item == "Gray":
        gray += 1
    elif item == "Cinnamon":
        red += 1
    elif item == "Black":
        black += 1

squirrel_dict = {"Fur Color":["Gray", "Red", "Black"] , "Count": [gray, red, black]}
squirrel_data = pd.DataFrame(squirrel_dict)
squirrel_data.to_csv("Squirrel Colors.csv")