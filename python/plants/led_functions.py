from neopixel import *

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
