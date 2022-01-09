import math
import Point

class Line:
    def __init__(self, start:Point, angle):
        self.start = start
        self.angle = angle # angle to X axis
        self.a = None
        self.b = None
        if(abs(angle) != 90):
            self.a = math.tan(-angle)
            self.b = -(self.a * start.x - start.y)



    def find_colision_point(self, line):
        if(self.angle == line.angle):
            return False
        if(self.angle == 90):
            return Point.Point(0,0)
        else:
            a1 = math.tan(self.angle)
            b1 = -a1 * self.start.x + self.start.y
            a2 = math.tan(line.angle)
            b2 = -a2 * line.start.x + line.start.y
            x = (b2-b1)/(a1 - a2)
            y = a1*(b2 - b1) / (a1 - a2) * x + b1
            return Point.Point(x , y)
