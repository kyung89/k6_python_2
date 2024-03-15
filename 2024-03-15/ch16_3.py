

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

with open(Path("weather_data","sitka_weather_2021_full.csv")) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        x1.append(line[COL_DATE])
        y1.append(line[COL_TMAX])

        x2.append(line[COL_DATE])
        y2.append(line[COL_TMIN])

plt.plot(x1, y1, label = header[COL_TMAX])
#plt.plot(x2, y2, label = header[COL_TMIN])
plt.xticks(rotation=90)
plt.legend()
plt.show()