""" Example of using threads to read different sensors and control outputs simultaneously.
    - When the black button is pressed, the green LED will light up.
    - When the temperature is above 25 degrees, the blue LED will light up.
    - When the brightness is above 90, the red LED will light up.
    - When the acceleration in any axis is above 1.4g, all the LEDs will light up until the white button is pressed.
    - The values are displayed in the terminal.
    - Press Ctrl+C to stop the program.
    
    This example is a great contribution by David Corrionero, 
    former student of the University of the Basque Country (UPV/EHU).
    Last updated: 2025/09/26
    """

import myrio_base
import threading
from time import sleep
import os

myrio1 = myrio_base.MyRIO()

def confirm_button():
    # When the black button is pressed, the green LED will light up.
    global confirm
    while True:
        if myrio1.read_digital_input(3, port="A"):
            confirm = True
            myrio1.write_digital_output(0,True)
            sleep(2)
            myrio1.write_digital_output(0,False)
        confirm = False

def measure_temperature():
    # When the temperature is above 25 degrees, the blue LED will light up.
    global temperature
    while True:
        myrio1.write_digital_output(2,False)
        temperature = myrio1.read_MXP_temperature()
        sleep(0.25)
        while temperature >= 25:
            myrio1.write_digital_output(2,True)
            sleep(0.25)
            temperature = myrio1.read_MXP_temperature()

def brightness_measurement():
    # When the brightness is above 90, the red LED will light up.
    global brightness
    while True:
        myrio1.write_digital_output(1,False)
        brightness = myrio1.read_MXP_luminosity()
        sleep(0.25)
        while brightness >= 90:
            myrio1.write_digital_output(1,True)
            sleep(0.25)
            brightness = myrio1.read_MXP_luminosity()

def HMI():
    while True:
        os.system('clear')
        print("Values:\n")
        print("Temperature:"+ str(temperature) +"C \n")
        print("Confirmation:" + ("Yes" if confirm else "No") + "\n")
        print("Acceleration: X="+str(x_value)+"Y="+ str(y_value)+"Z="+str(z_value)+"\n")
        print("Brightness:"+str(brightness)+"%\n")
        sleep(0.5)


for number in range(3): myrio1.write_digital_output(number,False) #Turn off all RGB colors
myrio1.write_leds_booleans([False,False,False,False])

thread1 = threading.Thread(target=confirm_button, daemon = True)
thread1.start()

thread2 = threading.Thread(target=measure_temperature, daemon = True)
thread2.start()

thread3 = threading.Thread(target=brightness_measurement, daemon = True)
thread3.start()

HMI = threading.Thread(target=HMI, daemon = True) # Forth thread configured and started
HMI.start()

while True:
    # Ctrl+C to stop the program
    x_value,y_value,z_value = myrio1.read_analog_accelerometer()
    if x_value > 1.4 or y_value > 1.4 or z_value > 1.4:
        #switch on all leds
        myrio1.write_leds_booleans([True,True,True,True])
        while not myrio1.read_digital_input(4, port="A"): #Wait until the white button is pressed
            sleep(0.1)
        #switch off all leds
        myrio1.write_leds_booleans([False,False,False,False])
    sleep(0.1)