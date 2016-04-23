#! /usr/bin/python2.7

import cgi
import cgitb
import update_voltage_frequency

def print_file(file_name):
    with open(file_name, 'r') as file:
        line = file.readline()
      
        while line:
            #print "\""+line+"\""
            print line
            line = file.readline()
            
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
#print "<html>"
#print "<head>"
#print "<title>CGI-Update-Procedure</title>"
#print "<head>"
#print "<body>"
#print "<h1>Current Values:</h1>"
#print "<h3>Voltage: %s V</h3>" % (voltage_value)
#print "<h3>Frequency: %s Khz</h3>" % (frequency_value)
#print "</body>"
#print "</html>"

# print out css to be applied
print '<link href="/html/css/bootstrap.min.css" rel="stylesheet" type="text/css">'
print '<link href="/html/css/bootstrap-theme.min.css" rel="stylesheet" type="text/css">'
#print_file('/home/pi/cpre492/www/html/css/bootstrap.min.css')
#print_file('/home/pi/cpre492/www/html/css/bootstrap-theme.min.css')

# Reprint index.html so that the user may change the voltage again
print_file('/home/pi/cpre492/www/html/index.html')
        
