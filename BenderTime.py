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

    #Prints the current time to the console
    def printTime(self, twelve):
        t = self._rtc.datetime
        hour = t.tm_hour
        if twelve == True:
            if hour > 12:
                hour -= 12

        print("{}:{:02}:{:02}".format(hour, t.tm_min, t.tm_sec))

    #Prints the current date to the console
    def printDate(self):
        t = self._rtc.datetime
        print(
            "{} {}/{}/{}".format(
            self._days[int(t.tm_wday)], t.tm_mday, t.tm_mon, t.tm_year
            )
        )

    #Sets the time on the RTC
    def setTime(self, year, month, day, hour, minute, second):
        wday = 0 #week starts on 0 monday
        yday = -1 # day of the year?
        dst = 0 #0 no, 1 dst, -1 unknown

        t = time.struct_time((year, month, day, hour, minute, second, wday, yday, dst))

        print("Setting time to:", t)
        self._rtc.datetime = t

    #Gets the current time and returns an array of 4 digits
    def getTime(self, twelve):
        t = self._rtc.datetime
        hours = t.tm_hour
        minutes = t.tm_min
        h1 = 0
        h2 = 0
        m1 = 0
        m2 = 0
        #Convert to 12hr format
        if twelve == True:
            if hours > 12:
                hours -= 12

        hourStr = str(hours)
        minuteStr = str(minutes)
        #Split hours into digits
        if hours < 10:
            h2 = int(hourStr[0])
        else:
            h1 = int(hourStr[0])
            h2 = int(hourStr[1])
        #Split minutes into digits
        if minutes < 10:
            m2 = int(minuteStr[0])
        else:
            m1 = int(minuteStr[0])
            m2 = int(minuteStr[1])

        return[h1,h2,m1,m2]

    #TODO: Sets alarm on RTC
    def setAlarm():
        print("Setting alarm")

    #TODO: Check alarm could be used to display an animation on the hour etc.
    def checkAlarm():
        print("Checking Alarm")