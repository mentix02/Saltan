import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt


fig = plt.figure()
ax = fig.gca(projection='3d')
z = np.linspace(1, 2, 3	)
r = z
x = r * 1
y = r * 2
ax.plot(x, y, z, label='parametric curve')
ax.legend()

plt.show()
