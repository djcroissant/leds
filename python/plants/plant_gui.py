# https://likegeeks.com/python-gui-examples-tkinter-tutorial/
from Tkinter import *
from ttk import *

from neopixel import *
from init_strip import *
from timer_threading import *
from led_functions import *
from common import CS

from threading import Timer, Thread, Event

import time
from datetime import datetime


root = Tk()
 
# root properties
root.title("Daya Electric Forest Control Panel")
root.geometry('550x600')


#### TIMER SECTION ####
class TimerGroup:
  def __init__(self, frame, led_func, strip, ref=[0,0], title=""):
    row = ref[0]
    col = ref[1]
    
    # title
    lbl = Label(frame, text=title)
    lbl.grid(row=row+0, column=col+0, columnspan=3)

    # input labels
    Label(frame, text="recurring").grid(row=row+1, column=col+0)
    Label(frame, text="hour").grid(row=row+1, column=col+1)
    Label(frame, text="minute").grid(row=row+1, column=col+2)

    # recurring
    self.recur = IntVar()
    c = Checkbutton(frame, text="", variable=self.recur)
    c.grid(row=row+2, column=col+0)

    # time input
    self.hour = Spinbox(frame, from_=0, to=23, width=5)
    self.hour.grid(row=row+2, column=col+1)

    self.min = Spinbox(frame, from_=0, to=59, width=5)
    self.min.grid(row=row+2, column=col+2)

    # start button properties
    self.start_button = Button(frame, text="Start", command=self.start_button_click)
    self.start_button.grid(row=row+3, column=col+0)

    # cancel button properties
    self.cancel_button = Button(frame, text="Cancel", command=self.cancel_button_click)
    self.cancel_button.grid(row=row+3, column=col+1)

    # status properties
    self.status = Label(frame, text="Timer OFF", font=("Arial Bold", 24))
    self.status.grid(row=row+4, column=col+0, columnspan=3)

    # led function
    self.led_func = led_func
    self.strip = strip

  # start button handler
  def start_button_click(self):
    hour = int(self.hour.get())
    minute = int(self.min.get())
    self.status.configure(text="Timer set for %d:%d" % (hour, minute))
    self.stopFlag = Event()
    self.event_thread = TimerThread(self.stopFlag, hour, minute, self.recur, self.led_func, self.strip)
    self.event_thread.start()

  # cancel button handler
  def cancel_button_click(self):
    self.status.configure(text="Timer OFF")
    self.stopFlag.set()


# Currently passing sunrise/sunset functions to timer groups
# Future version could allow user to pick the function associated with the timer
timer_frame=Frame(root)
timer_frame.pack()
turn_on_frame = Frame(timer_frame, relief="groove")
turn_on_frame.pack(side=LEFT)
turn_on_timer = TimerGroup(turn_on_frame, sunrise, strip, [0,0], "set a time to turn on")

turn_off_frame = Frame(timer_frame,  relief="groove")
turn_off_frame.pack(side=LEFT)
turn_off_timer = TimerGroup(turn_off_frame, sunset, strip, [0,4], "set a time to turn on")


#### SLIDER SECTION ####
class SliderGroup:
  def __init__(self, slider_frame, srow, scol):
    # red slider
    self.red_slider = Scale(slider_frame, from_=0, to=255, orient="horizontal")
    self.red_slider.grid(row=srow+0, column=scol+1, columnspan=2)
    self.lbl = Label(slider_frame, text="Red")
    self.lbl.grid(row=srow+0, column=scol+0)

    # green slider
    self.green_slider = Scale(slider_frame, from_=0, to=255, orient="horizontal")
    self.green_slider.grid(row=srow+1, column=scol+1, columnspan=2)
    self.lbl = Label(slider_frame, text="Green")
    self.lbl.grid(row=srow+1, column=scol+0)

    # blue slider
    self.blue_slider = Scale(slider_frame, from_=0, to=255, orient="horizontal")
    self.blue_slider.grid(row=srow+2, column=scol+1, columnspan=2)
    self.lbl = Label(slider_frame, text="Blue")
    self.lbl.grid(row=srow+2, column=scol+0)
    
    # apply_slider properties
    self.apply_slider = Button(slider_frame, text="Apply Slider", command=self.apply_slider_click)
    self.apply_slider.grid(row=srow+1, column=scol+3, columnspan=2)

  # apply_slider handler
  def apply_slider_click(self):
    target = {
      "red": self.red_slider.get(),
      "green": self.green_slider.get(),
      "blue": self.blue_slider.get()    
    }
    CS.state = custom_on(strip, CS.state, target)

  def set_slider(self, target):
    self.red_slider.set(target["red"])
    self.green_slider.set(target["green"])
    self.blue_slider.set(target["blue"])


srow=0          # 0 to 2
scol=0          # 0 to 0
slider_frame = Frame(root, relief="groove")
slider_frame.pack()

slider = SliderGroup(slider_frame, srow, scol)


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
  preset_lookup = {"dark and moody": dark_and_moody, "sultry dancing": sultry_dancing, "awake evening": awake_evening, "bright warm": bright_warm}
  CS.state = preset_lookup[val](strip, CS.state)
  slider.set_slider(CS.state)

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
  CS.state = all_on(strip, CS.state)
  slider.set_slider(CS.state)

# master_off click handler
def master_off_click():
  CS.state = all_off(strip, CS.state)
  slider.set_slider(CS.state)

# master_on button properties
master_on = Button(master_toggle_frame, text="Lights ON", command=master_on_click)
master_on.grid(row=row+0, column=col+0)

# master_off button properties
master_off = Button(master_toggle_frame, text="Lights OFF", command=master_off_click)
master_off.grid(row=row+0, column=col+1)


 
root.mainloop()
