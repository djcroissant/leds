from neopixel import Color
import time
import numpy as np

from common import Pix


class LedFunctions:
  def all_off(self, pixel):
    target = {"red": 0, "green": 0, "blue": 0} 
    self.transition(pixel, target)

  def all_on(self, pixel):
    target = {"red": 255, "green": 255, "blue": 255} 
    self.transition(pixel, target)

  def custom_on(self, pixel, target):
    self.transition(pixel, target)

  def awake_evening(self, pixel):
    target = {"red": 100, "green": 30, "blue": 10} 
    self.transition(pixel, target)

  def bright_warm(self, pixel):
    target = {"red": 200, "green": 60, "blue": 20} 
    self.transition(pixel, target)

  def dark_and_moody(self, pixel):
    target = {"red": 70, "green": 15, "blue": 0} 
    self.transition(pixel, target)

  def sultry_dancing(self, pixel):
    target = {"red": 120, "green": 15, "blue": 100} 
    self.transition(pixel, target)

  def sunrise(self, pixel):
    """ Red comes in during first third
        Green comes in during 2nd third
        Blue comes in during final third """
    duration = 30     # event duration in minutes
    steps = 600
    wait_sec = duration * 60 / steps  # time to wait between each increment
    target = {"red": 255, "green": 255, "blue": 255}
    state = pixel.state

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
    
    for i in range(steps):
      pixel.state = {"red": red[i], "green": green[i], "blue": blue[i]}
      color = Color(int(green[i]), int(red[i]), int(blue[i]))
      for j in range(pixel.strip.numPixels()):
        pixel.strip.setPixelColor(j, color)
      pixel.strip.show()
      print("sunrise step %s of %s" % (i+1, steps))
      time.sleep(wait_sec)

  def sunset(self, pixel):
    """
    If lights are all fully on, then fade down to bright_warm setting
    If lights aren't fully on, do nothing
    """
    state = pixel.state
    if state["red"] > 200 and state["green"] > 200 and state["blue"] > 200:
      pixel.state = self.bright_warm(pixel)
      
  def transition(self, pixel, target):
    num_pixels = pixel.strip.numPixels()
    steps = 50
    red_tran = np.linspace(pixel.state["red"], target["red"], steps)
    green_tran = np.linspace(pixel.state["green"], target["green"], steps)
    blue_tran = np.linspace(pixel.state["blue"], target["blue"], steps)
    print("red: ", red_tran)
    print("green: ", green_tran)
    print("blue: ", blue_tran)
    pixel.state = target

    for step in range(steps):
      for i in range(num_pixels):
        color = Color(int(green_tran[step]), int(red_tran[step]), int(blue_tran[step]))
        pixel.strip.setPixelColor(i, color)
      pixel.strip.show()
      print("state: ", pixel.state)

  
