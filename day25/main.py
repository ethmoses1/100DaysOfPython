
# data = []
# with open("./weather_data.csv") as weather_data:
#     contents = weather_data.read()
#     data = contents.split("\n")
#
# print(data)

# import csv
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])


#COLUMNS

data_dict = data.to_dict()
temp_list = data["temp"].to_list()

# average_temp = sum(temp_list)/len(temp_list)
# print(average_temp)



average = data["temp"].mean()
print(average)


#ROWS
monday = data[data.day == "Monday"]
max = data[data.temp == data.temp.max()]