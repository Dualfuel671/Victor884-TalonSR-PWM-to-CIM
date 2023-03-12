# Victor884-TalonSR-PWM-to-CIM

!(/home/dualfuel/Downloads/WemosD1R1.jpg)

/home/dualfuel/Downloads/TalonSR.jpg

/home/dualfuel/Downloads/CIM.jpg

/home/dualfuel/Downloads/GroveShield.jpg

/home/dualfuel/Downloads/Victor884.jpg

What would appear to be a simple task, namely wiring a Wemos D1 to a Victor884 or TalonSR and running a simple brush motor, is fraught with little 
annoying details.

The Wemos D1

It can be coded with a variety of IDEs but by far the least costly in terms of processor speed and internet data, was the Thonny IDE for Python.
I used Thonny with Ubuntu 20.4 and a processor speed of 1.277GHz (AMD A8). Neither VS Code, nor Arduino IDE (v.2) worked well enough with the old A8 to 
be productive (too laggy).

The Grove Shield

These fit over the Wemos D1 R1 or the Arduino Uno. They are fantastic for attaching Grove connectors to. The Grove connectors do not fall off like 
the wires on the pin headers.

https://www.digikey.com/en/products/detail/seeed-technology-co.,-ltd/103030000/5488134?utm_adgroup=Seeed%20Technology%20Co.%2C%20LTD.&utm_source=google&utm_medium=cpc&utm_campaign=Shopping_DK%2BSupplier_Tier%201%20-%20Block%202&utm_term=&utm_content=Seeed%20Technology%20Co.%2C%20LTD.&gclid=Cj0KCQiAjbagBhD3ARIsANRrqEtRQX1r860BYjomDfTjcAhNfRAnPfUNsjPHASJR2ibVgPuiq9bLNvkaAhdGEALw_wcB

The Victor884 and the TalonSR

I didn't bother to calibrate either controller for this iteration. The really super important thing was to make sure the PWM wires are seated properly.
The connector pins can easily be go in the wrong location if using individual test leads. Its best to invest in the quality 3 wire connectors that the 
robot teams use.
Controllers with power will flash orange LEDs when they have no PWM signal. When they have signal, flashing red is backwards direction, and green flashing 
is forwards direction. Solid orange is 75% duty cycle and the motor is in neutral.

The CIM motor

This is the First Robotics workhorse motor. Its a brush motor. Its heavy, not as effcient, and not really as desirable for competition anymore. The CIM
is perfect for experimental work, and is nearly indestructable. It provides roughly a 1/2hp, so it can actually do some work.
