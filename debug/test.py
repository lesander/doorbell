#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

# listen to BCM 17 (physical pin 11)
pin = 17

# setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN)

# print the state of the pin every .1 second
try:
	while True:
		print(GPIO.input(pin))
		sleep(.1)

# cleanup when stopping
except KeyboardInterrupt:
	print('Cleaning up..')
	GPIO.cleanup()
