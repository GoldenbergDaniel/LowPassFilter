import math
import numpy as np

from sinusoidal import Sinusoidal

wave = Sinusoidal(1, 1/3, math.pi/2)
wave.generate_inputs(12)

print(wave.get_inputs_avg())
print(wave.get_outputs_avg())
