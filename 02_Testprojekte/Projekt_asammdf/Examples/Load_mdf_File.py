# https://asammdf.readthedocs.io/en/latest/examples.html

from asammdf import MDF

filename = "my_new_file.mf4"

mdf = MDF(filename)
speed = mdf.get('WheelSpeed')
speed.plot()

important_signals = ['WheelSpeed', 'VehicleSpeed', 'VehicleAcceleration']
# get short measurement with a subset of channels from 10s to 12s
short = mdf.filter(important_signals).cut(start=10, stop=12)

# convert to version 4.10 and save to disk
short.convert('4.10').save('important signals.mf4')

# plot some channels from a huge file
efficient = MDF('huge.mf4')
for signal in efficient.select(['Sensor1', 'Voltage3']):
   signal.plot()