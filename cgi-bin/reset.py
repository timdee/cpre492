#! /usr/bin/python2.7

# TODO the purpose of this script is to reset the minigen to a default state


# This script is designed to count as a test
print "Content-type:text/html\r\n\r\n"
print "<html>"
print "<head>"
print "<title>Reset-Procedure</title>"
print "<head>"
print "<body>"
print "</body>"
print "</html>"

# reprint index.html
with open('/home/pi/senior_design/www/index.html', 'r') as file:
  line = file.readline()
  
  while line:
    #print "\""+line+"\""
    print line
    line = file.readline()
