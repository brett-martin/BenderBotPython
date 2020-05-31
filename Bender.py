"""
Main Bender class controls and syncs all bender sub components
bender = display(eyes) + time + sound + antennaLED + buttons + distance sensor + light sensor
"""
import board
import busio
import time
from digitalio import DigitalInOut, Direction, Pull
from BenderBot.BenderDisplay import BenderDisplay

class Bender():

    def __init__(self):

        #Create the dispay object (Rows, Columns, Segments, brightness)
        self._display = BenderDisplay(16,8,4,0.2)
        #mouth = BenderMouth()
        #trigger = BenderDistanceSensor()
        #RTC = RealTimeClock()

        #Create the Antenna LED and assign it to a board pin
        self._antennaLED = DigitalInOut(board.D11)
        self._antennaLED.direction = Direction.OUTPUT
        self._antennaLED.value = False

        # Create the Colon LED for displaying time and assign it to a board pin
        self._colonLED = DigitalInOut(board.D10)
        self._colonLED.direction = Direction.OUTPUT
        self._colonLED.value = False

    #Gets the current time from RTC module
    def __getTime(self):
        #currentTime = RTC.getTime()
        #formattedTime = RTC.formatTime(currentTime)
        #return formattedTime
        return [1,2,3,4]

    #Plays a complete animation including display, sound, LEDs etc
    def playAnimation(self, animation):
        self._display.playAnimation(self._display.animations.getAnimation(animation))

    #Shows a named expression for delay x
    def showExpression(self, expression, delay):
        self._display.showExpression(self._display.expressions.getExpression(expression))
        self._display.updateDisplay(delay)

    #Shows the current time
    def showTime(self):
        currentTime = self.__getTime()
        self._colonLED.value = True
        self._display.showTime(currentTime)
        self._display.updateDisplay(2)
        self._colonLED.value = False

    #Counts up from x to y in a loop with z seconds in between
    def countUp(self, start, end, delay):
        #TODO: check that start < end and is 0-9999 range
        for number in range(start, end):
            digits = self.getNumberArray(number)
            self._display.showTime(digits)
            self._display.updateDisplay(delay)

    #Counts down from x to y in a loop with z seconds in between
    def countDown(self, start, end, delay):
        #TODO: check that start > end and is 0-9999 range
        for number in range(start, end, -1):
            digits = self.getNumberArray(number)
            self._display.showTime(digits)
            self._display.updateDisplay(delay)

    #Converts an int 0-9999 into a zero-padded array of ints
    def getNumberArray(self, someInt):
        padded = f"{someInt:04}"
        res = [int(x) for x in str(padded)]
        return res

    #Turns on or off the Antenna LED (True,False)
    def antennaOn(self, state):
        self._antennaLED.value = state