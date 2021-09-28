#!/usr/bin/env python
#
'''
## License

The MIT License (MIT)

Copyright (c) 2021 Tomasz Klim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import sys
import json
import time
import random
import os.path
from neopixel import *


# LED strip configuration:
LED_COUNT      = 32      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 10      # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


def usage():
    print("Usage: {} <cache-file> <pixel> <r:0-255> <g:0-255> <b:0-255>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 6:
    usage()

try:
    pixel, r, g, b = [int(x) for x in sys.argv[2:]]
except ValueError:
    usage()

if max(r, g, b) > 255:
    usage()

if pixel > LED_COUNT - 1:
    usage()


# either read the cache file or initialize cache with all pixels off
fname = sys.argv[1]
if os.path.isfile(fname):
    with open(fname) as f:
        pixels = json.load(f)
else:
    pixels = [[0, 0, 0]] * LED_COUNT

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

# restore pixel states from cache file
for x in range(0, strip.numPixels()):
	strip.setPixelColor(x, Color(pixels[x][1], pixels[x][0], pixels[x][2]))

# there's a bug somewhere in the driver - the real order of colors to pass here is G-R-B instead of R-G-B
strip.setPixelColor(pixel, Color(g, r, b))
strip.show()

# push the changed pixel to cache and save it
pixels[pixel] = [r & 0xff, g & 0xff, b & 0xff]
with open(fname, 'w') as outfile:
    json.dump(pixels, outfile)
