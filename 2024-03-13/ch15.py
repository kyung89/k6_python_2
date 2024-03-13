import matplotlib.pyplot as plt
import numpy as np
import random

# Getting Started 예제 소스 코드

#x = np.linspace(0, 2 * np.pi, 200)
#y = np.sin(x)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()

# https://matplotlib.org/stable/users/getting_started/
# 아침마다 와서 읽는다!!!


fig, ax = plt.subplots()  # Create a figure containing a single axes.

x = [1, 2, 3, 4]
y = [2, 3, 4, 6]
#ax.scatter(x, y, label="blue")  # Plot some data on the axes.
ax.plot(x, y, label="blue")

x2 = [1, 2, 3, 4]
y2 = [1, 2, 3, 4]
#ax.scatter(x2, y2, label="yellow")
ax.plot(x2, y2, label="yellow")

ax.set_title('Plot A and B')
ax.set_aspect("equal")
ax.set_xlabel("Age")
ax.set_ylabel("BMI")
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.legend()
plt.savefig("plot.png") # 그래프 저장
plt.show()

# plot 함수화

#def plot(x, y, label):
#  ax.plot(x, y, label=label)

#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#x = [1, 2, 3, 4]
#y = [2, 3, 4, 6]
#plot(x, y, "blue")  # Plot some data on the axes.

#x2 = [1, 2, 3, 4]
#y2 = [1, 2, 3, 4]
#plot(x2, y2, "yellow")
#ax.set_aspect("equal")
#ax.legend()
#plt.show()