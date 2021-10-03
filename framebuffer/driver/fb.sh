#!/bin/sh

image=$1

# these parameters were set for Adafruit PiTFT devices, you may need to modify them for other device models:
# https://learn.adafruit.com/adafruit-pitft-28-inch-resistive-touchscreen-display-raspberry-pi/displaying-images
#
fbi -T 2 -d /dev/fb1 --noverbose -a $image 2>&1 |grep -v ^using

pkill -TERM fbi
