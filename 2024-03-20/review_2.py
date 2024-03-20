from matplotlib import  pyplot as plt
from random import randint 
import csv
from pathlib import Path
from datetime import datetime as dt

x1 = []
y1 = []

x2 = []
y2 = []

with open(Path("weather_data","sitka_weather_07-2021_simple.csv"), "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    # print(header)
    for row in reader:
        # print(row, type(row))
        # print(type(row[2]), type(row[4]), type(row[5]))
        x1.append(dt.strptime(row[2], "%Y-%m-%d"))
        y1.append(int(row[4]))
        y2.append(int(row[5]))


plt.plot(x1, y1, label = header[4], color = "red")
plt.plot(x1, y2, label = header[5], color = "blue")
plt.fill_between(x1, y1, y2, alpha=0.5) # p.460

plt.xticks(x1, rotation="vertical")

# plt.title("X Square")
# plt.xlabel("X")
# plt.ylabel("X Square")
plt.legend()
plt.show()
