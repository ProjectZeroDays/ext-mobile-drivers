This repository contains hardware drivers for various LED/LCD displays, used with Raspberry Pi or similar platforms, to signal Mobile Badger functional states.

- [`bakebit-nanohat-oled`](bakebit-nanohat-oled) - [BakeBit NanoHat OLED](http://wiki.friendlyarm.com/wiki/index.php/NanoHat_OLED)
- [`pimoroni-blinkt`](pimoroni-blinkt) - [Pimoroni Blinkt!](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt)
- [`pimoroni-scroll-hat-mini`](pimoroni-scroll-hat-mini) - []()
- [`waveshare-144inch-lcd-hat`](waveshare-144inch-lcd-hat) - []()
- [`waveshare-rgb-led-hat`](waveshare-rgb-led-hat) - []()
- [`framebuffer`](framebuffer) - generic driver for all HDMI-only displays, tested with [Adafruit PiTFT](https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi), tuned for generic 320x240 screens

### Installing

1. Clone this repository as `/opt/drivebadger/external/ext-mobile-drivers` directory on your Mobile Badger device.
2. Inside this directory, create a symlink to subdirectory for your display device, eg. `ln -s pimoroni-blinkt installed`
3. If required, install external drivers for your device.

### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [Mobile Badger wiki](https://github.com/drivebadger/mobilebadger/wiki)
- [Events display page](https://github.com/drivebadger/mobilebadger/wiki/Events-display)
