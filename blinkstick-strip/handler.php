#!/usr/bin/php
<?php

// this can be adjusted to user preferences, from 1 to 100
$brightness = 80;

//  -1  - clear all display
//  -2  - dynamic line, use one from command line
// 0-7  - static line, use one from the table
$events = array (
	"shutdown"                                 => array(-1, "off"),

	"ready"                                    => array(0, "yellow"),
	"target_ready"                             => array(0, "green"),
	"target_disconnected"                      => array(0, "yellow"),

	"media_device_detected"                    => array(7, "green"),
	"media_device_processed"                   => array(7, "off"),

	"operation_started"                        => array(-2, "green"),
	"operation_finished"                       => array(-2, "off"),
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
$color = $details[1];

if ($color == "off") {
	$brightness = 0;
	$color = "black";
}

if ($pixel == -1) {
	for ($pixel = 0; $pixel <= 7; $pixel++)
		execute("blinkstick --brightness $brightness --index $pixel $color");
} else {
	if ($pixel == -2)
		$pixel = intval($argv[2]);
	execute("blinkstick --brightness $brightness --index $pixel $color");
}
