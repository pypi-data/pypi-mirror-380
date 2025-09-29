"""Usage examples of the MyRIO class: analog inputs and outputs

This examples show how to use the analog inputs and outputs
and the onboard Accelerometer.

We have a set of myRIOs in our facilities that we complement
with some MXP cards. These cards have a temperature sensor in
AI0 and a Light sensor in AI1. We use these channels
in our examples. The port that we use most is the A port, so
we set it as default on our package.

Last update: 2024/03/07 Aitzol Ezeiza Ramos (UPV/EHU)
"""

import myrio_base
import time

myrio1 = myrio_base.MyRIO()

# Read onboard accelerometer values
print("Accelerometer test (5 seconds)")
for i in range(10):
    print(myrio1.read_analog_accelerometer())
    time.sleep(0.5)
print("End of Accelerometer test")
time.sleep(2)

# Read analog inputs
print("Analog Inputs test (5 seconds) (values in volts)")
for i in range(10):
    print(str(myrio1.read_analog_input(0)) + " " + str(myrio1.read_analog_input(1)))
    time.sleep(0.5)
print("End of Analog Inputs test")
time.sleep(2)

# Test the analog output wiring it to AI2
print("myRIO analog output test - wire AO0 to AI2 and press the onboard button")

while not myrio1.read_button():
    time.sleep(0.1)

print("AO0 write: 5.0")
myrio1.write_analog_output(channel=0, value=5.0)
time.sleep(1)
print("AI2 read: ", str(myrio1.read_analog_input(channel=2)))
print("AO0 write: 2.5")
myrio1.write_analog_output(channel=0, value=2.5)
time.sleep(1)
print("AI2 read: ", str(myrio1.read_analog_input(channel=2)))
print("AO0 write: 0.0")
myrio1.write_analog_output(channel=0, value=0.0)
time.sleep(1)
print("AI2 read: ", str(myrio1.read_analog_input(channel=2)))
print("End of Analog Output test")
