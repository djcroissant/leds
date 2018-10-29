from threading import Timer, Thread, Event


class PlantThread(Thread):
    def __init__(self, event, delay):
        Thread.__init__(self)
        self.stopped = event
        self.delay = delay

    def run(self):
        try: 
          while not self.stopped.wait(self.delay):
              print("well hello!")
              # call a function
        except KeyboardInterrupt:
          print('bye')
          stopFlag.set()



stopFlag = Event()
thread = PlantThread(stopFlag, 2)
thread.start()
# this will stop the timer
# stopFlag.set()


# def timed_event():
#   t=Timer(5, the_action, ['hi there'])
#   t.start()

# def the_action(arg):
#   print(arg)

# timed_event()


