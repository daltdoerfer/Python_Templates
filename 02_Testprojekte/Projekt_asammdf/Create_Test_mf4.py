# https://asammdf.readthedocs.io/en/latest/examples.html
from asammdf import MDF, Signal
import numpy as np

# create 3 Signal objects
timestamps = np.array([0.01 * t for t in range(20)], dtype=np.float32)

signal = []

# float64
signal_1 = Signal(samples=np.array([0, 0, 50, 80, 150, 250, 400, 800, 1200, 1500, 2000, 2100, 2120, 2080, 2000, 2150, 1880, 1750, 1800, 1800], dtype=np.float64),
                   timestamps=timestamps,
                   name='EngineRPM',
                   unit='rpm')

# float64
signal_2 = Signal(samples=np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 56, 58, 59, 60, 58, 57, 56, 54], dtype=np.float64),
                   timestamps=timestamps,
                   name='Gas_Pedal',
                   unit='%')

# float64
signal_3 = Signal(samples=np.array([0, 0, 0, 10, 20, 30, 40, 80, 120, 150, 200, 210, 212, 208, 200, 215, 188, 175, 180, 180], dtype=np.float64),
                   timestamps=timestamps,
                   name='EM01_RPM',
                   unit='rpm')


# create empty MDf version 4.00 file
with MDF(version='4.10') as mdf4:

    # append the 3 signals to the new file
    signals = [signal_1, signal_2, signal_3 ]
    mdf4.append(signals, comment='Created by Python')

    # save new file
    mdf4.save('my_new_file.mf4', overwrite=True)

