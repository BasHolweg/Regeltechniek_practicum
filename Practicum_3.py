import numpy as np
import matplotlib.pylab as plt
import control

m = 1
Kp = 20
Ki = 1
Kd = 5

I = control.tf([Ki], [1.0, 0.])
D = control.tf([Kd, 0.], [1.])
G = control.tf([1.0], [m, -5., 0.])

print(I)
print(D)
print(G)

L = (Kp + I + D)*G
Sys2 = 1

print(L)

Hclosed = control.feedback(L, Sys2)

t, y = control.step_response(Hclosed)

print(Hclosed)

# control.bode_plot(Hclosed)

plt.plot(t, y)
plt.ylabel('Stap responsie')
plt.xlabel('Tijd [s]')
plt.show()
