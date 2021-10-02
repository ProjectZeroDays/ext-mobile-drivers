This repository contains hardware drivers for various LED/LCD displays, used with Raspberry Pi or similar platforms, to signal Mobile Badger functional states.

All of these drivers are also available in separate repositories, for any other use:

- [`bakebit-nanohat-oled`](https://github.com/pisecurity/bakebit-nanohat-driver)
- [`pimoroni-blinkt`](https://github.com/pisecurity/blinkt-persistence)
- `pimoroni-scroll-hat-mini`
- `waveshare-144inch-lcd-hat`
- `waveshare-rgb-led-hat`

### Installing

1. Clone this repository as `/opt/drivebadger/external/ext-mobile-drivers` directory on your Mobile Badger device.
2. Inside this directory, create a symlink to subdirectory for your display device, eg. `ln -s pimoroni-blinkt installed`
3. If required, install external drivers for your device.

### More information

- [Drive Badger main repository](https://github.com/drivebadger/drivebadger)
- [Drive Badger wiki](https://github.com/drivebadger/drivebadger/wiki)
- [Mobile Badger wiki](https://github.com/drivebadger/mobilebadger/wiki)
- [Events display page](https://github.com/drivebadger/mobilebadger/wiki/Events-display)
