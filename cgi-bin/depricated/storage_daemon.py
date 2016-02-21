#! /usr/bin/python2.7

import daemon
import time
import sys

# this script will start a daemon used to store minigen object and digital pot object
# somehow to need to be able to
#   set -- minigen and digital pot object
#   get -- minigen and digital pot object:
print "Storage Daemon Running"

context = daemon.DaemonContext(stdout=sys.stdout)
pipe = ""

with context:
  print "a\n"
  time.sleep(5)
