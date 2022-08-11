import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

fur_color = data["Primary Fur Color"]

counts = fur_color.value_counts()

new_data = {
    "Fur Color": {0: "gray", 1: "red", 2: "black"},
    "Count": {0: counts.Gray, 1: counts.Cinnamon, 2: counts.Black}
}

new_frame = pd.DataFrame(new_data)
new_frame.to_csv("squirrel_color_counts.csv")
