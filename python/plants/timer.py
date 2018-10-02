#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
from neopixel import *
import argparse

from datetime import datetime
from threading import Timer, Thread, Event

# LED strip configuration:
LED_COUNT      = 600      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


class StartThread(Thread):
    def __init__(self, strip, on_time):
        Thread.__init__(self)
        self.strip = strip
        self.delay = get_delta_seconds(on_time)

    def run(self):
      print(self.delay)
      Event().wait(self.delay)
      all_on(self.strip)


class StopThread(Thread):
  def __init__(self, strip, off_time):
    Thread.__init__(self)
    self.strip = strip
    self.off_time = off_time
    self.delay = get_delta_seconds(off_time)


  def run(self):
    print(self.delay)
    Event().wait(self.delay)
    all_off(self.strip)


def timer(strip):
  on_time = (13,50)
  # off_time = (13,6)
  # on_time2 = (13,7)
  seconds = get_delta_seconds(on_time)
  print(seconds)
  t = Timer(seconds, all_on, [strip])
  t.start()
  

def get_delta_seconds(future_timer):
  now = datetime.now()
  future_time = now.replace(hour=future_timer[0], minute = future_timer[1])
  delta_t = future_time - now
  return delta_t.seconds + 1

def all_on(strip):
  """All on at quarter brightness"""
  for i in range(strip.numPixels()):
    color = Color(70, 70, 70)
    strip.setPixelColor(i, color)
  strip.show() 

def all_off(strip):
  """All off"""
  for i in range(strip.numPixels()):
    color = Color(0, 0, 0)
    strip.setPixelColor(i, color)
  strip.show()    

# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print("Timer set!")
    on_time = (6,54)
    off_time = (6,56)
    stopFlag = Event()
    start_thread = StartThread(strip, on_time)
    start_thread.start()

    stop_thread = StopThread(strip, off_time)
    stop_thread.start()
