import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(0.0, 2 * np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

ax.plot(x, y1, linestyle = '-', color = 'b')
ax.plot(x, y2, linestyle = '', marker = '+', color = 'r')

plt.legend(['sin(x)', 'cos(x)'])
plt.savefig('chart.png')
plt.show()