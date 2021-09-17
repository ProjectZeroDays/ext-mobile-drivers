#!/usr/bin/php
<?php

$clear = "/opt/drivebadger/external/ext-mobile-drivers/bakebit-nanohat-oled/driver/clear.py";
$print = "/opt/drivebadger/external/ext-mobile-drivers/bakebit-nanohat-oled/driver/line.py";

$events = array (
	"ready"                                    => array(0, "ready"),
	"progress"                                 => array(0, "..."),
	"shutdown"                                 => array(-1, false),

	"target_drive_ready"                       => array(1, "target ready"),
	"target_drive_disconnected"                => array(1, false),

	"user_drive_mounted"                       => array(4, "user drive mnt"),
	"user_drive_disconnected"                  => array(4, false),

	"ptp_device_detected"                      => array(5, "ptp detected"),
	"ptp_device_processed"                     => array(5, false),

	"mtp_device_detected"                      => array(5, "mtp detected"),
	"mtp_device_processed"                     => array(5, false),

	"operation_started"                        => array(7, "rsyncing data"),
	"operation_finished"                       => array(7, false),
);


function execute($exec) {
	$out = shell_exec($exec);
	if (!empty($out))
		echo trim($out)." [$exec]\n";
}


if ($argc < 2)
	die("usage: $argv[0] <event>\n");

$event = $argv[1];

if (!isset($events[$event]))
	die("error: unknown event \"$event\"\n");

$details = $events[$event];
$line = $details[0]+1;
$text = $details[1];

if ($line == 0)
	execute("$clear");
else {
	if ($text === false)
		$text = "";
	execute("$print $line \"$text\"");
}
