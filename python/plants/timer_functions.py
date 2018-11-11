import time
from datetime import datetime


class TimerFunctions:
  def get_delta_seconds(self, hour, minute):
    now = datetime.now()
    future_time = now.replace(hour=hour, minute = minute)
    delta_t = future_time - now
    return delta_t.seconds + 1