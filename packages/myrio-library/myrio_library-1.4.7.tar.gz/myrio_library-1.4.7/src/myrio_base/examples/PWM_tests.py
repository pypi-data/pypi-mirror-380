"""Usage examples of the MyRIO class: PWM tests

This examples show how to use the PWM output of the myRIO.

Our MXP cards have an RGB LED connected to DIO_2:0, so we
could not use this LED for the test. We have connected an
RGB LED wired to the B port (pins 27, 29, 31) for our examples.

Last update: 2024/04/12 Aitzol Ezeiza Ramos (UPV/EHU)
"""

import myrio_base as myRIO
from time import sleep

myrio1 = myRIO.MyRIO()

# Test the PWM outputs
print("PWM output test (port B: PWM0, PWM1, PWM2):")
print("Configuring...")
X_0 = myrio1.config_PWM_output(channel=0, frequency=5000, port="B")
X_1 = myrio1.config_PWM_output(channel=1, port="B")
X_2 = myrio1.config_PWM_output(channel=2, port="B")
print("20% 20% 20%")
myrio1.write_PWM_output(channel=0, duty_cycle=20, X=X_0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=20, X=X_1, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=20, X=X_2, port="B")
sleep(2)
print("80% 40% 10%")
myrio1.write_PWM_output(channel=0, duty_cycle=80, X=X_0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=40, X=X_1, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=10, X=X_2, port="B")
sleep(2)
print("0% 40% 0%")
myrio1.write_PWM_output(channel=0, duty_cycle=0, X=X_0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=40, X=X_1, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=0, X=X_2, port="B")
sleep(2)
print("100% 0% 0%")
myrio1.write_PWM_output(channel=0, duty_cycle=100, X=X_0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=0, X=X_1, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=0, X=X_2, port="B")
sleep(2)
print("10% 45% 11,5%")
myrio1.write_PWM_output(channel=0, duty_cycle=10, X=X_0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=45, X=X_1, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=11.5, X=X_2, port="B")
sleep(2)

print("0% 0% 0%")
myrio1.write_PWM_output(channel=0, duty_cycle=0.0, port="B")
myrio1.write_PWM_output(channel=1, duty_cycle=0.0, port="B")
myrio1.write_PWM_output(channel=2, duty_cycle=0.0, port="B")

print("Display RGB color orange (252, 161, 3):")
myrio1.display_color_PWM(252, 161, 3)
sleep(2)
print("Display RGB color silver (192, 192, 192):")
myrio1.display_color_PWM(192, 192, 192)
sleep(2)
print("Display RGB color purple (128, 0, 128):")
myrio1.display_color_PWM(128, 0, 128)
sleep(2)
myrio1.display_color_PWM(0, 0, 0)
