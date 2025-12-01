import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])
data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)
