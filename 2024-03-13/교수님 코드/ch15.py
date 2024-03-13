import matplotlib.pyplot as plt

x = list(range(1, 101))
square = [i**2 for i in x]

plt.scatter(x, square, c=square, cmap=plt.cm.Blues)
plt.colorbar()
plt.savefig('colorbar.png')

plt.show()