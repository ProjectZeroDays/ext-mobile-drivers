### Overview

This driver was created to handle Adafruit PiTFT 2.2/2.8 inch 320x240 LCD displays:

- https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi
- https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/overview

These displays are told to support SPI, however I was unable to find any working native driver, so the only option was to use them in framebuffer copy mode.
This mode is inefficient, so while this driver should be easy to use with many other devices, you should consider it as a last-chance driver, and try to find
a native GPIO/SPI driver for your device. Or, if you didn't buy it yet, choose for other model, that has GPIO driver available (it is easy to recognize that:
GPIO driver should provide example scripts, that draw some texts/lines/etc. on the display).


### Installing

```
apt-get install python-pil python3-pip fonts-dejavu-core fbi
pip3 install --upgrade adafruit-python-shell click

git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts
cd Raspberry-Pi-Installer-Scripts

python3 adafruit-pitft.py --display=22 --rotation=90 --install-type=console
```

See https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install-2 for more variants of the last command (`--display=22` parameter
selects 2.2 inch model - however it is safe to use it with 2.8 inch models, it will just disable the touch screen capabilities).


### How this driver works

This is a framebuffer-based driver. It works in a different way (much slower) than native drivers. On each operation:

- empty image is created
- all texts (current and all previous ones) are drawn on this image
- image is saved to filesystem
- image contents are copied to framebuffer by `fbi` tool
