import time
from datetime import datetime
from threading import Timer, Thread, Event

class TimerThread(Thread):
  def __init__(self, event, hour, minute, recur, led_func, pixel):
    Thread.__init__(self)
    self.recur = recur
    self.stopped = event
    self.delay = self.get_delta_seconds(hour, minute)
    self.led_func = led_func
    self.pixel = pixel
    print (self.delay)

  def run(self):
    print('hi there')
    # while not self.stopped.wait(self.delay):
    #   self.led_func(self.pixel)
    #   self.stopped.set()
    # if self.recur:
    #   day_delay = ((24*60)-30)*60    # 24 hrs minus 30 min -> seconds
    #   while not self.stopped.wait(day_delay):
    #     self.led_func(self.pixel)

  def get_delta_seconds(self, hour, minute):
    now = datetime.now()
    future_time = now.replace(hour=hour, minute = minute)
    delta_t = future_time - now
    return delta_t.seconds
