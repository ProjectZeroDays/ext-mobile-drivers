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
import scrollphathd


def usage():
    print("Usage: {} <cache-file> <pixel> <row> <brightness>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 5:
    usage()

try:
    pixel, row, brightness = [int(x) for x in sys.argv[2:]]
except ValueError:
    usage()

if pixel > scrollphathd.width:
    usage()

if row > scrollphathd.height:
    usage()


# either read the cache file or initialize cache with all pixels off
fname = sys.argv[1]
if os.path.isfile(fname):
    with open(fname) as f:
        grid = json.load(f)
else:
    grid = [[0] * scrollphathd.width for i in range(scrollphathd.height)]

scrollphathd.set_clear_on_exit(False)
scrollphathd.set_brightness(0.5)
scrollphathd.clear()

# restore pixel states from cache file
for x in range(scrollphathd.width):
   for y in range(scrollphathd.height):
        scrollphathd.set_pixel(x, y, grid[y][x] / 10.0)

scrollphathd.set_pixel(pixel, row, brightness / 10.0)
scrollphathd.show()

# push the changed pixel to cache and save it
grid[row][pixel] = brightness
with open(fname, 'w') as outfile:
    json.dump(grid, outfile)
