from Tkinter import *
from ttk import *

from common import Pix
from timer_threading import TimerThread, WebTimerThread
from led_functions import LedFunctions

from threading import Timer, Thread, Event


class TimerGroup:
  def __init__(self, frame, led_func, pixel, ref=[0,0], title=""):
    self.rrow = ref[0]
    self.rcol = ref[1]
    
    # title
    lbl = Label(frame, text=title)
    lbl.grid(row=self.rrow+0, column=self.rcol+0, columnspan=3)

    # input labels
    Label(frame, text="recurring").grid(row=self.rrow+1, column=self.rcol+0)
    Label(frame, text="hour").grid(row=self.rrow+1, column=self.rcol+1)
    Label(frame, text="minute").grid(row=self.rrow+1, column=self.rcol+2)

    # recurring
    self.recur = IntVar()
    c = Checkbutton(frame, text="", variable=self.recur)
    c.grid(row=self.rrow+2, column=self.rcol+0)

    # time input
    self.hour = Spinbox(frame, from_=0, to=23, width=5)
    self.hour.grid(row=self.rrow+2, column=self.rcol+1)

    self.min = Spinbox(frame, from_=0, to=59, width=5)
    self.min.grid(row=self.rrow+2, column=self.rcol+2)

    # start button properties
    self.start_button = Button(frame, text="Start", command=self.start_button_click)
    self.start_button.grid(row=self.rrow+3, column=self.rcol+0)

    # cancel button properties
    self.cancel_button = Button(frame, text="Cancel", command=self.cancel_button_click)
    self.cancel_button.grid(row=self.rrow+3, column=self.rcol+1)

    # status properties
    self.status = Label(frame, text="Timer OFF", font=("Arial Bold", 24))
    self.status.grid(row=self.rrow+4, column=self.rcol+0, columnspan=3)

    # led function
    self.led_func = led_func
    self.pixel = pixel

  # start button handler
  def start_button_click(self):
    hour = int(self.hour.get())
    minute = int(self.min.get())
    self.status.configure(text="Timer set for %d:%d" % (hour, minute))
    self.stopFlag = Event()
    self.event_thread = TimerThread(self.stopFlag, hour, minute, self.recur, self.led_func, self.pixel)
    self.event_thread.start()

  # cancel button handler
  def cancel_button_click(self):
    self.status.configure(text="Timer OFF")
    self.stopFlag.set()


class SliderGroup:
  def __init__(self, frame, pixel):
    self.pixel = pixel

    # set reference value for row and col.
    # to add content fefore (0,0), increase the reference value by 1 and
    # set row=self.rrow-1 or col=self.rcol-1
    self.rrow=0
    self.rcol=0

    # red slider
    self.red_slider = Scale(frame, from_=0, to=255, orient="horizontal")
    self.red_slider.grid(row=self.rrow+0, column=self.rcol+1, columnspan=2)
    self.lbl = Label(frame, text="Red")
    self.lbl.grid(row=self.rrow+0, column=self.rcol+0)

    # green slider
    self.green_slider = Scale(frame, from_=0, to=255, orient="horizontal")
    self.green_slider.grid(row=self.rrow+1, column=self.rcol+1, columnspan=2)
    self.lbl = Label(frame, text="Green")
    self.lbl.grid(row=self.rrow+1, column=self.rcol+0)

    # blue slider
    self.blue_slider = Scale(frame, from_=0, to=255, orient="horizontal")
    self.blue_slider.grid(row=self.rrow+2, column=self.rcol+1, columnspan=2)
    self.lbl = Label(frame, text="Blue")
    self.lbl.grid(row=self.rrow+2, column=self.rcol+0)
    
    # apply_slider properties
    self.apply_slider = Button(frame, text="Apply Slider", command=self.apply_slider_click)
    self.apply_slider.grid(row=self.rrow+1, column=self.rcol+3, columnspan=2)

  # apply_slider handler
  def apply_slider_click(self):
    target = {
      "red": self.red_slider.get(),
      "green": self.green_slider.get(),
      "blue": self.blue_slider.get()    
    }
    LedFunctions().custom_on(self.pixel, target)
  def set_slider(self, target):
    self.red_slider.set(target["red"])
    self.green_slider.set(target["green"])
    self.blue_slider.set(target["blue"])


class PresetGroup:
  def __init__(self, frame, pixel, slider):
    self.pixel = pixel
    self.slider = slider

    # set reference value for row and col.
    # to add content fefore (0,0), increase the reference value by 1 and
    # set row=self.rrow-1 or col=self.rcol-1
    self.rrow=0
    self.rcol=0

    # preset dropdown
    self.drop_menu = Combobox(frame)
    self.drop_menu['values']=("dark and moody", "sultry dancing", "awake evening", "bright warm")
    self.drop_menu.current(3)
    self.drop_menu.grid(row=self.rrow+0, column=self.rcol+0)
  
    # apply_preset button
    self.apply_preset = Button(frame, text="Apply Preset", command=self.apply_preset_click)
    self.apply_preset.grid(row=self.rrow+0, column=self.rcol+1)

  # apply_preset click handler
  def apply_preset_click(self):
    # check value, call function by same name
    val = self.drop_menu.get()
    preset_lookup = {
      "dark and moody": LedFunctions().dark_and_moody, 
      "sultry dancing": LedFunctions().sultry_dancing, 
      "awake evening": LedFunctions().awake_evening, 
      "bright warm": LedFunctions().bright_warm
    }
    preset_lookup[val](self.pixel)
    self.slider.set_slider(self.pixel.state)


class MasterToggleGroup:
  def __init__(self, frame, pixel, slider):
    self.pixel = pixel
    self.slider = slider

    # set reference value for row and col.
    # to add content fefore (0,0), increase the reference value by 1 and
    # set row=self.rrow-1 or col=self.rcol-1
    self.rrow=0
    self.rcol=0

    # master_on button properties
    self.master_on = Button(frame, text="Lights ON", command=self.master_on_click)
    self.master_on.grid(row=self.rrow+0, column=self.rcol+0)

    # master_off button properties
    self.master_off = Button(frame, text="Lights OFF", command=self.master_off_click)
    self.master_off.grid(row=self.rrow+0, column=self.rcol+1)

  # master_on click handler
  def master_on_click(self):
    LedFunctions().all_on(self.pixel)
    self.slider.set_slider(self.pixel.state)

  # master_off click handler
  def master_off_click(self):
    LedFunctions().all_off(self.pixel)
    self.slider.set_slider(self.pixel.state)

class WebToggleGroup:
  def __init__(self, frame, pixel, slider):
    self.stopFlag = Event()
    self.delay = 1      # second
    self.pixel = pixel
    self.slider = slider

    # set reference value for row and col.
    # to add content fefore (0,0), increase the reference value by 1 and
    # set row=self.rrow-1 or col=self.rcol-1
    self.rrow=0
    self.rcol=0

    # web_on button properties
    self.web_on = Button(frame, text="Web Connect", command=self.web_on_click)
    self.web_on.grid(row=self.rrow+0, column=self.rcol+0)

    # web_off button properties
    self.web_off = Button(frame, text="Lights OFF", command=self.web_off_click)
    self.web_off.grid(row=self.rrow+0, column=self.rcol+1)

  # web_on click handler
  def web_on_click(self):
    self.event_thread = WebTimerThread(self.stopFlag)
    self.event_thread.start()


  # web_off click handler
  def web_off_click(self):
    self.stopFlag.set()
    # LedFunctions().all_off(self.pixel)
    # self.slider.set_slider(self.pixel.state)