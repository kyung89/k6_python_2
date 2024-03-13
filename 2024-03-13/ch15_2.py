import matplotlib.pyplot as plt
import numpy as np
import random

fig, ax = plt.subplots()  # Create a figure containing a single axes.

data = [random.randint(0, 100) for _ in range(1000)]
ax.hist(data)
plt.show()