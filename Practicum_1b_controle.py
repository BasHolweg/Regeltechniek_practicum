import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab as cm

teller = np.array([5.0])
noemer = np.array([1.0, 5])

H = control.tf(teller, noemer)

t = np.arange(0, 10, 0.01)
u = np.sin(5*t)
y, T, xout = cm.lsim(H, u, t)

plt.show()
