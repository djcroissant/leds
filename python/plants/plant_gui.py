# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from Tkinter import *
from ttk import *

from neopixel import *
from timer_threading import TimerThread
from led_functions import LedFunctions
from common import Pix
from gui_components import TimerGroup, SliderGroup, PresetGroup, MasterToggleGroup

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
turn_on_timer = TimerGroup(turn_on_frame, LedFunctions().sunrise, sunshine, [0,0], "set a time to turn on")

turn_off_frame = Frame(timer_frame,  relief="groove")
turn_off_frame.pack(side=LEFT)
turn_off_timer = TimerGroup(turn_off_frame, LedFunctions().sunset, sunshine, [0,4], "set a time to turn off")


#### SLIDER SECTION ####
slider_frame = Frame(root, relief="groove")
slider_frame.pack()
slider = SliderGroup(slider_frame, sunshine)


#### PRESET SECTION ####
preset_frame = Frame(root, relief="groove")
preset_frame.pack()
preset = PresetGroup(preset_frame, sunshine, slider)


#### MASTER TOGGLE SECTION ####
master_toggle_frame = Frame(root, relief="groove")
master_toggle_frame.pack()
master_toggle = MasterToggleGroup(master_toggle_frame, sunshine, slider)

#### WEB TOGGLE SECTION ####
web_toggle_frame = Frame(root, relief="groove")
web_toggle_frame.pack()
web_toggle = WebToggleGroup(web_toggle_frame, sunshine, slider)

 
root.mainloop()
