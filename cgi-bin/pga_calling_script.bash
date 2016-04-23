#! /bin/bash

# open python thing
cd /home/pi/cpre492/cgi-bin

echo -e "import pga\np_amp=pga.pga($2, $3, $4)\np_amp.setGain($1)" | sudo python
#sudo python import pga
#sudo python p_amp = pga.pga($2, $3, $4)
#sudo python p_amp.setGain(-1)
