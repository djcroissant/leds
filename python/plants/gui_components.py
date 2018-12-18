from Tkinter import *
from ttk import *

from common import Pix
from timer_threading import TimerThread
from led_functions import LedFunctions

from threading import Timer, Thread, Event


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
    sunshine.state = LedFunctions().custom_on(sunshine.strip, sunshine.state, target)

  def set_slider(self, target):
    self.red_slider.set(target["red"])
    self.green_slider.set(target["green"])
    self.blue_slider.set(target["blue"])
