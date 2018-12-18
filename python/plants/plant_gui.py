# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from Tkinter import *
from ttk import *

from neopixel import *
from timer_threading import TimerThread
from led_functions import LedFunctions
from common import Pix
from gui_components import TimerGroup, SliderGroup

from threading import Timer, Thread, Event

import time
from datetime import datetime


root = Tk()
sunshine = Pix()
 
# root properties
root.title("Daya Electric Forest Control Panel")
root.geometry('550x600')


#### TIMER SECTION ####
# Currently passing sunrise/sunset functions to timer groups
# Future version could allow user to pick the function associated with the timer
timer_frame=Frame(root)
timer_frame.pack()
turn_on_frame = Frame(timer_frame, relief="groove")
turn_on_frame.pack(side=LEFT)
turn_on_timer = TimerGroup(turn_on_frame, LedFunctions().sunrise, sunshine.strip, [0,0], "set a time to turn on")

turn_off_frame = Frame(timer_frame,  relief="groove")
turn_off_frame.pack(side=LEFT)
turn_off_timer = TimerGroup(turn_off_frame, LedFunctions().sunset, sunshine.strip, [0,4], "set a time to turn on")


#### SLIDER SECTION ####
srow=0          # 0 to 2
scol=0          # 0 to 0
slider_frame = Frame(root, relief="groove")
slider_frame.pack()

slider = SliderGroup(slider_frame, srow, scol, sunshine)


#### PRESET SECTION ####
row=0          # 0 to 2
col=0          # 0 to 0
preset_frame = Frame(root, relief="groove")
preset_frame.pack()

# preset dropdown
preset_drop = Combobox(preset_frame)
preset_drop['values']=("dark and moody", "sultry dancing", "awake evening", "bright warm")
preset_drop.current(1)
preset_drop.grid(row=row+0, column=col+0)

# apply_preset click handler
def apply_preset_click():
  # check value, call function by same name
  val = preset_drop.get()
  preset_lookup = {
    "dark and moody": LedFunctions().dark_and_moody, 
    "sultry dancing": LedFunctions().sultry_dancing, 
    "awake evening": LedFunctions().awake_evening, 
    "bright warm": LedFunctions().bright_warm
  }
  preset_lookup[val](sunshine)
  slider.set_slider(sunshine.state)

# apply_preset button
apply_preset = Button(preset_frame, text="Apply Preset", command=apply_preset_click)
apply_preset.grid(row=row+0, column=col+1)

#### MASTER TOGGLE SECTION ####
row=0          # 0 to 2
col=0          # 0 to 0
master_toggle_frame = Frame(root, relief="groove")
master_toggle_frame.pack()

# master_on click handler
def master_on_click():
  LedFunctions().all_on(sunshine)
  slider.set_slider(sunshine.state)

# master_off click handler
def master_off_click():
  LedFunctions().all_off(sunshine)
  slider.set_slider(sunshine.state)

# master_on button properties
master_on = Button(master_toggle_frame, text="Lights ON", command=master_on_click)
master_on.grid(row=row+0, column=col+0)

# master_off button properties
master_off = Button(master_toggle_frame, text="Lights OFF", command=master_off_click)
master_off.grid(row=row+0, column=col+1)


 
root.mainloop()
