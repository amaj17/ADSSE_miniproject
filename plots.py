import matplotlib.pyplot as plt
import numpy as np


brute = np.array([0.000056, 0.002556 , 0.308672, 33.7554 ,1189.87, 3377.66 ])
n = np.array([10, 100, 1000, 10000,50000, 100000])
dac = np.array([0.0000973, 0.000913, 0.011568, 0.136917, 0.744698, 1.84362])
kadane = np.array([0.0000253, 0.0000765,  0.000738, 0.007256, 0.038569, 0.075981])

plt.plot(brute, n, label = "brute-fore", linestyle='-', marker='o', color='b')
plt.plot(dac, n, label = "divide-and-conque", linestyle='-', marker='o', color='g')
plt.plot(kadane, n, label = "Kadane's", linestyle='-', marker='o', color='r')
plt.xlabel("Time (s)")
plt.ylabel("Array size (n)")
plt.legend()
plt.show()
