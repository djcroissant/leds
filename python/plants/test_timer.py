import time
from datetime import datetime
from threading import Timer, Thread, Event

class StartThread(Thread):
    def __init__(self, on_time):
        Thread.__init__(self)
        self.on_time = on_time
        self.delay = get_delta_seconds(on_time)

    def run(self):
      print(self.delay)
      Event().wait(self.delay)
      print('hello')
      # call a function


class StopThread(Thread):
  def __init__(self, off_time):
    Thread.__init__(self)
    self.off_time = off_time
    self.delay = get_delta_seconds(off_time)


  def run(self):
    print('lkasdfl;')
    Event().wait(self.delay)
    print('goodbye')


def get_delta_seconds(future_timer):
  now = datetime.now()
  future_time = now.replace(hour=future_timer[0], minute = future_timer[1])
  delta_t = future_time - now
  return delta_t.seconds + 1

print("Timer set!")
on_time = (19,30)
off_time = (19,31)
start_thread = StartThread(on_time)
start_thread.start()

stop_thread = StopThread(off_time)
stop_thread.start()
