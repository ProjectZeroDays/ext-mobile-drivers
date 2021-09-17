#!/bin/sh

# Pimoroni Blinkt! is supported only on Raspberry Pi with Raspbian
if [ -f /etc/rpi-issue ] && [ ! -f /usr/lib/python3/dist-packages/blinkt.py ]; then
	echo "now execute as \"pi\" user and reboot:"
	echo "curl https://get.pimoroni.com/blinkt | bash"
fi
