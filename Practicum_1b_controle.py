import numpy as np
import matplotlib.pylab as plt
import control
import control.matlab as cm
import scipy.signal as sig

teller = np.array([5.0])
noemer = np.array([1.0, 5])

H = control.tf(teller, noemer)
H1 = sig.lti(teller, noemer)

t = np.arange(0, 10, 0.01)
u = np.sin(5.*t)

tout, y, x = sig.lsim(H1, u, t)
# y, T, xout = cm.lsim(H, u, t)

plt.plot(t, y)
plt.plot(t, u)
plt.show()
