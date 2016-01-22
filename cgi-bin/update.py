#! /usr/bin/python2.7

import cgi
import cgitb
import update_voltage_frequency

# create instance of field storage to get values
parameters = cgi.FieldStorage()

# get the data from the fields
#update_voltage = parameters.getvalue('update_voltage')
#update_frequency = parameters.getvalue('update_frequency')

voltage_value = parameters.getvalue('voltage')
frequency_value = parameters.getvalue('frequency')

# Update the frequency and voltage
update_voltage_frequency.update_voltage(voltage_value)
update_voltage_frequency.update_frequency(frequency_value)

# This script is designed to count as a test
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>CGI-Update-Procedure</title>"
print "<head>"
print "<body>"
print "<h1>Current Values:"
print "<h3>Voltage: %s V" % (voltage_value)
print "<h3>Frequency: %s Khz" % (frequency_value)
print "</body>"
print "</html>"

# Reprint index.html so that the user may change the voltage again
with open('/home/pi/senior_design/www/index.html', 'r') as file:
  line = file.readline()
  
  while line:
    #print "\""+line+"\""
    print line
    line = file.readline()
