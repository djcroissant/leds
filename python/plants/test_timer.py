import time
from datetime import datetime
from threading import Timer, Thread, Event

class StartThread(Thread):
    def __init__(self, on_time):
        Thread.__init__(self)
        self.on_time = on_time

    def run(self):
      Event().wait(5)
      print('hello')
      # call a function


class StopThread(Thread):
  def __init__(self, off_time):
    Thread.__init__(self)
    self.off_time = off_time

  def run(self):
    Event().wait(10)
    print('goodbye')


print("Timer set!")
on_time = (19,30)
off_time = (19,31)
start_thread = StartThread(on_time)
start_thread.start()

stop_thread = StopThread(off_time)
stop_thread.start()
