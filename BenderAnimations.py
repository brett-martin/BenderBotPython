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

    def getAnimation(self, animationName):
        animations = {
            "angry": self._angry,
            "suspicious": self._suspicious,
            "bored": self._bored
        }
        return animations.get(animationName, self._none)