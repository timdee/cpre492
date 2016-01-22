# Description of functionality
These scripts update the voltage and frequency output of the circuit. They do this by communicating with a Sparkfun Minigen and digital potentiometers.

The communication for both the Minigen and the pots is implemented in the python classes contained in minigen.py and digital_pot.py respectively.

Because of the possibility of multiple pots, setting the voltage is done by the voltage_regulator class. This class uses a number of digital_pot's.

The web server calls the update.py script, providing the requested voltage and frequency values.

udate.py calls functions in update_voltage_frequency.py to begin the update process for frequency and voltage.

update_voltage_frequency creates instances of minigen class to update frequency.
update_voltage_frequency creates instances of voltage_regulator to update voltage.

minigen class uses spidev library to communicate with the minigen.

voltage_regulator class uses instances of digital_pot to control the digital potentiometers.

digital_pot class uses spidev library to communicate with the digital potentiometers.

# Digital pot data sheet information
### Digital potiemeter MCP 4131
Datasheet:
http://ww1.microchip.com/downloads/en/DeviceDoc/22060b.pdf

Arduino Library:
https://github.com/jmalloc/arduino-mcp4xxx

I think spidev idles low. Pot has SPI modes 0,0 and 1,1. The distinction between the modes is one idles low and the other idles high. We will use mode 0,0.




# Class Layout

--------------
- web server -
--------------
|
|
update.py
  |
  |
  update_voltage_frequency.py
    |                 |
    |                 |
    minigen.py        voltage_regulator.py
                        |
                        |
                        digital_pot.py