from neopixel import *
import time
import numpy as np


def all_off(strip, state):
  target = {"red": 0, "green": 0, "blue": 0} 
  transition(strip, state, target)
  return target

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

def bright_warm(strip):
  red = 200
  green = 60
  blue = 20
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
  red = []
  green = []
  blue = []

  red.extend(arr)
  red.extend(fill_on_half)
  red.extend(fill_on_half)
  green.extend(fill_off_half)
  green.extend(arr)
  green.extend(fill_on_half)
  blue.extend(fill_off_half)
  blue.extend(fill_off_half)
  blue.extend(arr)

  if reverse:
    red = red[::-1]
    green = green[::-1]
    blue = blue[::-1]
    print("red")
    print(red)
    print("green")
    print(green)
    print("blue")
    print(blue)


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

def transition(strip, state, target):
  num_pixels = strip.numPixels()
  steps = 50
  red_tran = np.linspace(state["red"], target["red"], steps)
  green_tran = np.linspace(state["green"], target["green"], steps)
  blue_tran = np.linspace(state["blue"], target["blue"], steps)

  for step in range(steps):
    for i in range(num_pixels):
      color = Color(green_tran[step], red_tran[step], blue_tran[step])
      strip.setPixelColor(i, color)
    strip.show()

  