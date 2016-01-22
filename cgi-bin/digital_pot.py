#! /usr/bin/python2.7

import spidev
import time
# connect and talk to the digital pot with spi
# datasheet:
# http://ww1.microchip.com/downloads/en/DeviceDoc/22060b.pdf
class digital_pot:

  # initialize the connection
  def __init__(self):
    self.spi = spidev.SpiDev()
    # this should use the second chip enable pin
    self.spi.open(0, 1)

    # according to the datasheet, driving with 2.7v or higher you can use 10mhz
    self.spi.max_speed_hz = 10000000

    self.reset()

  # set the device to a known state
  def reset(self):
    self.spi.writebytes([0,0])

  # set the resistance of the pot.
  # resistance is measured in ohms

  def setStep(self, num):
    self.spi.writebytes([0,num])
  # close the spi connection
  def close(self):
    self.spi.close()


# Test function
def main():
#  print 'running in test mode'
  dp = digital_pot()
#  for i in range(0, 33 ):
#    v = dp.setVoltage(.1*i)
#    print "Voltage: " + str(i/10.) + " Actual:" + str(v)
 #   time.sleep(1)
  dp.setStep(50)
  dp.close()

if(__name__ == "__main__"):
  main()
