#! /usr/bin/python2.7

import spidev
import time

spi = spidev.SpiDev()

# open(bus, device)
spi.open(0, 0)

# minigen is driven at 40Mhz
#spi.max_speed_hz = 40000000
spi.max_speed_hz = 10000000

# reset all registers to zero in the minigen
print 'reset'
spi.writebytes([0x01,0x00])
time.sleep(1)
spi.writebytes([0x00, 0x00])
time.sleep(1)

# set config register ( sine wave, phase register 0, frequency register 0, adjust freq mode full )
#spi.writebytes([0x20, 0x00])
time.sleep(1)

# set phase register ( phase reg 0 = 0)
spi.writebytes([0xC0, 0x00])
print 'set phase register'
time.sleep(1)

# set frequency register
print 'set frequency'
#while True:
#  spi.writebytes([0x40,0x00,0x00,0x00])
  #spi.writebytes([0x40,0x00])
  #spi.writebytes([0x00,0x00])

# LSB -> MSB
#spi.writebytes([0x4F,0x5C,0x40,0x0A])

# LSB
spi.writebytes([0x4F,0x5C])
# MSB
spi.writebytes([0x40,0x0A])

# at the END close the connection
spi.close()
