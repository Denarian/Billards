import math

from Point import Point


class Circle:
    def __init__(self, center: Point, r):
        self.center = center
        self.r = r

    def check_if_on_circle(self, point: Point):
        return round(pow(point.x - self.center.x, 2) + pow(point.y - self.center.y, 2) - pow(self.r, 2)) == 0

    def calculate_tangent_in_point(self, point: Point):
        if self.check_if_on_circle(point):
            if point.x - self.center.x != 0:
                a = (self.center.y - point.y) / (self.center.x - point.x)
                angle = math.atan(a) * 180 / math.pi
                # if not (point.x < self.center.x and point.y < self.center.y):
                #     angle += 180
                # angle -= 90
                angle = (angle + 90) % 360
                # if point.x < self.center.x and point.y < self.center.y:
                #     angle += 180
            elif point.y > self.center.y:
                angle = 0
            else:
                angle = 180
            import Line as l
            print(angle)
            return l.Line(point, angle)
        else:
            return False
