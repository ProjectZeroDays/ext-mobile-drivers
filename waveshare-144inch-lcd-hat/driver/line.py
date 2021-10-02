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
import LCD_1in44
import LCD_Config
from PIL import Image,ImageDraw


# this is the default color scheme
background_color = "WHITE"
text_color       = "BLACK"

# you can apply this (or any other) color scheme, however remember that this
# display device changes color to WHITE for ~1 second during each LCD_Init,
# so your display will blink, which can bring someone's attention.
#
#background_color = "BLACK"
#text_color       = "YELLOW"


margin_left = 6
line_height = 12
max_lines   = 10


def usage():
    print("Usage: {} <cache-file> <line> <text>".format(sys.argv[0]))
    sys.exit(1)

if len(sys.argv) != 4:
    usage()

if int(sys.argv[2]) > max_lines - 1:
    usage()

fname = sys.argv[1]
line = int(sys.argv[2])
text = sys.argv[3]


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


# initialize the screen
LCD = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
LCD.LCD_Init(Lcd_ScanDir)

image = Image.new("RGB", (LCD.width, LCD.height), background_color)
draw = ImageDraw.Draw(image)

# (re)draw texts from cache file
for x in range(max_lines):
    draw.text((margin_left, x * line_height), grid[x], fill = text_color)

# push the final image to the device
LCD.LCD_ShowImage(image,0,0)
