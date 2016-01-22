#! /usr/bin/python2.7

import digital_pot

# This script adjusts the gpio pins to communicate 
# with the variable resistors, adjusting them to produce the voltage we want
# ment to abstract away the communication with variable resistors
#
# uses the digital_pot class to communicate with the digital pots
class voltage_regulator:
  # initialize the connection
  def __init__(self):
    self.op0_r0 = 0
    self.op0_r1 = 1
    #self.op1_r0 = 0
    #self.op1_r1 = 1

  # variable resistors will use spi as well
  def set_voltage(self, voltage):
    # compute the resistor values
    self.compute_resistor_values(voltage)

    # set the variable resistor value
    #TODO use the digital_pot class

  # given the desired voltage, compute the necessary resistor values
  #
  # Vout = Vin(1 + (opx_r1/opx_r0))
  #
  # The above transfter function is for a single op amp
  # Vin is 1vpp from signal generator
  def compute_resistor_values(self, voltage):
    # fix r1 so there is only one variable
    self.op0_r1 = 1000

    # compute r1
    # function solved for r1
    # 
    # opx_r0 = (Vin(opx_r1))/(Vout - Vin)
    self.op0_r0 = self.op0_r1/(voltage -1)

  # print out the calculated resistor values
  def print_resistor_values(self):
    print "resistor op0_r0: " + str(self.op0_r0)
    print "resistor op0_r1: " + str(self.op0_r1)

  # preform any cleanup actions (most likly closing i2c connection)
  def close_regulator(self):
    pass


# Test function
def main():
  print 'running in test mode'
  vr = voltage_regulator()

  vr.set_voltage(10)
  vr.print_resistor_values()

if(__name__ == "__main__"):
  main()
