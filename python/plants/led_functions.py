from neopixel import *
import time
import numpy as np


def all_off(strip, state):
  target = {"red": 0, "green": 0, "blue": 0} 
  transition(strip, state, target)
  return target

def all_on(strip, state):
  target = {"red": 255, "green": 255, "blue": 255} 
  transition(strip, state, target)
  return target

def custom_on(strip, state, target):
  transition(strip, state, target)

def awake_evening(strip, state):
  target = {"red": 100, "green": 30, "blue": 10} 
  transition(strip, state, target)
  return target

def bright_warm(strip, state):
  target = {"red": 200, "green": 60, "blue": 20} 
  transition(strip, state, target)
  return target

def dark_and_moody(strip, state):
  target = {"red": 70, "green": 15, "blue": 0} 
  transition(strip, state, target)
  return target

def sultry_dancing(strip, state):
  target = {"red": 120, "green": 15, "blue": 100} 
  transition(strip, state, target)
  return target

def sunrise(strip, state, target):
  """ Red comes in during first third
      Green comes in during 2nd third
      Blue comes in during final third """
  duration = 30     # event duration in minutes
  steps = 600
  wait_sec = duration * 60 / steps  # time to wait between each increment

  red_tran = np.linspace(state["red"], target["red"], int(steps/3))
  red_target = target["red"] * int(steps * 2 / 3)
  red = red_tran + red_target

  green_state = state["green"] * int(steps / 3)
  green_tran = np.linspace(state["green"], target["blue"], int(steps/3))
  green_target = target["green"] * int(steps / 3)
  green = green_state + green_tran + green_target

  blue_state = state["blue"] * int(steps * 2 / 3)
  blue_tran = np.linspace(state["blue"], target["blue"], int(steps/3))
  blue = blue_state + blue_tran
  
  for i in range(steps):
    color = Color(green[i], red[i], blue[i])
    for j in range(strip.numPixels()):
      strip.setPixelColor(j, color)
    strip.show()
    print("sun_transition")
    time.sleep(wait_sec)

def sunset(strip, state, target):
  """
  If lights are all fully on, then fade down to bright_warm setting
  If lights aren't fully on, do nothing
  """
  if state["red"] > 200 and state["green"] > 200 and state["blue"] > 200:
    return bright_warm(strip, state)
    
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

  