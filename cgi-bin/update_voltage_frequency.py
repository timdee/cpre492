#! /usr/bin/python2.7

import spidev
import minigen
#import cPickle as pickle
#import pga
import subprocess
import math

#Designed to communicate with a Minigen connected to the GPIO pins
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

  # Test setting the frequency using spi
  #update_frequency(100)

  # Test setting the voltage using I2c
  update_voltage("22")

# define variables
#minigen_pickle_file = "/tmp/mini_pickle"
#digital_pot_pickle_file = "/tmp/pot_pickle"

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

  # range of each step fed into the summer
  # pga will have many steps between 0 -> step_range
  # ex: if max value of the pga is 10vpp, then step_range is 10
  # ADJUST STEP RANGE TO COSNTANT AMPLIFIER OUTPUT
  #step_range = 10
  #pga_step_size = step_range / 7.0

#  if ( pga_voltage > step_range ):  
#    state_0 = "1"
#    pga_voltage -= step_range
#  else:
#    state_0 = "0"
  
#  if ( pga_voltage > step_range ):  
#    state_1 = "1"
#    pga_voltage -= step_range
#  else:
#    state_1 = "0"

  # convert the pga voltage into a pga gain
  #pga_gain = pga_voltage / pga_step_size

  # debug: print out pga_voltage and states of pins
#  print str(pga_voltage)
 # print str(state_0)
  #print str(state_1)
#  print str(int(round(pga_gain)))

  #TEST PRINTS FOR 2 STAGE AMPLIFIER
  #print "pga_voltage " + str(pga_voltage)

  #print "pga_0_voltage " + str(pga_0_voltage)
  #print "pga_1_voltage " + str(pga_1_voltage)

  #print "pga_0_gain " + str(pga_0_gain)
  #print "pga_1_gain " + str(pga_1_gain)

  #print "pga_0_gain_script " + str(int(round(-1*pga_0_gain)))
  #print "pga_1_gain_script " + str(int(round(-1*pga_1_gain)))

  # call a script that will set the pga values
  # TODO be able to choose pga pins set based on this call
  subprocess.call("./pga_calling_script.bash " + str(int(round(-1*pga_0_gain))), shell=True)
  subprocess.call("./pga_calling_script.bash " + str(int(round(-1*pga_1_gain))), shell=True)

  # set switch 0
  #subprocess.call("./switch_calling_script.bash 0 " + state_0, shell=True)

  # set switch 1
  #subprocess.call("./switch_calling_script.bash 1 " + state_1, shell=True)

  #print 'voltage updated'

  # make an instance of the voltage_regulator class to handle the connection
  #vr = voltage_regulator.voltage_regulator()
  #vr = get_pickle_digital_pot()

  # ask vr to set the voltage to the given value
#  vr.set_voltage(voltage)

  # update pickled information
  ###set_pickle_digital_pot(vr)

  # preform cleanup actions
  #vr.close_regulator()

# Update the frequency to the specified value. Values are given in Khz.
def update_frequency(frequency):
  #print 'frequency updated'

  # make an instance of the minigen class to handle the connection
  m = minigen.minigen()
 # m = get_pickle_minigen()

  # ask the minigen to set the new frequency
  m.setFrequency(float(frequency)*1000)

  # update pickled information
  ###set_pickle_minigen(m)

  #close the conection
  m.close()

# attempt to grab pickeled information about minigen
# if no pickle is found, create new minigen object
#def get_pickle_minigen():
 # try:
   # m = pickle.load( open( minigen_pickle_file, "rb" ) )
    ##print "pickle loaded successfully"
  #except:
   # m = minigen.minigen()
    #print "new object created"

 # return m

# attempt to grab pickeled information about ditital pot
# if no pickle is found, create new minigen object
#def get_pickle_digital_pot():
#  try:
#    vr = pickle.load( open( digital_pot_pickle_file,  "rb" ) )
#  except:
#    vr = voltage_regulator.voltage_regulator()

#  return vr 

# set pickeled information about minigen
#def set_pickle_minigen(m):
#  pickle.dump( m, open(minigen_pickle_file , "wb" ) )

# set pickeled information about digital pot
#def set_pickle_digital_pot(vr):
#  pickle.dump( vr, open(digital_pot_pickle_file, "wb" ) )

if(__name__ == "__main__"):
  main()
