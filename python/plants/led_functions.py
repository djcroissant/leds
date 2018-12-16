from neopixel import *
import time
import numpy as np

from common import CS
from gui_components import TimerGroup, SliderGroup


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
  return target

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

def sunrise(strip):
  """ Red comes in during first third
      Green comes in during 2nd third
      Blue comes in during final third """
  duration = 1 #30     # event duration in minutes
  steps = 60 #0
  wait_sec = duration * 60 / steps  # time to wait between each increment
  target = {"red": 255, "green": 255, "blue": 255}
  state = CS.state

  red_tran = list(np.linspace(state["red"], target["red"], int(steps/3)))
  red_target = [target["red"]] * int(steps * 2 / 3)
  red = red_tran + red_target

  green_state = [state["green"]] * int(steps / 3)
  green_tran = list(np.linspace(state["green"], target["blue"], int(steps/3)))
  green_target = [target["green"]] * int(steps / 3)
  green = green_state + green_tran + green_target

  blue_state = [state["blue"]] * int(steps * 2 / 3)
  blue_tran = list(np.linspace(state["blue"], target["blue"], int(steps/3)))
  blue = blue_state + blue_tran
  
  print("red: ", red)
  print("green: ", green)
  print("blue: ", blue) 
  for i in range(steps):
    CS.state = {"red": red[i], "green": green[i], "blue": blue[i]}
    color = Color(int(green[i]), int(red[i]), int(blue[i]))
    for j in range(strip.numPixels()):
      strip.setPixelColor(j, color)
    strip.show()
    print("sunrise step %s of %s" % (i+1, steps))
    time.sleep(wait_sec)

def sunset(strip):
  """
  If lights are all fully on, then fade down to bright_warm setting
  If lights aren't fully on, do nothing
  """
  state = CS.state
  if state["red"] > 200 and state["green"] > 200 and state["blue"] > 200:
    CS.state = bright_warm(strip, CS.state)
    slider.set_slider(CS.state)
    
def transition(strip, state, target):
  num_pixels = strip.numPixels()
  steps = 50
  red_tran = np.linspace(state["red"], target["red"], steps)
  green_tran = np.linspace(state["green"], target["green"], steps)
  blue_tran = np.linspace(state["blue"], target["blue"], steps)

  for step in range(steps):
    for i in range(num_pixels):
      color = Color(int(green_tran[step]), int(red_tran[step]), int(blue_tran[step]))
      strip.setPixelColor(i, color)
    strip.show()

  
