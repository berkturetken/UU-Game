from enum import Enum
import prints


class Color(Enum):
    RED = 0
    YELLOW = 1
    
class Shape(Enum):
    CROSS = 0
    CIRCLE = 1

class OuterColor(Enum):
    GREEN = 0
    BLUE = 1

class OuterShape(Enum):
    SQUARE = 0
    ROUND = 1

class Piece:
    def __init__(self, color, shape, outerColor, outerShape):
        if (color == 0):
            self.color = Color.RED
        else:
            self.color = Color.YELLOW

        if (shape == 0):
            self.shape = Shape.CROSS
        else:
            self.shape = Shape.CIRCLE

        if (outerColor == 0):
            self.outerColor = OuterColor.GREEN
        else:
            self.outerColor = OuterColor.BLUE

        if (outerShape == 0):
            self.outerShape = OuterShape.SQUARE
        else:
            self.outerShape = OuterShape.ROUND
            
        #self.color = color
        #self.shape = shape
        #self.outerColor = outerColor
        #self.outerShape = outerShape

    def printSelf(self):
        color = None
        shape = None
        outerShapeLeft = None
        outerShapeRight = None
        outerColor = None
        if (self.color == Color.RED):
            color = prints.sf.RED
        else:
            color = prints.sf.YELLOW
        if (self.shape == Shape.CROSS):
            shape = 'X'
        else:
            shape = 'O'
        if (self.outerColor == OuterColor.GREEN):
            outerColor = prints.sf.GREEN
        else:
            outerColor = prints.sf.BLUE
        if (self.outerShape == OuterShape.SQUARE):
            outerShapeLeft = '['
            outerShapeRight = ']'
        else:
            outerShapeLeft = '('
            outerShapeRight = ')'

        prints.eprint(outerShapeLeft, outerColor, True, False)
        prints.eprint(shape, color, True, False)
        prints.eprint(outerShapeRight, outerColor, True, False)

    def __eq__(self, other):
        if (other is None):
            return False
        return (self.shape == other.shape or
                self.color == other.color or
                self.outerShape == other.outerShape or
                self.outerColor == other.outerColor)

    def equal(self, other):
        
        return (self.shape is other.shape or
                self.color is other.color or
                self.outerShape is other.outerShape or
                self.outerColor is other.outerShape)

    def equals(self, other1, other2, other3):
        return (self.shape == other1.shape and self.shape == other2.shape and self.shape == other3.shape or
                self.color == other1.color and self.color == other2.color and self.color == other3.color or
                self.outerShape == other1.outerShape and self.outerShape == other2.outerShape and self.outerShape == other3.outerShape or
                self.outerColor == other1.outerColor and self.outerColor == other2.outerColor and self.outerColor == other3.outerColor)
