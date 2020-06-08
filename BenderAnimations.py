"""
BenderAnimations contain full animations which are a combination of individual expression frames and delay timings
When played rapidly appear as an animation. Animations are assumed to begin from a neutral face and end on neutral
"""
from BenderBot.BenderExpressions import BenderExpressions

class BenderAnimations():

    def __init__(self):
        expressions = BenderExpressions()

        self._none = [
        [expressions.getExpression("neutral"), 1.0]]

        self._bored = [
        [expressions.getExpression("semiBored"), 0.02],
        [expressions.getExpression("bored"), 2.0],
        [expressions.getExpression("semiBored"), 0.02],
        [expressions.getExpression("neutral"), 0.05]]

        self._angry = [
        [expressions.getExpression("semiAngry"), 0.1],
        [expressions.getExpression("angry"), 1.5],
        [expressions.getExpression("semiAngry"), 0.1],
        [expressions.getExpression("neutral"), 0.02]]

        self._suspicious = [
        [expressions.getExpression("squint1"), 0.02],
        [expressions.getExpression("squint2"), 0.02],
        [expressions.getExpression("squint3"), 0.02],
        [expressions.getExpression("squint4"), 0.02],
        [expressions.getExpression("squint5"), 1.00],
        [expressions.getExpression("squintRight1"), 0.02],
        [expressions.getExpression("squintRight2"), 0.5],
        [expressions.getExpression("squintRight1"), 0.02],
        [expressions.getExpression("squint5"), 0.02],
        [expressions.getExpression("squintLeft1"), 0.02],
        [expressions.getExpression("squintLeft2"), 0.5],
        [expressions.getExpression("squintLeft1"), 0.02],
        [expressions.getExpression("squint5"), 0.02],
        [expressions.getExpression("squint4"), 0.02],
        [expressions.getExpression("squint3"), 0.02],
        [expressions.getExpression("squint2"), 0.02],
        [expressions.getExpression("squint1"), 0.02],
        [expressions.getExpression("neutral"), 2.00]]

        self._lookLeft = [
        [expressions.getExpression("lookLeft1"), 0.02],
        [expressions.getExpression("lookLeft2"), 2.00],
        [expressions.getExpression("lookLeft1"), 0.02],
        [expressions.getExpression("neutral"), 2.00]]

        self._lookRight = [
        [expressions.getExpression("lookRight1"), 0.02],
        [expressions.getExpression("lookRight2"), 2.00],
        [expressions.getExpression("lookRight1"), 0.02],
        [expressions.getExpression("neutral"), 2.00]]

        self._lookUp = [
        [expressions.getExpression("lookUp1"), 0.02],
        [expressions.getExpression("lookUp2"), 2.00],
        [expressions.getExpression("lookUp1"), 0.02],
        [expressions.getExpression("neutral"), 2.00]]

        self._lookDown = [
        [expressions.getExpression("lookDown1"), 0.02],
        [expressions.getExpression("lookDown2"), 2.00],
        [expressions.getExpression("lookDown1"), 0.02],
        [expressions.getExpression("neutral"), 2.00]]

        self._shocked = [
        [expressions.getExpression("shocked"), 2.00],
        [expressions.getExpression("neutral"), 2.00]]

        self._blink = [
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("blank"), 0.01],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("neutral"), 2.00]]

        self._doubleBlink = [
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("blank"), 0.01],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("neutral"), 0.20],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("blank"), 0.01],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("neutral"), 2.00]]

        self._sleep = [
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("blank"), 1.00]]

        self._wakeup = [
        [expressions.getExpression("blank"), 0.10],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("neutral"), 0.50],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("blank"), 0.01],
        [expressions.getExpression("squint4"), 0.001],
        [expressions.getExpression("squint2"), 0.001],
        [expressions.getExpression("neutral"), 2.00]]

    def getAnimation(self, animationName):
        animations = {
            "angry": self._angry,
            "suspicious": self._suspicious,
            "bored": self._bored,
            "lookUp": self._lookUp,
            "lookLeft": self._lookLeft,
            "lookRight": self._lookRight,
            "lookUp": self._lookUp,
            "lookDown": self._lookDown,
            "shocked": self._shocked,
            "blink": self._blink,
            "doubleBlink": self._doubleBlink,
            "sleep": self._sleep,
            "wakeup": self._wakeup,
        }
        return animations.get(animationName, self._none)