# -----------------------------------------------------------------------------
# CircuitPython library for the LM75A temperature sensor
#
# Website: https://github.com/bablokb/circuitpython-lm75a
#
# -----------------------------------------------------------------------------

import board
import busio
import time
from adafruit_bus_device.i2c_device import I2CDevice

class LM75A(object):
  # LM75A default address
  ADDRESS = 0x48

  # --- constructor   --------------------------------------------------------
  
  def __init__(self,i2c=None,address=ADDRESS):
    if i2c is None:
      i2c = busio.I2C(board.SCL,board.SDA)
    self._device = I2CDevice(i2c,address)

  # --- compute the 2's complement of int value   ----------------------------

  def _twos_comp(self,val,bits):
    """compute the 2's complement of int value val"""
    if (val & (1 << (bits - 1))):      # if sign bit is set e.g., 8bit: 128-255
      val = val - (1 << bits)          # compute negative value
    return val                         # return positive value as is

  # --- read temp-bytes from the device   ------------------------------------

  def _get_temp_bytes(self):
    buf = bytearray(2)
    with self._device:
      self._device.readinto(buf)     # this assumes the pointer-reg is correct
    return buf

  # --- return (converted) temperature   --------------------------------------

  def get_temp(self):
    [t_high,t_low] = self._get_temp_bytes()
    fraction = 0.5*(t_low >> 7)                    # bit7==1: 0.5, else 0.0
    return self._twos_comp(t_high,8) + fraction
