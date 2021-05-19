import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([2.0])
noemer = np.array([1.0, -3.0])
H = control.tf(teller, noemer)

K = [0.1, 1, 1.5, 10]

for i in range(len(K)):
    Sys1 = K[i]*H
    Sys2 = 1
    Hclosed = control.feedback(Sys1, Sys2)
    t, y = control.step_response(Hclosed)
    plt.plot(t, y)
    plt.legend(K)

plt.ylim(0, 80)
plt.xlim(0, 3)
plt.ylabel('Stap responsie')
plt.xlabel('Tijd [s]')
plt.show()
