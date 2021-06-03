import numpy as np
import matplotlib.pylab as plt
import control

m = 1
Kp = 100

teller = np.array([1.0])
noemer = np.array([m, 0., 0.])

H = control.tf(teller, noemer)
print(H)

Sys1 = Kp*H
Sys2 = 1
Hclosed = control.feedback(Sys1, Sys2)
t, y = control.step_response(Hclosed)
polen = control.pole(Hclosed)

print(polen)

plt.plot(t, y)
plt.ylabel('Stap responsie')
plt.xlabel('Tijd [s]')
plt.show()
