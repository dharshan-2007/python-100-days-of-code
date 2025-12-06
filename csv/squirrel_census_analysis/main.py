import pandas
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
greysq=len(data[data["Primary Fur Color"]=="Gray"])
cinnsq=len(data[data["Primary Fur Color"]=="Cinnamon"])
blacksq=len(data[data["Primary Fur Color"]=="Black"])
datadict={
    "Fur Color":["Grey","Cinnamon","Black"],
    "Count":[greysq,cinnsq,blacksq]
}
df=pandas.DataFrame(datadict)
df.to_csv("squirrel_count.csv")
