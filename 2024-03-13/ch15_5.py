# p.426 랜덤 워크? 랜덤 밸류!

import matplotlib.pyplot as plt
import random 

#x = list(range(100))
#y = list(range(100, 200))

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(100, 200) for _ in range(100)]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.scatter(x[:50], y[:50], color="red")
ax.scatter(x[50:], y[50:], color="blue")
ax.plot(x[:50], y[:50], color="red")
ax.plot(x[50:], y[50:], color="blue")
plt.show()
