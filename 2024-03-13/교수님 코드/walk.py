import matplotlib.pyplot as plt
import random
#x = list(range(100))
#y = list(range(100, 200))

x = [random.randint(0, 100) for _ in range(100)]
y = [random.randint(100, 200) for _ in range(100)]

x_walks = [5, -5]
y_walks = [5, -5]

x_data, y_data = [], []
x, y = 0, 0
x_data.append(x)
y_data.append(y)
lst = [-5, 5]
random_walks = [(lst[random.randint(0, 1)], lst[random.randint(0, 1)]) for _ in range(100)]
#print(random_walks)

for x_move, y_move in random_walks:
    x, y = x+x_move, y+y_move
    x_data.append(x)
    y_data.append(y)
    

fig, ax = plt.subplots()
ax.plot(x_data, y_data)
plt.show()