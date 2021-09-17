#!/bin/sh

if [ -f /usr/lib/python3/dist-packages/blinkt.py ]; then
	/opt/drivebadger/external/ext-mobile-drivers/pimoroni-blinkt/handler.php "$1"

elif [ -f /etc/friendlyelec-release ]; then
	/opt/drivebadger/external/ext-mobile-drivers/bakebit-nanohat-oled/handler.php "$1"

else
	logger -p user.info -t "badger-event[$$]" -- "$1"
fi
