import matplotlib.pyplot as plt
import numpy as np
x=np.arange(0, 10)
y=2*x
plt.plot(x, y)
plt.title("Simple Plot")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()