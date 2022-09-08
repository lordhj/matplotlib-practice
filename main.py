import matplotlib.pyplot as plt
import numpy as np

a=np.linspace(0,10,11)
b=a**4
x=np.arange(0, 10)
y=2*x
fig=plt.figure(figsize=(3,3), dpi=100)

#Large Axes
axes1=fig.add_axes([0, 0, 1, 1])
axes1.set_xlim(0, 10)
axes1.set_ylim(0,10000)
axes1.set_xlabel("A")
axes1.set_ylabel("B")
axes1.set_title("Power of 4")
axes1.plot(a, b)

#Small Axes
axes2=fig.add_axes([0.2, 0.2, 0.1, 0.1])
axes1.set_xlim(1, 2)
axes1.set_ylim(0,400)
axes1.set_xlabel("A")
axes1.set_ylabel("B")
axes1.set_title("Zoomed IN")
axes2.plot(x, y)

#Saving fig
fig.savefig('newfig.png', bbox_inches='tight')

plt.show()