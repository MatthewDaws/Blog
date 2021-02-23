---
layout: post
title: Arduino and RTCs
latex
---

My son is keen to build some sort of automated plant watering device, using my Arduino.  I have a:

- [Watering kit (Amazon)](https://www.amazon.co.uk/gp/product/B0814HXWVV) - Seems to work well.  The pump works happily at 5v and something less than 200mA.  It's quite satisfying to see it drain a cup of water.  Definitely powerful enough for this project.
- Youtube has various videos explaining how the water sensor works.  Some brief playing with the Arduino suggests a lot of calibration would be needed.
- The relay which comes with the kit is fun, but the LEDs are sort of annoying for a practical project (more on this below).  A [MOSFET](https://en.wikipedia.org/wiki/MOSFET) transistor would surely work just as well, for this low amp application.
- A [RTC (PiHut)](https://thepihut.com/products/adafruit-pcf8523-real-time-clock-assembled-breakout-board) and the correct battery.

The point of having the RTC is to perform a task at a set time each day (for example).  The Arduino can keep time, but only from when it's switched on.  As quickly discovered, the big problem is that running the Arduino at all times uses quite a bit of power: nothing for a mains-powered solution, but far too much for a battery-powered one.  And somehow grossly inefficient when we want to perform a task once a day.

<!--more-->

Some links:

- [Adafruit quick start guide](https://learn.adafruit.com/adafruit-pcf8523-real-time-clock/rtc-with-arduino)
- [DateTime class reference](https://adafruit.github.io/RTClib/html/class_date_time.html) - From the Adafruit library
- [Timer docs](https://adafruit.github.io/RTClib/html/class_r_t_c___p_c_f8523.html#a54045d4b13deaa90aa7075c735a93634) - Same class docs, but very useful for getting hints as to what the timer actually does.  ("The INT/SQW pin will be pulled low at the end of a specified countdown ... The interrupt low pulse width is adjustable from 3/64ths (default) to 14/64ths of a second.")

Current task is to understand more about how to make a simple circuit which would:
- Use almost no power
- At the interrupt, power up the Arduino
- The Arduino does it's thing, starts a new count-down timer, and then turns itself off

To read:
- https://circuitjournal.com/arduino-auto-power-off
- https://www.instructables.com/Arduino-Microcontroller-Self-Power-Off/
