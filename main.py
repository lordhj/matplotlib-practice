from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,10,11)
b=a**4
x=np.arange(0, 10)
y=2*x

fig=plt.figure()
ax=fig.add_axes([0, 0, 1, 1])
ax.plot(x,x, label="X v/s X")
ax.plot(x,x**2, label="X v/s X^2")
ax.legend()

plt.show()