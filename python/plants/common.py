"""
Common module used to hold objects that will be used
in all modules:
"""

# Color State (CS). This holds the current state of the lights
class CS:
  state = {"red": 0, "green": 0, "blue": 0}

  # Function to set slider values
  def set_slider(target):
    red_slider.set(target["red"])
    green_slider.set(target["green"])
    blue_slider.set(target["blue"])