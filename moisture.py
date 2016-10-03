#!/usr/bin/python

# Start by importing the libraries we want to use

import RPi.GPIO as GPIO 		# This is the GPIO library we need to use the GPIO pins on the Raspberry Pi
import time 				# This is the time library, we need this so we can use the sleep function

# This is our callback function, this function will be called every time there is a change on the specified GPIO channel, in this example we are using 17
def callback(channel):  
	if GPIO.input(channel):
		print "LED off"
	else:
		print "LED on"

# Set our GPIO numbering to BCM
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin that we have our digital output from our sensor connected to
channel = 17
# Set the GPIO pin to an input
GPIO.setup(channel, GPIO.IN)

# This line tells our script to keep an eye on our gpio pin and let us know when the pin goes HIGH or LOW
GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)

# This line asigns a function to the GPIO pin so that when the above line tells us there is a change on the pin, run this function
GPIO.add_event_callback(channel, callback)

while True:
	time.sleep(0.1)
