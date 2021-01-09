---
layout: post
title: Raspberry Pi and LEDS again
latex
---

It's that time of the year again, so out come the [Raspberry Pi driven LED pixels](2020-01-09-pixels.html).  Here are some notes to myself about how to set this all up, before I forget again for another 11 months.

<!--more-->

### Setting up the Pi

- Download the latest [Raspberry Pi OS](https://www.raspberrypi.org/software/)
- Burn this to a microSD card
- Add details about your [wireless network](https://www.raspberrypi.org/documentation/configuration/wireless/headless.md) to the boot partition
- Add a blank [ssh file](https://www.raspberrypi.org/documentation/remote-access/ssh/README.md) as well.  Default username/password is "pi"/"raspberry"
- Don't forget that you need a decent power supply, but this basically worked fine on my aging Pi zero.

### Wiring the level-shifter

The following is from [Adafruit guide](https://learn.adafruit.com/neopixels-on-raspberry-pi/raspberry-pi-wiring); 
[Link to image](https://learn.adafruit.com/assets/64121)

![Wiring diagram](public/12.png)

But I added a 300 ohm resistor between the output of the IC and the data pin of the pixels; and a 1000 μF capacitor across the terminals of my power supply.

### Python usage

Despite Python 2 being end of life, it seems you still need to use `python3` and `pip3` etc.  The Python bindings now have their own GitHub repo: https://github.com/rpi-ws281x/rpi-ws281x-python

I just did:

    sudo pip3 install rpi_ws281x

You do need `sudo` here as you will need to run Python in `sudo` mode to access the correct hardware (pwm) on the Pi.  Also remember that the _GPIO number is not the same as the pin number!_  Using the `pinout` command is handy here; see also
[gpio docs](https://www.raspberrypi.org/documentation/usage/gpio/)

- Using GPIO 18, pwm, works fine.
- Using 10 didn't work, as the SPI won't initialise.
- Using 21, pcm, works fine.

I then managed to bork the wifi/bluetooth hardware on my Pi Zero (perhaps by over-volting it using a bad Quick Charge usb supply).  Using a Model B
instead, only GPIO 21 works out the box; for further details perhaps see [readme](https://github.com/jgarff/rpi_ws281x/blob/master/README.md).

- It should be possible to power the Pi by connecting the 5V and GND pins to a decent 5V power supply, but I couldn't get this to work: the Pi just kept rebooting.
- Wiring that worked seemed to be to power the level-shifter off the Pi, have all GNDs joined, but keep 5V power lines separate.

That's as far as I got.  Maybe next year some custom light-show will actually be written.
