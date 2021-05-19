import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([5.0])
noemer = np.array([1.0, 5])

H = control.tf(teller, noemer)

w = [0, 1, 5, 10, 100]
Hw_list = []

for i in range(len(w)):
    Hw = control.evalfr(H, 1j * w[i])
    Hw_list.append(Hw)
    Hw_abs = np.abs(Hw)
    Hw_arg = np.angle(Hw)
    print("w:{:<5} H(jw):{:<45} H|(jw)|:{:<30} arg(H(jw)):{:<30}".format(w[i], Hw, Hw_abs, np.degrees(Hw_arg)))

X = [x.real for x in Hw_list]
Y = [y.imag for y in Hw_list]
plt.scatter(X,Y, color='purple')
control.nyquist_plot(H)

plt.show()
