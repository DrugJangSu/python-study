# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     print(data)
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

## Using the panda library module, it's much more convenient

# import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data)
# print(data["temp"])
# print(data["day"])


import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# print(len(temp_list))

# # <way to calculate average #1>
# average =sum(temp_list) / len(temp_list)
# print(average)

# # <way to calculate average #2>
# print(data["temp"].mean())

# # <way to find max value>
# print(data["temp"].max())

# # Get Data in Columns
# print(data["condition"])
# print(data.condition) # another way to get a column

## Be aware that if your column name has a Capital letter or space, you must use the same format.

# Get Data in Rows
# print(data[data.day == "Monday"])

## Get row where temp is max
# data["temp"].max()
# data.temp.max()
# data.temp == data.temp.max()

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

## get monday's temp in Fahrenheit

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)
## Running the above code will create a new_data.csv file in the same directory.
