#!/usr/bin/php
<?php

$cache = "/run/scroll-hat.json";
$clear = dirname(__FILE__)."/driver/clear.py";
$cmd = dirname(__FILE__)."/driver/set-pixel.py";

$levels = array (
	"off"  => 0,
	"half" => 6,
	"full" => 9,
);

//  -1  - clear all display
//  -2  - dynamic line, use one from command line
// 0-9  - static line, use one from the table
$events = array (
	"shutdown"                                 => array(-1, 0, "off"),

	"ready"                                    => array(0, 0, "half"),
	"target_ready"                             => array(0, 2, "half"),
	"target_disconnected"                      => array(0, 2, "off"),

	"media_device_detected"                    => array(9, 0, "half"),
	"media_device_processed"                   => array(9, 0, "off"),

	"operation_started"                        => array(-2, 0, "half"),
	"operation_finished"                       => array(-2, 0, "off"),
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
$pixel = $details[0];
$row = $details[1];
$brightness = $levels[$details[2]];


if ($pixel == -1)
	execute("$clear");
else {
	if ($pixel == -2)
		$pixel = intval($argv[2]);
	execute("$cmd $cache $pixel $row $brightness");
}
