"""
BenderSound handles playing audio via Adafruit Sound FX board using a UART serial connection
"""
import time
import board
import busio
from digitalio import DigitalInOut, Direction, Pull

class BenderMouth():

    def __init__(self):
        self._volume = 2

        # Create the Mouth LEDs for showing speech with lights
        self._mouthLED = DigitalInOut(board.D9)
        self._mouthLED.direction = Direction.OUTPUT
        self._mouthLED.value = False

    def soundOn(self, state):
        print(state)

    def setVolume(self, vol):
        self._volume = vol

    def getVolume(self):
        return self._volume

    def playSound(self, soundName):
        sounds = {
            "hello": "hello",
        }
        return sounds.get(soundName, "")

    def animateMouth(self):
        self._mouthLED.value = True
        time.sleep(0.2)
        self._mouthLED.value = False
        time.sleep(0.02)
        self._mouthLED.value = True
        time.sleep(0.04)
        self._mouthLED.value = False
        time.sleep(0.2)
        self._mouthLED.value = True
        time.sleep(0.05)
        self._mouthLED.value = False
        time.sleep(0.2)
        self._mouthLED.value = True
        time.sleep(0.1)
        self._mouthLED.value = False
        time.sleep(0.2)
        self._mouthLED.value = True
        time.sleep(0.07)
        self._mouthLED.value = False