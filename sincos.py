#%% 6 Challenge Programming ch09-cp06.py
import numpy as np
import matplotlib.pyplot as plt
linestyles = ['-', '--', '-.', ':']
#x=(            )(-np.pi * 2, np.pi * 2, 720)
#x = [0.01 * i for i in range(-700, 700)]
#x2 = [0.005 * i for i in range(-700, 700)]
#x = [0.005 * i for i in range(-700,700)]
#x = np.arange(-6, 6,0.1)
x = np.arange(-1,1,0.25)
#(               )
#x = np.linspace(-np.pi * 2, np.pi * 2, 720)
#cos, sin = np.cos(x/2), np.sin(x/2)
# (                   )
cos, sin = np.cos(x), np.sin(x)
#sin = np.sin(x2);cos = np.cos(x2);
#sin=np.sin(x)
#cos=np.cos(x)
#sin,cos=np.sin(x*(0.1668*np.pi)),np.cos(x*(0.1668*np.pi))
plt.plot(x, sin, ls=linestyles[3], label='sin')
plt.plot(x, cos, ls=linestyles[1], label='cos')
plt.title("Graph of sin cos")
plt.xlabel('radians')
plt.ylabel('value')
plt.grid()
plt.legend()
plt.show()
