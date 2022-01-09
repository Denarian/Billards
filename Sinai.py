from Point import Point
from Line import Line
from Circle import Circle
import math


class Sinai:
    def __init__(self, x, y):
        self.dim = Point(x, y)
        self.lines = []
        self.walls = [Line(Point(0, 0), 0, Point(x, 0)),
                      Line(Point(x, 0), 90, Point(x, y)),
                      Line(Point(y, x), 180, Point(0, y)),
                      Line(Point(0, y), 270, Point(0, 0))]
        self.circle = Circle(Point(x / 2, y / 2), x / 4)

    def calculate(self, start: Point, angle, numOfColisons):
        self.lines.append(Line(start, angle))
        for n in range(numOfColisons):
            line: Line = self.lines[-1]
            if self.circle.check_if_on_circle(line.start) is False and line.check_collision_circle(self.circle):
                print('k')
                angle = line.calculate_deflection_angle_circle(self.circle)
                point = line.find_collision_point_circle(self.circle)
                self.lines.append(Line(point, angle))
                continue
            for w in self.walls:
                if w.check_is_on_line(line.start):
                    continue
                if line.check_collision_wall(w):
                    angle = line.calculate_deflection_angle_wall(w)
                    point = line.find_collision_point_wall(w)
                    self.lines.append(Line(point, angle))
                    print(w.angle)
                    break


s = Sinai(100, 100)
s.calculate(Point(0, 0), 45, 10)

for l in s.lines:
    print('a: ' + str(l.a) + ' b : ' + str(l.b) + ' x: ' + str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(
        l.angle))
    # print('x: ' + str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(l.angle))
