#! /usr/bin/python2.7

import RPi.GPIO as GPIO
import time
import os

class pga:

	def __init__(self):
		#Switch user
		#sudoPassword = 'root'
		#command = 'sudo -i'
		#p = os.system('echo %s|sudo -S %s' % (sudoPassword, command))

		#Default Gx pins
		self.pinGx = [4, 17, 27]
		
		#6910-3
		#self.gainList = [0, -1, -2, -3, -4, -5, -6, -7]

		#6910-2
		#self.gaintList = [0, -1, -2, -4, -8, -16, -32, -64]

		#6910-3
		self.gainList = [0, -1, -2, -5, -10, -20, -50, -100]


		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.updatePins()
		

	def updatePins(self):
		GPIO.cleanup()
		for pos in range(0,3):
			GPIO.setup(self.pinGx[pos], GPIO.OUT)

	def setPinG0(self, pin):
		self.pinGx[0] = pin
		self.updatePins()

	def setPinG1(self, pin):
		self.pinGx[1]= pin
		self.updatePins()

	def setPinG2(self, pin):
		self.pinGx[2] = pin
		self.updatePins()
	
	def setGainList(self, list):
		if(len(list) == 8):
			self.gainList = list
			return True
		return False

	def getGainList(self):
		return self.gainList

	def printGainList(self):
		print self.gainList


	def setGain(self, gain):
		try:
			binNum = '{:03b}'.format(self.gainList.index(gain))
			#print binNum
			binNum = binNum[::-1]
			for pos in range(0, 3):
				if int(binNum[pos]) == 1:
					GPIO.output(self.pinGx[pos], 1)
				else:
					GPIO.output(self.pinGx[pos], 0)
		except ValueError:
			print "Gain not Found"
			

def main():
	print "Running PGA test"
	p = pga()
	p.setGain(0)


 #self.gainList = [0, -1, -2, -5, -10, -20, -50, -100]
if(__name__ == "__main__"):
	main()
