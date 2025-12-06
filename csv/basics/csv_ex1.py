import csv

with open("weather_data.csv","r") as datas:
    data=csv.reader(datas)
    temp=[]
    for row in data:
        if row[1]!="temp":
            temp.append(row[1])

    print(temp)