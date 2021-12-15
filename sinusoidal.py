import math
import numpy as np

class Sinusoidal:
    def __init__(self, amplitude, frequency, period):
        self.amplitude = amplitude
        self.frequency = frequency
        self.period = period
        self.inputs = []
        self.inputs_avg = []
        self.outputs = []
    def evaluate(self, input):
        return self.amplitude * np.sin(self.frequency * input)
    def generate_inputs(self, count, place=2):
        for i in range(count):
            self.inputs.append(round(((i+1)*(self.period)), place))
        return self.inputs
    def get_inputs_avg(self, place=2):
        for i in self.inputs:
            avg = (i-self.period + i)/2
            self.inputs_avg.append(round(avg, place))
        return self.inputs_avg
    def get_outputs_avg(self, place=2):
        avg_outputs = []
        for i in self.inputs:
            avg = (self.amplitude * math.sin(self.frequency * i) + self.amplitude * math.sin(self.frequency * (i+self.period))) / 2
            avg_outputs.append(round(avg, place))
        return avg_outputs
