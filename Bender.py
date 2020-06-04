"""
Main Bender class controls and syncs all bender sub components
bender = display(eyes) + time + sound + antennaLED + buttons + distance sensor + light sensor
"""
import board
import busio
import time
from BenderBot.BenderDisplay import BenderDisplay
from BenderBot.BenderMouth import BenderMouth
from BenderBot.BenderTime import BenderTime

class Bender():

    def __init__(self):
        #Create i2c bus to talk to displays and RTC
        self._i2c = busio.I2C(board.SCL, board.SDA)

        #Create the dispay object (Rows, Columns, Segments, brightness, i2c bus)
        self._display = BenderDisplay(16,8,4,0.2,self._i2c)

        #Create the mouth object that will handle speech and mouth animation
        self._mouth = BenderMouth()

        #Create the clock object that will wrap all time functions
        self._clock = BenderTime(self._i2c)

        #Create a distance sensor that will tell is if someone is in front of Bender
        #trigger = BenderDistanceSensor()

    #Sets mode of operation for bender
    def setMode(self): #TODO:
        print("Set Mode")
        #Possible modes: Clock, Random expressions, Manual mode, Count up/down, sleep, set time, volume

    # Turns sound on or off for expressions
    def soundOn(self, state):
        self._mouth.soundOn(state)

    #Plays a complete animation including display, sound, LEDs etc
    def playAnimation(self, animation):
        self._display.playAnimation(self._display.animations.getAnimation(animation))

    #Shows a named expression for delay x
    def showExpression(self, expression, delay):
        self._display.showExpression(self._display.expressions.getExpression(expression))
        self._display.updateDisplay(delay)

    #Shows the current time
    def showTime(self):
        currentTime = self._clock.getTimeArray()
        self._display.showTime(currentTime)
        self._display.updateDisplay(2)
        self._display.colonOn(False)

    #Shows the current time for x seconds
    def showTimeFor(self, delay):
        currentTime = self._clock.getTimeArray()
        self._display.showTime(currentTime)
        self._display.updateDisplay(delay)
        self.showExpression("blank",0.0)
        self._display.colonOn(False)
        self._display.updateDisplay(1.0)

    #Counts up from x to y in a loop with z seconds in between
    def countUp(self, start, end, delay):
        #TODO: check that start < end and is 0-9999 range
        for number in range(start, end):
            digits = self.getNumberArray(number)
            self._display.showTime(digits)
            self._display.updateDisplay(delay)
        self._display.colonOn(False)

    #Counts down from x to y in a loop with z seconds in between
    def countDown(self, start, end, delay):
        #TODO: check that start > end and is 0-9999 range
        for number in range(start, end, -1):
            digits = self.getNumberArray(number)
            self._display.showTime(digits)
            self._display.updateDisplay(delay)
        self._display.colonOn(False)

    #Converts an int 0-9999 into a zero-padded array of ints
    def getNumberArray(self, someInt):
        padded = f"{someInt:04}"
        res = [int(x) for x in str(padded)]
        return res

    #Turns on or off the Antenna LED (True,False)
    def antennaOn(self, state):
        self._display.antennaOn(state)

    #Pulses the Mouth LEDs
    def mouthOn(self): #Demo of what mouth might look like
        self._mouth.animateMouth()