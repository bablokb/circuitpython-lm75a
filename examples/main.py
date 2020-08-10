#!/usr/bin/python3
# -----------------------------------------------------------------------------
# CircuitPython library for the LM75A
#
# Sample code
#
# Website: https://github.com/bablokb/circuitpython-lm75a
#
# -----------------------------------------------------------------------------

import time
import lm75a

sensor = lm75a.LM75A()      # this uses the default address 0x48

while True:
  print("reading temperature... ",end="")
  temp = sensor.get_temp()
  print("%4.1f" % temp)
  time.sleep(2)
