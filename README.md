# BenderBot
CircuitPython library to control animatronicBender

# Example Usage

"""
Bender Display implementation
"""

from BenderBot.Bender import Bender

bender = Bender()

while True:
    #Loop through current animations pausing between each one with neutral expression
    bender.showExpression("neutral", 2.0)
    bender.playAnimation("angry")
    
    bender.showExpression("neutral", 2.0)
    bender.playAnimation("bored")
    
    bender.showExpression("neutral", 2.0)
    bender.playAnimation("suspicious")
    
    #bender.showTime()
    #bender.__getTime() 
    