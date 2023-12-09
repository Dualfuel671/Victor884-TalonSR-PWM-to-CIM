'''
Author : Bruce Jackson
Purpose : Control a Victor884 or TalonSR
Language : MicroPython
Harware : ESP8266, ESP12, motor controller
Note-save this program as 'main.py' on the controller so it will start without the computer.
'''
#The machine module is specific to the ESP8266
import machine

'''
The time module provides functions for getting 
1. the current date and time
2. for sleeping
'''
import time

from time import sleep

'''
class Pin - Control I/O pins
The pin class has methods
1. to set the mode of pin (IN, OUT)
2. to get and set the digital logic level
'''
from machine import Pin, PWM

# Its important to use Digital Input and Output (DIO)pin 12 on the Wemos D1 R1 board. DIO pin 2 is the builtinLED 
# DIO(2) didn't work
p12 = machine.Pin(12)
# configure PWM on pin p2
pwm12 = machine.PWM(p12)
# set the PWM frequency as 50Hz
# the TalonSR accepts different frequencies...TODO, find out which is best.
pwm12.freq(50)

while True:
    for d in range(50,100,1):
        # set the duty cycle to d .i.e. 50 through 100 with step of 1
        # at 75% duty cycle the motor rotation reverses direction
        # at 50% its going fastest in reverse
        # at 100% its going fastest forwards
        pwm12.duty(d)
        tSleep = (d/1023)*20
        # time.sleep provides the time increments that the motor stays on a particular duty cycle
        time.sleep(tSleep)
        #print the pwm details like pin, freq, duty cycle
        print (pwm12)
    time.sleep(2)
