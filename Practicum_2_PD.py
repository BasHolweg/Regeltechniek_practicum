import numpy as np
import matplotlib.pylab as plt
import control

m = 1
Kp = 100
Kd = 20

L = control.tf([Kd, Kp], [1.])
H = control.tf([1.0], [m, 0., 0.])

print(L)
print(H)

Sys1 = L*H
Sys2 = 1
Sys3 = Kp*H

Hp = control.feedback(Sys3, Sys2)
Hclosed = control.feedback(Sys1, Sys2)

t, y = control.step_response(Hclosed)
polen = control.pole(Hclosed)

control.bode_plot(Sys1)
control.bode_plot(Hp)

print(polen)

# plt.plot(t, y)
# plt.ylabel('Stap responsie')
# plt.xlabel('Tijd [s]')
plt.show()
