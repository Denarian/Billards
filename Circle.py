from Point import Point


class Circle:
    def __init__(self, center: Point, r):
        self.center = center
        self.r = r

    def check_if_on_circle(self, point: Point):
        return round(pow(point.x - self.center.x, 2) + pow(point.y - self.center.y, 2) - pow(self.r, 2)) == 0
