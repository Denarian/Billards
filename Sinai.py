from Point import Point
from Line import Line
import math


class Sinai:
    def __init__(self, x, y):
        self.dim = Point(x, y)
        self.lines = []

    def calculate(self, start: Point, angle, numOfColisons):
        self.lines.append(Line(start, angle))
        new_line = None
        for n in range(numOfColisons):
            # szukamy gdzie uderzy nowa linia i liczymy kat jej odbicia
            if self.check_circle():
                pass
            elif 0 < self.lines[n].angle  and  self.lines[n].angle < 90:
                if self.check_top_wall(self.lines[n]):
                    new_line = self._hit_top_wall(self.lines[n])
                elif self.check_right_wall(self.lines[n]):
                    new_line = self._hit_right_wall(self.lines[n])

            elif 90 < self.lines[n].angle  and  self.lines[n].angle  < 180:
                if self.check_top_wall(self.lines[n]):
                    new_line = self._hit_top_wall(self.lines[n])
                elif self.check_left_wall(self.lines[n]):
                    new_line = self._hit_left_wall(self.lines[n])

            elif -90 < self.lines[n].angle  and  self.lines[n].angle  < 0:
                if self.check_bottom_wall(self.lines[n]):
                    new_line = self._hit_bottom_wall(self.lines[n])
                elif self.check_right_wall(self.lines[n]):
                    new_line = self._hit_right_wall(self.lines[n])

            elif -180 < self.lines[n].angle  and  self.lines[n].angle  < 90:
                if self.check_top_wall(self.lines[n]):
                    new_line = self._hit_top_wall(self.lines[n])
                elif self.check_left_wall(self.lines[n]):
                    new_line = self._hit_left_wall(self.lines[n])

            elif self.lines[n].angle == 0:
                x = self.dim.x
                y = self.lines[n].start.y
                new_angle = 180
                new_line = Line(Point(x, y), new_angle)
            elif abs(self.lines[n].angle) == 180:
                x = 0
                y = self.lines[n].start.y
                new_angle = 0
                new_line = Line(Point(x, y), new_angle)
            elif self.lines[n].angle == 90:
                x = self.lines[n].start.x
                y = self.dim.y
                new_angle = -90
                new_line = Line(Point(x, y), new_angle)
            elif self.lines[n].angle == -90:
                x = self.lines[n].start.x
                y = 0
                new_angle = 90
                new_line = Line(Point(x, y), new_angle)
            else:
                new_line = None
            self.lines.append(new_line)
            #
            # if self.lines[n].start.x == 0:  # start z lewej sciany
            #     if abs(self.lines[n].angle) == 180:  # prostopadla do lewej sciany
            #         x = self.dim.x
            #         y = self.lines[n].start.y
            #         new_angle = 0
            #         new_line = Line(Point(x, y), new_angle)
            #     elif self.check_bottom_wall(self.lines[n]):
            #         new_line = self._hit_bottom_wall(self.lines[n])
            #     elif self.check_top_wall(self.lines[n]):
            #         new_line = self._hit_top_wall(self.lines[n])
            #     elif self.check_right_wall(self.lines[n]):
            #         new_line = self._hit_right_wall(self.lines[n])
            #
            # elif self.lines[n].start.x == self.dim.x:  # start z prawej sciany
            #     if self.lines[n].angle == 0:  # prostopadla do prawej sciany
            #         x = 0
            #         y = self.lines[n].start.y
            #         new_angle = 180
            #         new_line = Line(Point(x, y), new_angle)
            #     elif self.check_bottom_wall(self.lines[n]):
            #         new_line = self._hit_bottom_wall(self.lines[n])
            #     elif self.check_top_wall(self.lines[n]):
            #         new_line = self._hit_top_wall(self.lines[n])
            #     elif self.check_left_wall(self.lines[n]):
            #         new_line = self._hit_left_wall(self.lines[n])
            #
            # elif self.lines[n].start.y == self.dim.y:  # start z gornej sciany
            #     if self.lines[n].angle == 90:  # sprawdzenie czy linia jes trównoległa
            #         x = self.lines[n].start.x
            #         y = self.dim.y
            #         new_angle = -90
            #         new_line = Line(Point(x, y), new_angle)
            #     elif self.check_bottom_wall(self.lines[n]):
            #         new_line = self._hit_bottom_wall(self.lines[n])
            #     elif self.check_left_wall(self.lines[n]):
            #         new_line = self._hit_left_wall(self.lines[n])
            #     elif self.check_right_wall(self.lines[n]):
            #         new_line = self._hit_right_wall(self.lines[n])
            #
            # elif self.lines[n].start.y == 0: # start z dolnej sciany
            #     if self.lines[n].angle == -90:  # sprawdzenie czy linia jes trównoległa
            #         x = self.lines[n].start.x
            #         y = self.dim.y
            #         new_angle = 90
            #         new_line = Line(Point(x, y), new_angle)
            #     elif self.check_top_wall(self.lines[n]):
            #         new_line = self._hit_top_wall(self.lines[n])
            #     elif self.check_right_wall(self.lines[n]):
            #         new_line = self._hit_right_wall(self.lines[n])
            #     elif self.check_left_wall(self.lines[n]):
            #         new_line = self._hit_left_wall(self.lines[n])



    def check_circle(self):
        return False

    def check_top_wall(self, line):
        return 0 <= ((self.dim.y - line.b) / line.a) and ((self.dim.y - line.b) / line.a) <= self.dim.x

    def check_bottom_wall(self, line):
        return 0 <= (0-line.b / line.a) and (0-line.b / line.a) <= self.dim.x

    def check_right_wall(self, line):
        return 0 <= (line.a * self.dim.x + line.b) and (line.a * self.dim.x + line.b) <= self.dim.y

    def check_left_wall(self, line):
        return 0 <= line.b and line.b <= self.dim.y

    def _hit_left_wall(self, line):
        x = 0
        y = line.b
        new_angle = 180-line.angle
        newStart = Point(x, y)
        new = Line(newStart, new_angle)
        return new

    def _hit_right_wall(self, line):
        x = self.dim.x
        y = line.a * self.dim.x + line.b
        new_angle = 180-line.angle
        newStart = Point(x, y)
        new = Line(newStart, new_angle)
        return new

    def _hit_bottom_wall(self, line):
        x = -(line.b / line.a)
        y = 0
        new_angle = 180-line.angle
        newStart = Point(x, y)
        new = Line(newStart, new_angle)
        return new

    def _hit_top_wall(self, line):
        x = (self.dim.y - line.b / line.a)
        y = self.dim.y
        new_angle = 180-line.angle
        newStart = Point(x, y)
        new = Line(newStart, new_angle)
        return new



s = Sinai(100,100)
s.calculate(Point(0,10),15,10)

for l in s.lines:
    print('a: ' + str(l.a) + ' b : '+ str(l.b) + ' x: '+ str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(l.angle))
