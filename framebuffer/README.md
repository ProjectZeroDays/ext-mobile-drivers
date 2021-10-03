### Compatibility

This driver was created to handle Adafruit PiTFT 2.2/2.8 inch 320x240 LCD displays:

- https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi
- https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/overview

These displays are told to support SPI, however I was unable to find any working driver, so the only option was to use them in framebuffer copy mode.
This mode is inefficient, so while this driver should be easy to use with many other devices, you should consider it as a last-chance driver, and try to find
a native GPIO/SPI driver for your device. Or, if you didn't buy it yet, choose for other model, that has GPIO driver available (it is easy to recognize that:
GPIO driver should provide example scripts, that draw some texts/lines/etc. on the display).


### How this driver works

Framebuffer-based driver works in a different way than native drivers. On each operation:

- empty 320x240 image is created
- all texts (current and all previous ones) are put on this image
- image is saved to filesystem
- image contents are copied to framebuffer by `fbi` tool


### Installing dependencies

```
apt-get install python-pil python3-pip fonts-dejavu-core fbi
pip3 install --upgrade adafruit-python-shell click

git clone https://github.com/adafruit/Raspberry-Pi-Installer-Scripts
cd Raspberry-Pi-Installer-Scripts

python3 adafruit-pitft.py --display=22 --rotation=90 --install-type=console
```

See https://learn.adafruit.com/adafruit-2-8-pitft-capacitive-touch/easy-install-2 for more variants of the last command.
