import matplotlib.pyplot as plt
import numpy as np

from mpl_interactions import ipyplot as iplt

x = np.linspace(0, np.pi, 200)
y = np.linspace(0, 10, 200)
X, Y = np.meshgrid(x, y)


def f(param1, param2):
    return np.sin(X) * param2 + np.exp(np.cos(Y * param1)) + param2


fig, ax = plt.subplots()
controls = iplt.imshow(f, param1=(-5, 5), param2=(-3, 12))

plt.show()