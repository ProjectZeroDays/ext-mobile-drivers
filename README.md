This repository contains hardware drivers for various LED/LCD displays, used with Raspberry Pi or similar platforms, to signal Mobile Badger functional states.

- [`adafruit-pitft-2x-lcd`](adafruit-pitft-2x-lcd) - [Adafruit PiTFT 2.2/2.8 inch LCD](https://learn.adafruit.com/adafruit-2-2-pitft-hat-320-240-primary-display-for-raspberry-pi)
- [`bakebit-nanohat-oled`](bakebit-nanohat-oled) - [BakeBit NanoHat OLED](http://wiki.friendlyarm.com/wiki/index.php/NanoHat_OLED)
- [`pimoroni-blinkt`](pimoroni-blinkt) - [Pimoroni Blinkt!](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-blinkt)
- [`pimoroni-scroll-hat-mini`](pimoroni-scroll-hat-mini) - [Pimoroni Scroll HAT Mini](https://shop.pimoroni.com/products/scroll-hat-mini)
- [`uctronics-35inch-lcd`](uctronics-35inch-lcd) - [Uctronics 3.5 inch Touchscreen](https://www.uctronics.com/display/uctronics-3-5-inch-touchscreen-for-raspberry-pi-with-case.html)
- [`waveshare-144inch-lcd-hat`](waveshare-144inch-lcd-hat) - [Waveshare 1.44inch LCD display HAT](https://www.waveshare.com/1.44inch-lcd-hat.htm)
- [`waveshare-rgb-led-hat`](waveshare-rgb-led-hat) - [Waveshare True color RGB LED HAT](https://www.waveshare.com/rgb-led-hat.htm)

### Installing

1. Clone this repository as `/opt/drivebadger/external/ext-mobile-drivers` directory on your Mobile Badger device.
2. Inside this directory, create a symlink to subdirectory for your display device, eg. `ln -s pimoroni-blinkt installed`
3. If required, install external drivers for your device.

### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [Mobile Badger wiki](https://github.com/drivebadger/mobilebadger/wiki)
- [Events display page](https://github.com/drivebadger/mobilebadger/wiki/Events-display)
