import numpy as np
import matplotlib.pylab as plt
import control

w = 100
d = [0.01, 0.1, 0.2, 0.5, 1, 2]

for i in range(len(d)):
    teller = np.array([w**2])
    noemer = np.array([1.0, 2*d[i]*w, w**2])
    H = control.tf(teller, noemer)
    control.bode(H)
    plt.show()

