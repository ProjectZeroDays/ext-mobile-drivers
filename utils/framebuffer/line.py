#!/usr/bin/env python
#
'''
## License

The MIT License (MIT)

Copyright (C) 2021 Tomasz Klim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

import sys
import json
import os.path
from PIL import Image,ImageDraw,ImageFont


# the below default values should work correctly with most height={240..320}
# (eg. 320x240, 480x280, 480x320) displays, that can be operated via framebuffer.
#
# note: if your particular display device supports direct GPIO/SPI
# communication and you are able to use any other driver (or write your
# own, based on provided examples), it is recommended to do so, since
# this framebuffer-based driver is very inefficient.
#
background_color = "BLACK"
text_color       = "YELLOW"

margin_left = 6
margin_top  = 0
line_height = 24
max_lines   = 10
font_size   = 20
font_file   = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"


def usage():
    print("Usage: {} <cache-file> <output-file> <width> <height> <line> <text>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 7:
    usage()

if int(sys.argv[5]) > max_lines - 1:
    usage()

fname = sys.argv[1]
output = sys.argv[2]
display_width = int(sys.argv[3])
display_height = int(sys.argv[4])
line = int(sys.argv[5])
text = sys.argv[6]

if display_height > 240:
    margin_top = 10


# either read the cache file or initialize cache with empty lines
if os.path.isfile(fname):
    with open(fname) as f:
        grid = json.load(f)
else:
    grid = [""] * max_lines

# push the changed pixel to cache and save it
grid[line] = text
with open(fname, 'w') as outfile:
    json.dump(grid, outfile)


image = Image.new("RGB", (display_width, display_height), background_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_file, font_size)

# (re)draw texts from cache file
for x in range(max_lines):
    draw.text((margin_left, (x * line_height) + margin_top), grid[x], font = font, fill = text_color)

image.save(output)
