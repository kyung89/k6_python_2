
from matplotlib import pyplot as plt
import csv
import datetime as dt
from datetime import datetime

x1, y1 = [], []
x2, y2 = [], []

with open('a.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(type(datetime.strptime(row[2], '%Y-%m-%d')), type(int(row[4])), type(int(row[5])))
        x1.append(datetime.strptime(row[2], '%Y-%m-%d'))
        y1.append(int(row[4]))
        y2.append(int(row[5]))

plt.plot(x1, y1, label='TMAX', color='red')
plt.plot(x1, y2, label='TMIN', color='blue')
plt.fill_between(x1, y1, y2, alpha=0.5)
plt.xticks(x1, rotation='vertical')
plt.xlabel('Date')
plt.legend()
plt.show()
