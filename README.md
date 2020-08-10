CircuitPython library for the LM75A temperature sensor
======================================================

A very (very!) basic implementation of the LM75A protocol. In fact,
the only thing you can currently do is read the temperature,
assuming you did not read/write the configuration register
before.

Implementing the remaining commands is more or less trivial, but
currently I have no need for that. Pull requests are of course
welcome.


Installation
------------

Just copy the file `lib/lm75a.py` to the lib-directory of your device.

You also need the `busio`-library from the CircuitPython library-bundle.


API
---

The API is very simple:

  - `lm75a(i2c=None,address=0x48)`: constructor
  - `get_temp()`: query the current temperatur (in °C)

There is a simple example in the `examples`-directory.
