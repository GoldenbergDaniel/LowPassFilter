import math

import matplotlib.pyplot as plt
import numpy as np

from sinusoidal import Sinusoidal

amplitude = 1
frequency = 3
period = math.pi/3

def add(arr1, arr2):
    arr3 = []
    for i in range(len(arr1)):
        arr3.append(arr1[i] + arr2[i])
    return arr3

x = np.arange(0, 4*math.pi, math.pi/80)
y = np.sin((frequency * x))

wave1 = Sinusoidal(amplitude, frequency, period)

count = 12
wave1.generate_inputs(count)

plt.grid(color='black', linestyle='-', linewidth=0.5)
plt.plot(wave1.get_inputs_avg(), wave1.get_outputs_avg(), marker="o", color='blue', linestyle="none")
plt.plot(x, y, color='green')
plt.show()
