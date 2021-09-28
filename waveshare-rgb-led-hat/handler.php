#!/usr/bin/php
<?php

$cache = "/run/rgb-led-hat.json";
$cmd = "/opt/drivebadger/external/ext-mobile-drivers/waveshare-rgb-led-hat/driver/set-pixel-rgb.py";

$colors = array (
	"off"    => array(  0,   0,   0),
	"red"    => array(255,   0,   0),
	"green"  => array(  0, 255,   0),
	"blue"   => array(  0,   0, 255),
	"orange" => array(255,  30,   0),
	"yellow" => array(255,  70,   0),
	"purple" => array(255,   0, 255),
	"white"  => array(255, 255, 255),
);

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
list($r, $g, $b) = $colors[$details[1]];

if ($pixel == -1) {
	for ($pixel = 0; $pixel <= 7; $pixel++)
		execute("$cmd $cache $pixel $r $g $b");
} else {
	if ($pixel == -2)
		$pixel = intval($argv[2]);
	execute("$cmd $cache $pixel $r $g $b");
}
