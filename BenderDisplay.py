"""
BenderDisplay handles talking to the 4 16x8 LED Matrix arrays and displaying
"""
import time
import board
import busio

from adafruit_ht16k33.matrix import MatrixBackpack16x8
from BenderBot.BenderExpressions import BenderExpressions
from BenderBot.BenderAnimations import BenderAnimations

#TODO: Replace string values with enum
#from enum import Enum
#exp = Enum(angry, bored, suspicious):

class BenderDisplay():

    def __init__(self, rows, columns, segments, brightness):
        self._rows = rows
        self._columns = columns
        self._segments = segments
        self._brightness = brightness

        self._displaySegments = []               #This holds the segment objects we create
        self._expressions = BenderExpressions()  #An object to hold all available display expressions
        self._animations = BenderAnimations()    #An object to hold all available display expressions
        #self._numbers = BenderNumbers()         #An object to hold 0-9 Number data for a segment
        #self._numbersBold = BenderNumbersBold() #An object to hold 0-9 Number data for a segment, Bold

        i2c = busio.I2C(board.SCL, board.SDA)
        i2cStart = 0x70

        #Setup segments in display
        for s in range(0, self._segments):
            segment = MatrixBackpack16x8(i2c, address = i2cStart + s, auto_write=False, brightness=brightness)
            #segment.auto_write = False                             #Dont update segment in real time
            segment.fill(0)                                         #Fill segment with off
            segment.show()                                          #Now update the display
            self._displaySegments.append(segment)                   #Add the segment to our array so we can update it later

    #Sets the brightness of all segments
    def setBrightness(self, value):
        self._brightness = value
        for seg in range(0,self._segments):
            self._displaySegments[seg].brightness = value

    #Fills a single segment all on or off (0,1)
    def fillSegment(self, seg, value):
        self._displaySegments[seg].fill(value)


    #Clears the entire display with all on or off (0,1)
    def clear(self, value):
        for seg in range(0,self._segments):
            self.fillSegment(seg, value)

    #Updates one segment with data from a matrix
    def updateSegment(self, segment, data):
        for row in range(0,16):
            for col in range(0,8):
                segment[row,7-col] = data[row][col]
                #time.sleep(0.05) #Uncomment to watch in slowmo

    #Shows values stored in _segments arrays then waits delay
    def updateDisplay(self, delay):
        for seg in range(0,self._segments):
            self._displaySegments[seg].show()
        time.sleep(delay)

    #Display a single expression which consists of a number of segments, must call updateDisplay() to see it
    def showExpression(self, exp):
        for seg in range(0, self._segments):
            self.updateSegment(self._displaySegments[seg], exp[seg])

    #Plays a series of expressions followed by a delay
    def playAnimation(self, animation):
        for frame in range(0, len(animation)):
            self.showExpression(animation[frame][0])
            self.updateDisplay(animation[frame][1])

    #Displays a single digit on a specific segment
    def displayNumber(number, segment):
        print("Display number")
        # show a number on a specific segment

    #Shows the current time on the display
    def showTime(self, time):
        for digit in range(0, len(time)):
            print(time[digit])
        #For each int in 0-4 updateSegment with matching Segment number
        print("Showing time")

    @property
    def columns(self):
        return self._columns

    @property
    def rows(self):
        return self._rows

    @property
    def segments(self):
        return self._segments

    @property
    def displaySegments(self):
        return self._displaySegments

    @property
    def expressions(self):
        return self._expressions

    @property
    def animations(self):
        return self._animations

    @property
    def brightness(self):
        return self._brightness