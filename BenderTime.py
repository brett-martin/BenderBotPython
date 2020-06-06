"""
BenderTime handles getting the time from a RTC and returning it in convienant formats
"""
import time
import board
import busio as io

import adafruit_ds3231

class BenderTime():

    def __init__(self, i2c):
        self._rtc = adafruit_ds3231.DS3231(i2c)
        self._days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

    def getTime(self):
        print("Get Time")
        t = self._rtc.datetime
        print(t)
        print(
            "The date is {} {}/{}/{}".format(
            self._days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
            )
        )
        print("The time is {}:{:02}:{:02}".format(t.tm_hour, t.tm_min, t.tm_sec))

    def setTime(self):
        print("set time")
        t = time.struct_time((2017, 10, 29, 15, 14, 15, 0, -1, -1))
        print("Setting time to:", t)
        rtc.datetime = t

    def getTimeArray(self):
        currentTime = self.getTime()
        return[0,5,1,7]

    def setAlarm():
        print("Setting alarm")

    #Check alarm could be used to display an animation on the hour etc.
    def checkAlarm():
        print("Checking Alarm")