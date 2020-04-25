"""For this project, you will have to generate a sine vs cosine curve."""

import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0,10,0.1)

sine_wave_amplitude = np.sin(time)
cosine_wave_amplitude = np.cos(time)

plot.plot(time, sine_wave_amplitude, time, cosine_wave_amplitude)
plot.title("Sine and Cosine Wave")
plot.xlabel("Time")
plot.ylabel("Amplitude")
plot.legend(['Sine', 'Cosine'])
plot.grid()

plot.show()

