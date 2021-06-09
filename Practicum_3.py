import numpy as np
import matplotlib.pylab as plt
import control

m = 1
Kp = 1
Ki = 0
Kd = 0

I = control.tf([Ki], [1.0, 0.])
D = control.tf([Kd, 0.], [1.])
G = control.tf([1.0], [m, 5., 0.])

# print(D)
# print(I)
print("G(s):",G)

L = (Kp + I + D) * G
Sys2 = 1

print("L(s):",L)

Hclosed = control.feedback(L, Sys2)

# t, y = control.step_response(G)
t, y = control.step_response(Hclosed)

print("Hgs(s):",Hclosed)

control.bode_plot(G)

# plt.plot(t, y)
# plt.title(f"Kp:{Kp} Ki:{Ki}")
# plt.ylabel('Stap responsie')
# plt.xlabel('Tijd [s]')
plt.show()
