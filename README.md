This repository contains hardware drivers for various LED/LCD displays, used with Raspberry Pi or similar platforms, to signal Mobile Badger functional states.

| Device model(s) | Installing | Notes |
| --------------- | ---------- | ----- |
| [Adafruit PiTFT 2.2/2.8 inch LCD](https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi) | [manual](adafruit-pitft-2x-lcd) | framebuffer-based |
| [BakeBit NanoHat OLED](http://wiki.friendlyarm.com/wiki/index.php/NanoHat_OLED) | [manual](bakebit-nanohat-oled) | for [NanoPi NEO/NEO2](http://wiki.friendlyarm.com/wiki/index.php/NanoPi_NEO2), not Raspberry Pi |
| [BlinkStick Strip](https://www.blinkstick.com/products/blinkstick-strip) | [manual](blinkstick-strip) | USB instead of GPIO; our recommended device |
| [Pimoroni Blinkt!](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt) | [manual](pimoroni-blinkt) | our recommended device |
| [Pimoroni Scroll HAT Mini](https://shop.pimoroni.com/products/scroll-hat-mini) | [manual](pimoroni-scroll-hat-mini) |  |
| [Uctronics 3.5 inch Touchscreen](https://www.uctronics.com/display/uctronics-3-5-inch-touchscreen-for-raspberry-pi-with-case.html) | [manual](uctronics-35inch-lcd) | framebuffer-based; avoid it |
| [Waveshare 1.44inch LCD display HAT](https://www.waveshare.com/1.44inch-lcd-hat.htm) | [manual](waveshare-144inch-lcd-hat) |  |
| [Waveshare True color RGB LED HAT](https://www.waveshare.com/rgb-led-hat.htm) | [manual](waveshare-rgb-led-hat) |  |


### Installing

1. Clone this repository as `/opt/drivebadger/external/ext-mobile-drivers` directory on your Mobile Badger device.
2. Follow the detailed install instructions for your device model (see above links).
3. Enable the driver for your device by creating a symbolic link named `installed` to its directory:

```
cd /opt/drivebadger/external/ext-mobile-drivers
ln -s pimoroni-blinkt installed
```

#### Why there is no single install script?

There are two main reasons for it:

1. Each device model has totally different dependencies and prerequisites, that can't be easily handled in a single script.
2. Raspberry Pi don't have a Plug&Play mechanism, and it's not possible to automatically detect and recognize connected devices in a reliable way. So it's up to the user to install the proper drivers.


### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [Mobile Badger wiki](https://github.com/drivebadger/mobilebadger/wiki)
- [Events display page](https://github.com/drivebadger/mobilebadger/wiki/Events-display)
