from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,10,11)
b=a**4
x=np.arange(0, 10)
y=2*x

fig=plt.figure()
ax=fig.add_axes([0, 0, 1, 1])
lines=ax.plot(x,x, color="purple", lw=2)
lines[0].set_dashes([1,2,1,2,10,2])
#ax.plot(x, x+1, color="#650dbd", lw=3, ls="-.")
ax.plot(x, x+1, color='green', lw=2, marker='o', markerfacecolor='red', markeredgewidth=4, markeredgecolor='orange')
plt.show()