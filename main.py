import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,10,11)
b=a**4
x=np.arange(0, 10)
y=2*x



#ONE DIMENSIONAL
"""
fig, axes=plt.subplots(nrows=3, ncols=1)
for ax in axes:
    ax.plot(x, y)
"""
#axes[0].plot(x,y)
#axes[1].plot(a,b)



fig, axes= plt.subplots(nrows=2, ncols=2)
axes[0][0].plot(x, y)
axes[0][1].plot(x, y)
axes[1][1].plot(a, b)
axes[1][0].set_ylabel("Y Label-Empty plot 1.0")
axes[1][1].set_title("Exponential Plot 1.1")
fig.suptitle("Subplots Demo Figure Level", fontsize=18)
plt.tight_layout()

fig.savefig("newsubplot.png", bbox_inches='tight')
plt.show()