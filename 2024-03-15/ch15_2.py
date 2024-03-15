from matplotlib import pyplot as plt
from matplotlib.ticker import MultipleLocator

x1 = list(range(5))
y1 = [i**2 for i in x1]

x2 = list(range(5))
y2 = [i**3 for i in x1]

fig, ax = plt.subplots()
ax.plot(x1, y1, label="AAA", color="red",linewidth=5)
ax.plot(x2, y2, label="BBB", color="black")
ax.scatter(x1, y1, color="red")
ax.scatter(x2, y2, color="black")

ax.set_title("AAA vs BBB")

ax.set_xlabel("x1")
ax.set_ylabel("y1")

# ax.set_xticks([0, 1, 2, 3, 4])

ax.xaxis.set_major_locator(MultipleLocator(1))

ax.legend()
plt.show()