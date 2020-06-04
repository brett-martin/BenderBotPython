"""
BenderExpression class stores expressions in easily accessiable formats from individual expression classes
"""

from BenderBot.Expressions.ExpAngry import ExpAngry
from BenderBot.Expressions.ExpNeutral import ExpNeutral
from BenderBot.Expressions.ExpBored import ExpBored
from BenderBot.Expressions.ExpSemiBored import ExpSemiBored
from BenderBot.Expressions.ExpSemiAngry import ExpSemiAngry
from BenderBot.Expressions.ExpAngry import ExpAngry
from BenderBot.Expressions.ExpSquint1 import ExpSquint1
from BenderBot.Expressions.ExpSquint2 import ExpSquint2
from BenderBot.Expressions.ExpSquint3 import ExpSquint3
from BenderBot.Expressions.ExpSquint4 import ExpSquint4
from BenderBot.Expressions.ExpSquint5 import ExpSquint5
from BenderBot.Expressions.ExpLeftSquint1 import ExpLeftSquint1
from BenderBot.Expressions.ExpLeftSquint2 import ExpLeftSquint2
from BenderBot.Expressions.ExpRightSquint1 import ExpRightSquint1
from BenderBot.Expressions.ExpRightSquint2 import ExpRightSquint2
from BenderBot.Expressions.ExpLookRight1 import ExpLookRight1
from BenderBot.Expressions.ExpLookRight2 import ExpLookRight2
from BenderBot.Expressions.ExpLookLeft1 import ExpLookLeft1
from BenderBot.Expressions.ExpLookLeft2 import ExpLookLeft2
from BenderBot.Expressions.ExpLookDown1 import ExpLookDown1
from BenderBot.Expressions.ExpLookDown2 import ExpLookDown2
from BenderBot.Expressions.ExpLookUp1 import ExpLookUp1
from BenderBot.Expressions.ExpLookUp2 import ExpLookUp2
from BenderBot.Expressions.ExpBlank import ExpBlank
from BenderBot.Expressions.ExpShocked import ExpShocked

class BenderExpressions():

    def __init__(self):
        self._neutral = ExpNeutral().exp
        #self._shocked = ExpShocked
        self._bored = ExpBored().exp
        self._semiBored = ExpSemiBored().exp
        self._angry = ExpSemiAngry().exp
        self._semiAngry = ExpSemiAngry().exp
        self._squint1 = ExpSquint1().exp
        self._squint2 = ExpSquint2().exp
        self._squint3 = ExpSquint3().exp
        self._squint4 = ExpSquint4().exp
        self._squint5 = ExpSquint5().exp
        self._squintLeft1 = ExpLeftSquint1().exp
        self._squintLeft2 = ExpLeftSquint2().exp
        self._squintRight1 = ExpRightSquint1().exp
        self._squintRight2 = ExpRightSquint2().exp
        self._lookRight1 = ExpLookRight1().exp
        self._lookRight2 = ExpLookRight2().exp
        self._lookLeft1 = ExpLookLeft1().exp
        self._lookLeft2 = ExpLookLeft2().exp
        self._lookDown1 = ExpLookDown1().exp
        self._lookDown2 = ExpLookDown2().exp
        self._lookUp1 = ExpLookUp1().exp
        self._lookUp2 = ExpLookUp2().exp
        self._blank = ExpBlank().exp
        self._shocked = ExpShocked().exp

    def getExpression(self, expressionName):
        expressions = {
            "neutral": self._neutral,
            #"shocked": self._shocked,
            "bored": self._bored,
            "semiBored": self._semiBored,
            "angry": self._angry,
            "semiAngry": self._semiAngry,
            "squint1": self._squint1,
            "squint2": self._squint2,
            "squint3": self._squint3,
            "squint4": self._squint4,
            "squint5": self._squint5,
            "squintLeft1": self._squintLeft1,
            "squintLeft2": self._squintLeft2,
            "squintRight1": self._squintRight1,
            "squintRight2": self._squintRight2,
            "lookRight1": self._lookRight1,
            "lookRight2": self._lookRight2,
            "lookLeft1": self._lookLeft1,
            "lookLeft2": self._lookLeft2,
            "lookDown1": self._lookDown1,
            "lookDown2": self._lookDown2,
            "lookUp1": self._lookUp1,
            "lookUp2": self._lookUp2,
            "blank": self._blank,
            "shocked": self._shocked
        }
        return expressions.get(expressionName, self._neutral)