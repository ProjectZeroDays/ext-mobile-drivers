## Overview: SPI vs HDMI versions

Uctronics offers [several versions of 3.5-inch LCD screen, with SPI and HDMI interfaces](https://www.uctronics.com/display.html), with different enclosures etc.
Make sure that you buy exactly this version (SPI with acrylic case and stylus):

https://www.uctronics.com/display/uctronics-3-5-inch-touchscreen-for-raspberry-pi-with-case.html

To install the driver, clone exactly this repository:

https://github.com/UCTRONICS/UCTRONICS_HSLCD35

and execute `Raspbian/install_driver.sh` script (it will require reboot at the end).

It is also important, that your initial Raspbian image has compatible kernel version - [one from these](https://github.com/UCTRONICS/UCTRONICS_HSLCD35/tree/master/Raspbian/usr).

Image [`2021-05-07-raspios-buster-armhf-lite.zip`](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip)
([torrent](https://downloads.raspberrypi.org/raspios_lite_armhf/images/raspios_lite_armhf-2021-05-28/2021-05-07-raspios-buster-armhf-lite.zip.torrent)) has kernel version `5.10.17-v7+`, which is good.

Do NOT upgrade it after installing, as it would stop the display from working. Instead, after installing the display, execute:

```
apt-mark hold raspberrypi-kernel
```

which will prevent the kernel from being upgraded in the future. Security-wise, doing so is a bad idea, but it is necessary
for this display to work, since its drivers are linked only with particular kernel versions (source code is not provided).


## Warning

Do NOT follow these instructions, as they are related to different model, and despite of not working, will also install **very old** kernel version, with security bugs:

- https://github.com/UCTRONICS/UCTRONICS_LCD35_RPI
- https://www.uctronics.com/wiki/(SKU:_U4703)UCTRONICS_LCD35_RPI_(SPI_interface)


### How this driver works

This is a framebuffer-based driver. It works in a different way (much slower) than native drivers. On each operation:

- empty image is created
- all texts (current and all previous ones) are drawn on this image
- image is saved to filesystem
- image contents are copied to framebuffer by `fbi` tool
