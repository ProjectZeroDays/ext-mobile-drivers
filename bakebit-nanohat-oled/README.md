## Overview

`bakebit-nanohat-driver` is a Python I2C driver, with very simple command line interface, for BakeBit NanoHat devices. Currently it supports only the OLED display part.

## Usage

Command line interface for OLED part includes 3 simple scripts:
- `clear.py` - reset the device, set into text mode and clear all contents
- `line.py` - print a single text line
- `restore.py` - print all 8 text lines at once

## Installing

This driver is meant to be used only on Ubuntu 16.04 LTS FriendlyELEC, as provided by NanoPi board vendor. This Ubuntu flavour has certain packages already installed, eg. `python-smbus`. So you only need to download or clone this repository.

You can find more about BakeBit NanoHat OLED devices [here](http://wiki.friendlyarm.com/wiki/index.php/NanoHat_OLED). Note: these devices contain also 3 buttons. These buttons are not supported yet.

## Compatibility

I've tested BakeBit NanoHat OLED devices with NanoPi-NEO2, on dedicated, preinstalled version of Ubuntu 16.04 LTS. It should however work with most NanoPi NEO board models.
