import matplotlib.pyplot as plt
plt.ion()
plt.plot([1.6, 2.7])
ax = plt.gca()
ax.plot([3.1, 2.2])
plt.draw()
plt.show()