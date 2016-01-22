#! /usr/bin/python2.7

import spidev
import time

# Designed to provide some of the functionality from SparkFun_MiniGen.cpp
# designed so that you only need to use set_frequency to set the frequency
class minigen:
  # initialize the connection with the minigen
	def __init__(self):
		self.spi = spidev.SpiDev()

		# open(bus, device)
		self.spi.open(0, 0)

		# minigen is driven at 40Mhz
		#self.spi.max_speed_hz = 15000000

		self.controlReg = [False]* 16
		self.controlReg[16-13] = True 

		self.freqReg0 = [False]*32
		self.freqReg1 = [False]*32

		self.freqReg0[31-30] = True
		self.freqReg0[31-14] = True
 
		self.freqReg1[31-31] = True
		self.freqReg1[31-15] = True

		self.fudgeFactor = 1

##########      Control Register 16Bits
#		Bit Number		Name		Function
#		D15					Addr1			Always 0				D15 and D14 is the address of the control register
#		D14					Addr0			Always 0	
#		D13					B28				When 1: allows a complete word to be loaded into a freq reg with two consecutive write. First contains 14 LSB, second contains
#													14 MSB. (First two bits is freq reg addr)  Consecutive writes to the same freq register is not allowed, you must alternate.
#													When 0: Configures the 28bit freq reg is act as two 14 bit regs. One contains 14 LSB, the other 14MSB. This allows for coarse, or fine
#													grain tuning. HLB defines which to change.
#													
#
#
#		D12					HLB				This allows the user to continiously load the MSB or LSB of a freq reg. Ignoring ther other 14 bits. When B28 = 1, this is ignored.
#													When 1: Allows write to 14 MSB
#													When 0: Allows write to 14 LSB
#
#
#
#		D11					FSEL			Selects either freq0 or freq1
#		D10					PSEL			Selects either phase0 or phase1 
#		D09				reserved			0
#		D08				RESET			When 1: resets internal regs to 0. When 0: disables the reset function.
#		D07				Sleep1			Enables or disables MCLK
#		D06				Sleep12			Powers down on chip DAC
#		D05				OPBITEN			0
#		D04										0
#		D03
#		D02					TODO
#		D01
#		D00

	def chooseFreq0(self):
		self.controlReg[15-11] = False
	def chooseFreq1(self):
		self.controlReg[15-11] = True
	def enableB28(self):
		self.controlReg[15-13] = True
	def disableB28(self):
		self.controlReg[15-13] = False
	def enableHLB(self):
		self.controlReg[15-12] = True
	def disableHLB(self):
		self.controlReg[15-12] = False

	def sendControlReg(self):
		controlRegNum = self.boolListToInteger(self.controlReg)
		self.spi.xfer([controlRegNum >> 8, controlRegNum & 0xFF])
	
	def getControlReg(self):
		return (self.boolListToInteger(self.controlReg))


	#Frequency Functions
	#
	#Frequency Registers are set up as one 1 32bit register with [31-30] and [15-14] defined to be the address 
	#

	def setFreqRegister(self,freqReg, isMSB, num):
		if(num >  0x3FFF):
			return -1
		bitString = bin(num)[2:][::-1]
		if(isMSB == 1):
			x = 15
		else:
			x = 31
		for i in bitString:
			if int(i) == 1:
				if(freqReg == 0):
					self.freqReg0[x] = True
				else:
					self.freqReg1[x] = True
			else:
				if(freqReg == 0):
					self.freqReg0[x] = False
				else:
					self.freqReg1[x] = False
			x= x - 1
		return 1


	def setFreq0MSB(self,num):
		return self.setFreqRegister(0,1,num)

	def setFreq0LSB(self,num):
		return self.setFreqRegister(0,0,num)

	def setFreq1MSB(self,num):
		return self.setFreqRegister(1,1,num)

	def setFreq1LSB(self,num):
		return self.setFreqRegister(1,0,num)

	def setEntireFreqReg0(self,num):
		actualValue = self.calculateFrequency(num)
		if(actualValue > 0x3FFFFFFF):
			return -1
		self.setFreq0LSB(actualValue & 0x3FFF)
		self.setFreq0MSB(actualValue >> 14)
		return 1

	def setEntireFreqReg1(self,num):
		actualValue = self.calculateFrequency(num)
		if(actualValue > 0x3FFFFFFF):
			return -1
		self.setFreq1LSB(actualValue & 0x3FFF)
		self.setFreq1MSB(actualValue >> 14)
		return 1		


	def getFreqReg0(self):
		return (self.boolListToInteger(self.freqReg0))
	def getFreqReg1(self):
		return (self.boolListToInteger(self.freqReg1))

	def sendFreqReg0MSB(self):
		sendFreqRegNum = self.boolListToInteger(self.freqReg0)
		self.spi.xfer([sendFreqRegNum >> 24, (sendFreqRegNum >> 16) & 0xFF])

	def sendFreqReg0LSB(self):
		sendFreqRegNum = self.boolListToInteger(self.freqReg0)
		self.spi.xfer([(sendFreqRegNum >> 8) & 0xFF, (sendFreqRegNum) & 0xFF])

	def sendFreqReg1MSB(self):
		sendFreqRegNum = self.boolListToInteger(self.freqReg1)
		self.spi.xfer([sendFreqRegNum >> 24, (sendFreqRegNum >> 16) & 0xFF])

	def sendFreqReg1LSB(self):
		sendFreqRegNum = self.boolListToInteger(self.freqReg1)
		self.spi.xfer([(sendFreqRegNum >> 8) & 0xFF, (sendFreqRegNum) & 0xFF])

	def setFrequency(self, freq):
		if(freq < 10000):
			return -1
		self.enableB28()
		self.chooseFreq1()
		self.sendControlReg()
		self.setEntireFreqReg0(freq)
		self.sendFreqReg0MSB()
		self.sendFreqReg0LSB()
		self.chooseFreq0()
		self.sendControlReg()
		return 1

	def setFrequency1(self, freq):
		self.disableB28()
		self.enableHLB()
		self.chooseFreq1()
		self.sendControlReg()

		calculatedValue = self.calculateFrequency(freq)
		if(calculatedValue > 0x3FFF):
			return -1

		MSB = (calculatedValue >> 14) & 0x3FFF
		self.setFreqRegister(0, 1, MSB)
		self.sendFreqReg0MSB()
		self.disableHLB()
		self.sendControlReg()
		LSB = calculatedValue & 0x3FFF
		self.setFreqRegister(0,0,LSB)
		self.sendFreqReg0LSB()
		
		self.chooseFreq0()
		self.sendControlReg()

	def calculateFrequency(self, num):
		#print "Calculated Value: " + str(int(num/(.0596)))*self.fudgeFactor
		return int(num/(.0596))*self.fudgeFactor

	def close(self):
		self.spi.close()	

	#Converts a boolean array to a number
	def boolListToInteger(self,lst):
		return int( ''.join(['1' if x else '0' for x in lst]),2)

# Test function
def main():
	print 'running in test mode'
	m = minigen()
	
#	for i in range(0 ,2):
#		for j in range(1,10):
#			m.setFrequency( 10000*j*(10**i))
#			print str( 10000*j*(10**i)) + " hz"
#			time.sleep(1)

	m.setFrequency(100000)
	print "Frequency Register: " + bin(m.getFreqReg0())
	m.close()


if(__name__ == "__main__"):
	main()
