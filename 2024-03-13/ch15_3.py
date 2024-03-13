import matplotlib.pyplot as plt

x = list(range(1, 101))
square = [i**2 for i in x]
fig, ax = plt.subplots()
#ax.plot(x, square, linewidth=5)
#ax.plot(x, square, linewidth=5, color="red")
ax.scatter(x, square, c=square, cmap=plt.cm.Blues)

#ax.set_xlim(0, 20)
#ax.set_ylim(0, 20)
#ax.set_title("Square", fontsize=30)
#ax.set_xlabel("X", fontsize=10)
#ax.set_ylabel("Y", fontsize=10)
ax.set_title("Square")
ax.set_xlabel("X")
ax.set_ylabel("Y")
#ax.tick_params(labelsize=30)
plt.style.use('seaborn-v0_8')
for s in plt.style.available:
    print(s)

ax.ticklabel_format(style="plain")
plt.show()

