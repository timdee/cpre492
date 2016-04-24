#! /usr/bin/python2.7

import spidev
import minigen
import subprocess
import math

#Designed to communicate with a Minigen connected to the GPIO pins
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

  # Test setting the frequency using spi
  update_frequency(30)

  # Test setting the voltage
  update_voltage("3")

# Update the voltage level to the specified value.
# This is not the voltage output by the minigen,
# Instead it is the voltage output by the circuit as a whole.
def update_voltage(voltage):  
  # determine the values for the two pga's based on the voltage
  # pga_0 has amplifier of 7.5 gain after it
  # pga_1 has amplifier of 1 gain after it
  amp_gain_0 = 7.5;
  amp_gain_1 = 1.0;

  # compute voltage values
  pga_voltage = int(voltage)

  # pga voltages
  pga_0_gain = math.floor(pga_voltage / amp_gain_0);
  pga_1_voltage = pga_voltage - pga_0_gain * amp_gain_0;

  # pga gains
  #pga_0_gain = pga_0_voltage / amp_gain_0;
  pga_1_gain = pga_1_voltage / amp_gain_1;

  #TEST PRINTS FOR 2 STAGE AMPLIFIER
  #print "pga_voltage " + str(pga_voltage)

  #print "pga_0_voltage " + str(pga_0_voltage)
  #print "pga_1_voltage " + str(pga_1_voltage)

  #print "pga_0_gain " + str(pga_0_gain)
  #print "pga_1_gain " + str(pga_1_gain)

  #print "pga_0_gain_script " + str(int(round(-1*pga_0_gain)))
  #print "pga_1_gain_script " + str(int(round(-1*pga_1_gain)))

  # call a script that will set the pga values
  # be able to choose pga pins set based on this call
  subprocess.call("./pga_calling_script.bash " + str(int(round(-1*pga_0_gain))) + " 5 6 13", shell=True)
  subprocess.call("./pga_calling_script.bash " + str(int(round(-1*pga_1_gain))) + " 4 17 27", shell=True)

# Update the frequency to the specified value. Values are given in Khz.
def update_frequency(frequency):
  # make an instance of the minigen class to handle the connection
  m = minigen.minigen()

  # ask the minigen to set the new frequency
  m.setFrequency(float(frequency)*1000)

  #close the conection
  m.close()

if(__name__ == "__main__"):
  main()
