from neopixel import *
import time

def all_off(strip):
  for i in range(strip.numPixels()):
    color = Color(0, 0, 0)
    strip.setPixelColor(i, color)
  strip.show()

def all_on(strip):
  red = 255
  green = 255
  blue = 255
  transition(strip, red, green, blue)

def custom_on(strip, red, green, blue):
  transition(strip, red, green, blue)

def awake_evening(strip):
  red = 100
  green = 30
  blue = 10
  transition(strip, red, green, blue)

def dark_and_moody(strip):
  red = 70
  green = 15
  blue = 0
  transition(strip, red, green, blue)

def sultry_dancing(strip):
  red = 120
  green = 15
  blue = 100
  transition(strip, red, green, blue)

def sun_transiton(strip, reverse=False):
  """ Red comes in during first third
      Green comes in during 2nd third
      Blue comes in during final third """
  duration = 30     # event duration in minutes
  iterations = int(255 * 5 / 3)    # required to bring color in phases
  wait_sec = duration * 60 / iterations  # time to wait between each increment

  arr = list(range(255))
  fill_on_half = [255] * int((iterations - len(arr)) / 2)

  fill_off_half = [0] * int((iterations - len(arr)) / 2)
  red = arr
  red.extend(fill_on_half)
  red.extend(fill_off_half)
  green = fill_off_half
  green.extend(arr)
  green.extend(fill_on_half)
  blue = fill_off_half
  blue.extend(fill_off_half)
  blue.extend(arr)

  if reverse:
    red = red[::-1]
    green = green[::-1]
    blue = blue[::-1]


  for i in range(iterations):
    color = Color(green[i], red[i], blue[i])
    print(red[i])
    print(green[i])
    print(blue[i])
    for j in range(strip.numPixels()):
      strip.setPixelColor(j, color)
    strip.show()
    print(wait_sec)
    time.sleep(wait_sec)

def sunrise(strip):
  sun_transiton(strip, False)

def sunset(strip):
  sun_transiton(strip, True)

def transition(strip, red, green, blue):
  num_pixels = strip.numPixels()
  # turn all off
  for i in range(num_pixels):
    color = Color(0, 0, 0)
    strip.setPixelColor(i, color)
  strip.show()

  # fade in red
  for lum in range(red):
    for i in range(num_pixels):
      color = Color(0, lum, 0)
      strip.setPixelColor(i, color)
    strip.show()

  # fade in green
  for lum in range(green):
    for i in range(num_pixels):
      color = Color(lum, red, 0)
      strip.setPixelColor(i, color)
    strip.show()

  # fade in blue
  for lum in range(blue):
    for i in range(num_pixels):
      color = Color(green, red, lum)
      strip.setPixelColor(i, color)
    strip.show()
