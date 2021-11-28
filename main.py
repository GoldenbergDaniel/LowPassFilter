import math

import matplotlib.pyplot as plt
import numpy as np

amplitude = 1
frequency = 0.5
period = math.pi/2

x = [period, 2*period, 3*period, 4*period, 5*period, 6*period, 7*period]
y = []

for i in x:
    y.append(amplitude * math.sin(frequency * i))

# for i in x:
#     y_.append(amplitude * math.sin(2 * i))

x1 = np.arange(0, 4*math.pi, math.pi/20)
y1 = amplitude * np.sin(frequency * x1)
y2 = amplitude * np.sin(2 * x1)

plt.plot(x, y, marker="o", linestyle="None")
plt.plot(x1, y1 + y2)

plt.show()
