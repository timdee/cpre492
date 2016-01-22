#! /usr/bin/python2.7

import spidev
import minigen
import voltage_regulator
import cPickle as pickle

#Designed to communicate with a Minigen connected to the GPIO pins
spi = spidev.SpiDev()

# Test function
def main():
  print 'running in test mode'

  # Test setting the frequency using spi
  update_frequency(100)

  # Test setting the voltage using I2c
  update_voltage(5)

# define variables
minigen_pickle_file = "/tmp/mini_pickle"
digital_pot_pickle_file = "/tmp/pot_pickle"

# Update the voltage level to the specified value.
# This is not the voltage output by the minigen,
# Instead it is the voltage output by the circuit as a whole.
def update_voltage(voltage):
  pass
  #print 'voltage updated'

  # make an instance of the voltage_regulator class to handle the connection
  vr = voltage_regulator.voltage_regulator()
  vr = get_pickle_digital_pot()

  # ask vr to set the voltage to the given value
#  vr.set_voltage(voltage)

  # update pickled information
  ###set_pickle_digital_pot(vr)

  # preform cleanup actions
  vr.close_regulator()

# Update the frequency to the specified value. Values are given in Khz.
def update_frequency(frequency):
  #print 'frequency updated'

  # make an instance of the minigen class to handle the connection
  #m = minigen.minigen()
  m = get_pickle_minigen()

  # ask the minigen to set the new frequency
  #m.set_frequency(frequency)

  # update pickled information
  ###set_pickle_minigen(m)

  #close the conection
  m.close_connection()

# attempt to grab pickeled information about minigen
# if no pickle is found, create new minigen object
def get_pickle_minigen():
  try:
    m = pickle.load( open( minigen_pickle_file, "rb" ) )
    #print "pickle loaded successfully"
  except:
    m = minigen.minigen()
    #print "new object created"

  return m

# attempt to grab pickeled information about ditital pot
# if no pickle is found, create new minigen object
def get_pickle_digital_pot():
  try:
    vr = pickle.load( open( digital_pot_pickle_file,  "rb" ) )
  except:
    vr = voltage_regulator.voltage_regulator()

  return vr 

# set pickeled information about minigen
def set_pickle_minigen(m):
  pickle.dump( m, open(minigen_pickle_file , "wb" ) )

# set pickeled information about digital pot
def set_pickle_digital_pot(vr):
  pickle.dump( vr, open(digital_pot_pickle_file, "wb" ) )

if(__name__ == "__main__"):
  main()
