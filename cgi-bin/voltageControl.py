import digital_pot

class voltageControl:


	def __init__(self):

		self. digitalPot = digital_pot.digital_pot()

		#Upper and lower Bound of DigitalPot
		self.upperResistance = 9870.0
		self.lowerResistance = 164.0
		self.maxStep = 128

		#Amplifier Circuit
		self.rf = 10000 #6575
		self.maxVoltage = 20
		self.minVoltage = 0
		self.inputVoltage = 1




	def close(self):
		self.digitalPot.close()


	def setVoltage(self, voltage):
		step = int(((((self.rf*self.inputVoltage)/voltage)-self.lowerResistance) * self.maxStep)/(self.upperResistance - self.lowerResistance))
		print step
		if( step > self.maxStep):
				step = self.maxStep
		self.digitalPot.setStep(step)




def main():
#  print 'running in test mode'
	vC = voltageControl()
	vC.setVoltage(10)


if(__name__ == "__main__"):
	main()
