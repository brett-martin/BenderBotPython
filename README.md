# BenderBot
CircuitPython library to control animatronicBender

# Example Usage

from BenderBot.Bender import Bender

bender = Bender()

# Supported Functions
bender.showExpression("neutral", 2.0)

bender.playAnimation("blink")
bender.playAnimation("doubleBlink")
bender.playAnimation("shocked")
bender.playAnimation("angry")
bender.playAnimation("bored")
bender.playAnimation("suspicious")
bender.playAnimation("lookDown")
bender.playAnimation("lookLeft")
bender.playAnimation("lookRight")

bender.antennaOn(True)
bender.playAnimation("lookUp")
bender.antennaOn(False)

bender.showTimeFor(5.0)
bender.countUp(1234,1345,0.01)
bender.countDown(100,-1,0.01)

    
