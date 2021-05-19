import numpy as np
import matplotlib.pylab as plt
import control

teller = np.array([18.])
noemer = np.array([1., 1.2, 36.])
H = control.tf(teller, noemer)

K = 100

Sys1 = K * H
Sys2 = 1
Hclosed = control.feedback(Sys1, Sys2)
tclosed, yclosed = control.step_response(Hclosed)
topen, yopen = control.step_response(Sys1)

c_closed = round(yclosed[len(tclosed) - 1])
D_closed = round(max(yclosed) - 1)
tp_closed = round(tclosed[next(len(yclosed)-i for i in range(2, len(yclosed)-1) if yclosed[-i] == yclosed.max())]-tclosed[0], 2)
Est_closed = round(1 - c_closed)
ts_closed = round(tclosed[next(len(yclosed)-i for i in range(2, len(yclosed)-1) if abs(yclosed[-i]/yclosed[-1])<0.95)]-tclosed[0], 2)

c_open = round(yopen[len(topen) - 1])
D_open = round(max(yopen) - 1)
tp_open = round(topen[next(len(yopen)-i for i in range(2, len(yopen)-1) if yopen[-i] == yopen.max())]-topen[0], 2)
Est_open = round(1 - c_open)
ts_open = round(topen[next(len(yopen)-i for i in range(2, len(yopen)-1) if abs(yopen[-i]/yopen[-1])<0.95)]-topen[0], 2)

print("Gesloten lus systeem:")
print(f"Doorschot:          {D_closed}")
print(f"Piektijd:           {tp_closed}")
print(f"Statische fout:     {Est_closed}")
print(f"Insteltijd:         {ts_closed}\n")

print("Open lus systeem:")
print(f"Doorschot:          {D_open}")
print(f"Piektijd:           {tp_open}")
print(f"Statische fout:     {Est_open}")
print(f"Insteltijd:         {ts_open}")

fig, res = plt.subplots(2, 1, constrained_layout=True)
res[0].plot(tclosed, yclosed)
res[0].set_xlabel("t")
res[0].set_title("Closed loop response")

res[1].plot(topen, yopen)
res[1].set_xlabel("t")
res[1].set_title("Open loop response")

plt.show()
