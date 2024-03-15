# with open("weather_data/sitka_weather_07-2021_simple.csv") as f:
#     for line in f:
#         print(line.rstrip().split(","))

import csv
# import os
# os.path
from pathlib import Path    # os 에 따른 다른 path 처리에 좋다
from matplotlib import pyplot as plt
# import json

x1, y1 = [], []
x2, y2 = [], []

COL_DATE = 2
COL_TMAX = 4
COL_TMIN = 5

with open(Path("weather_data","sitka_weather_07-2021_simple.csv")) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        x1.append(line[COL_DATE])
        y1.append(line[COL_TMAX])

        x2.append(line[COL_DATE])
        y2.append(line[COL_TMIN])

# print(f"x1 : {x1}")
# print(f"y1 : {y1}")

for idx, h in enumerate(header):
    print(idx, h)

plt.plot(x1, y1, label = header[COL_TMAX])
plt.plot(x2, y2, label = header[COL_TMIN])
plt.xticks(rotation=90)
plt.legend()
plt.fill_between(x1, y1, y2, facecolor="blue", alpha=0.1) # p.460
plt.show()