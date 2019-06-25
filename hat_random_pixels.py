#!/usr/bin/env python
from sense_hat import SenseHat
sense = SenseHat()
import random
import time

r = random.randint(0,7)
x = random.randint(0, 255)
y = random.randint(0, 255)
z = random.randint(0, 255)
sense.set_pixel(r, r (x, y, z)
time.sleep(1)
sense.clear()
