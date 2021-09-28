#!/bin/sh

# Partitions should be mapped to slot (physical lines, rows, pixels etc. of the actual display device):
#
# /dev/sdb2 -> slot 2
# /dev/nvme0n1p3 -> slot 3
# /dev/mmcblk0p2 -> slot 2
#
if [ "$2" = "" ]; then
	slot=0
else
	slot=`echo "$2" |sed 's/[^0-9p]//g' |grep -o '.$' |sed 's/[^0-9]//g'`
fi


# But devices themselves should be ignored, eg. /dev/sdb, /dev/nvme0n1
#
# TODO: /dev/nvme0n1 naming scheme is not properly ignored now. Switch to full Bash
# and recognize device naming schemes separately, similar to get-partition-drive.sh
#
if [ "$slot" = "" ]; then exit 0; fi


# At this point, $slot should always mean:
#   0 - global events (ready, shutdown etc.)
#     - events regarding target drive (UUID registered in target.uuid files)
#     - events regarding MTP/PTP devices, which will be remapped to slot 7 in handlers
#     - (for future) all other events, that have assigned static lines in handlers
# 1-7 - events linked to partition numbers (see above)
#
if [ -x /opt/drivebadger/external/ext-mobile-drivers/installed/handler.php ]; then

	# Make sure that only one instance is running - this is purposely done AFTER
	# scanning partition number and making sure, that this is really required.
	exec 9>/run/badger-event.lock
	if ! flock -w 10 9; then exit 1; fi

	/opt/drivebadger/external/ext-mobile-drivers/installed/handler.php "$1" $slot
else
	logger -p user.info -t "badger-event[$$]" -- "$1 [$2]"
fi
