#! /usr/bin/python2.7

import RPi.GPIO as GPIO
import time
import os
import sys

# GPIO pins
# physical pin 14 => GPIO22
# physical pin 16 => GPIO23
class switch:

	def __init__(self, switchNumber):
		# Default Gx pins
		self.pinGx = [22, 23]

		# switchNumber is either 0 or 1
		self.switchNumber = switchNumber;

		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.updatePins()

	def updatePins(self):
		GPIO.cleanup()
		GPIO.setmode(GPIO.BCM)
		
		for pos in range(0,2):
			GPIO.setup(self.pinGx[pos], GPIO.OUT)

	# Only Allows for gains set in the given list 
	def setState(self, state):
		# if 0, set 0. If any other value, set 1
		if(state == 0):
			self.pinGx[self.switchNumber] = 0
		else:
			self.pinGx[self.switchNumber] = 1
			
		self.updatePins()

def main():
	print "Running Switch Test"
	s = switch(int(sys.argv[1]))
	s.setState(int(sys.argv[2]))

if(__name__ == "__main__"):
	main()
