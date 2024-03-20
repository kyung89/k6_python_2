# 1교시는 백준 문제 풀이 시간을 가졌음

from matplotlib import  pyplot as plt

import random
from random import randint 

# print(randint(0, 9))
# x = [randint(0, 9) for _ in range(1000)]

# x = [1, 2, 3, 4]
# print(type(x), x)

# y = [i**2 for i in x]
# print(type(y), y)

# print(x, y)

# plt.plot(x, y)
# plt.scatter(x, y)
# plt.hist(x)
# plt.show()

x1 = list(range(1, 5))
y1 = [i*i for i in x1]
print(x1, type(x1))

x2 = list(range(1, 5))
y2 = [i**3 for i in x2]

# fig, axs = plt.subplots(1, 2, figsize=(10, 5)) # 나란히 두개를 그립시다

# axs[0].plot(x1, y1, label = "A", color = "red")
# axs[0].plot(x2, y2, label = "B", color = "blue")

# axs[1].scatter(x1, y1, label = "A", color = "red")
# axs[1].scatter(x2, y2, label = "B", color = "blue")

plt.plot(x1, y1, label = "A", color = "red")
plt.plot(x2, y2, label = "B", color = "blue")

plt.title("X Square")
plt.xlabel("X")
plt.ylabel("X Square")
plt.legend()
plt.show()
