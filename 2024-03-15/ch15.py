import matplotlib.pyplot as plt
from random import randint

x=  [randint(0, 10) for _ in range(10000)]

# x = range(4)
y = [i**2 for i in x]

# plt.plot(x, y)
# plt.scatter(x, y)

plt.hist(x)
plt.show()