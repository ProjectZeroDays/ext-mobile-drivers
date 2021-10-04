#!/bin/sh

image=$1

fbi -T 2 -d /dev/fb1 --noverbose -a $image 2>&1 |grep -v ^using

pkill -TERM fbi
