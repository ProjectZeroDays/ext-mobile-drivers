#!/bin/sh

if [ -f /etc/friendlyelec-release ]; then

	# Make sure that only one instance is running - this is purposely done AFTER checking, if current display really needs initialization..
	exec 9>/run/badger-event.lock
	if ! flock -w 10 9; then exit 1; fi

	/opt/drivebadger/external/ext-mobile-drivers/bakebit-nanohat-oled/driver/clear.py
fi
