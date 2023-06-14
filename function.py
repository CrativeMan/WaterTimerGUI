import time
import datetime
import water_timer as wt

#TODO: make this input from the user
sec = 20

def add_time():
    pass

def StartTimer():
    global sec

    while sec > 0:
        timer = datetime.timedelta(seconds=sec)
        time.sleep(1)
        sec -= 1