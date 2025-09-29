"""Usage examples of the MyRIO class: digital inputs and outputs

This examples show how to use the DIO ports and the
onboard button and LEDs.

We have a set of myRIOs in our facilities that we complement
with some MXP cards. These cards have an RGB LED connected to
DIO_2:0 and two push buttons on DIO_4:3. We use these channels
in our examples. The port that we use most is the A port, so
we set it as default on our package.

Last update: 2024/03/07 Aitzol Ezeiza Ramos (UPV/EHU)
"""

import myrio_base
import time

myrio1 = myrio_base.MyRIO()

# Read digital port (the whole port), one channel, and the onboard button

print("Digital port A:")
print(myrio1.read_digital_port(port="A"))
print("Digital channel 3, port A:")
print(myrio1.read_digital_input(3, port="A"))
print("onboard button:")
print(myrio1.read_button())

# Write onboard LEDs, using an integer and using a list of Booleans

print("Switching on the onboard LEDS (15 in binary)")
myrio1.write_leds_integer(7)
time.sleep(2)
print("Switching off the onboard LEDS (0 in binary)")
myrio1.write_leds_integer(0)
time.sleep(2)
print("Switching on the onboard LEDS 1 and 4 ([True, False, False, True])")
myrio1.write_leds_booleans([True, False, False, True])
time.sleep(2)
print("Switching off all the onboard LEDS ([False, False, False, False])")
myrio1.write_leds_booleans([False, False, False, False])
time.sleep(2)

# myRIO digital output test (the whole port at once, and then one by one)

print("Switching on the three RGB LEDS (7 in binary)")
myrio1.write_digital_port(7)
time.sleep(2)
print("Switching off the three RGB LEDS and all the other outputs (0,0 in binary)")
myrio1.write_digital_port(0, 0)
time.sleep(2)

print("Switching on the green LED (channel 0)")
myrio1.write_digital_output(0, True)
time.sleep(1)
print("Switching on the red LED (channel 1)")
myrio1.write_digital_output(1, True)
time.sleep(1)
print("Switching on the blue LED (channel 2)")
myrio1.write_digital_output(2, True)
time.sleep(1)

print("Switching off the three RGB LEDS one by one")
myrio1.write_digital_output(0, False)
time.sleep(1)
myrio1.write_digital_output(1, False)
time.sleep(1)
myrio1.write_digital_output(2, False)
time.sleep(1)

print("One color at a time (3 reps)")
for i in range(3):
    myrio1.write_digital_port(myrio_base.RED)
    time.sleep(1)
    myrio1.write_digital_port(myrio_base.GREEN)
    time.sleep(1)
    myrio1.write_digital_port(myrio_base.BLUE)
    time.sleep(1)

print("End of digital tests")
myrio1.write_digital_port(myrio_base.RGB_OFF)
