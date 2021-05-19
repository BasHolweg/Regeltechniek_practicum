import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([5.0])
noemer = np.array([1.0, 5])

H = control.tf(teller, noemer)

w = [0, 1, 5, 10, 100]
Hw_list = []
abs_list = []
arg_list = []

for i in range(len(w)):
    Hw = control.evalfr(H, 1j * w[i])
    Hw_abs = np.abs(Hw)
    Hw_arg = np.angle(Hw)
    Hw_list.append(Hw)
    abs_list.append(Hw_abs)
    arg_list.append(np.degrees(Hw_arg))
    print("w:{:<5} H(jw):{:<45} H|(jw)|:{:<30} arg(H(jw)):{:<30}".format(w[i], Hw, Hw_abs, np.degrees(Hw_arg)))

# fig, ax = plt.subplots(2, 1)
control.bode_plot(H)
# ax[0].scatter(w, abs_list, color="purple")
# ax[1].scatter(w, arg_list, color="purple")

plt.show()
