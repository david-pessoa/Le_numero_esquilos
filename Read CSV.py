import pandas as pd
data = pd.read_csv("weather_data.csv")
temps_c = data["temp"].to_list()
temps_f = []
for temp in temps_c:
    temp = temp * 9 / 5 + 32
    temps_f.append(temp)


    
