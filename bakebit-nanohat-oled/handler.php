#!/usr/bin/php
<?php

$clear = dirname(__FILE__)."/driver/clear.py";
$print = dirname(__FILE__)."/driver/line.py";

//  -1  - clear all display
//  -2  - dynamic line, use one from command line
// 0-7  - static line, use one from the table
$events = array (
	"shutdown"                                 => array(-1, ""),

	"ready"                                    => array(0, "ready"),
	"target_ready"                             => array(0, "target ready"),
	"target_disconnected"                      => array(0, "ready"),

	"media_device_detected"                    => array(7, "syncing media"),
	"media_device_processed"                   => array(7, "done"),

	"operation_started"                        => array(-2, "syncing data"),
	"operation_finished"                       => array(-2, "done"),
);


function execute($exec) {
	$out = shell_exec($exec);
	if (!empty($out))
		echo trim($out)." [$exec]\n";
}


if ($argc < 3)
	die("usage: $argv[0] <event> <line>\n");

$event = $argv[1];

if (!isset($events[$event]))
	die("error: unknown event \"$event\"\n");

$details = $events[$event];
$line = $details[0];
$text = $details[1];

if ($line == -1)
	execute("$clear");
else {
	if ($line == -2)
		$line = intval($argv[2]);
	execute("$print $line \"$text\"");
}
