import numpy as np
import matplotlib.pylab as plt
import control


def print_data(t, y, name):
    c = round(y[len(t) - 1])
    d = round(max(y) - 1)
    tp = round(t[next(len(y) - i for i in range(2, len(y) - 1) if y[-i] == y.max())] - t[0], 2)
    est = round(1 - c)
    ts = round(t[next(len(y) - i for i in range(2, len(y) - 1) if abs(y[-i] / y[-1]) < 0.95)] - t[0], 2)

    print(name)
    print(f"Doorschot:          {d}")
    print(f"Piektijd:           {tp}")
    print(f"Statische fout:     {est}")
    print(f"Insteltijd:         {ts}\n")


teller = np.array([18.])
noemer = np.array([1., 1.2, 36.])
H = control.tf(teller, noemer)

K = 100

Sys1 = K * H
Sys2 = 1
Hclosed = control.feedback(Sys1, Sys2)
tclosed, yclosed = control.step_response(Hclosed)
topen, yopen = control.step_response(Sys1)

print_data(tclosed, yclosed, "Gesloten lus systeem:")
print_data(topen, yopen, "Open lus systeem:")

fig, res = plt.subplots(2, 1, constrained_layout=False)
res[0].plot(tclosed, yclosed)
res[0].set_xlabel("t [s]")
res[0].set_title("Closed loop response")

res[1].plot(topen, yopen)
res[1].set_xlabel("t [s]")
res[1].set_title("Open loop response")

plt.show()
