import time
from datetime import datetime
from threading import Timer, Thread, Event

class TimerThread(Thread):
  def __init__(self, event, hour, minute, recur, led_func, strip):
    Thread.__init__(self)
    self.recur = recur
    self.stopped = event
    self.delay = self.get_delta_seconds(hour, minute)
    self.led_func = led_func
    self.strip = strip
    print (self.delay)

  def run(self):
    Event().wait(self.delay)
    self.led_func(self.strip)
    if self.recur:
      day_delay = 24*60*60    # 24 hrs -> seconds
      while not self.stopped.wait(day_delay):
            print("I'm repeating!")

  def get_delta_seconds(self, hour, minute):
    now = datetime.now()
    future_time = now.replace(hour=hour, minute = minute)
    delta_t = future_time - now
    return delta_t.seconds