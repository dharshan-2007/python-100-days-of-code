import pandas

data=pandas.read_csv("weather_data.csv")
print(data)
print(data['temp'])
data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(temp_list)

print(data["condition"])
print(data.condition)

print(data[data.day=="Monday"])
print(data[data.temp==data.temp.max()])

#create dataframe from scratch

data_dict={"Students":["arun","babu","chandru"],"scores":[70,80,91]}
data=pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")