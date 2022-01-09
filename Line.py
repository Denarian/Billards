import math
from Point import Point
from Circle import Circle


class Line:
    def __init__(self, start: Point, angle, end: Point = None):
        self.start = start
        self.end = end
        self.angle = angle  # angle to X axis
        self.a = None
        self.b = None
        if angle not in [90, 270]:
            self.a = math.tan(angle * math.pi / 180)
            self.b = -(self.a * start.x - start.y)

    def check_collision_wall(self, wall):
        impact = self.find_collision_point_wall(wall)
        if wall.start.x < wall.end.x:
            x1 = wall.start.x
            x2 = wall.end.x
        else:
            x2 = wall.start.x
            x1 = wall.end.x
        if wall.start.y < wall.end.y:
            y1 = wall.start.y
            y2 = wall.end.y
        else:
            y2 = wall.start.y
            y1 = wall.end.y
        return (x1 <= impact.x <= x2) and (y1 <= impact.y <= y2)

    def check_collision_circle(self, circle: Circle):
        if self.angle in [90, 270]:
            return (circle.center.x - circle.r) < self.start.x < (circle.center.x + circle.r)
        else:
            distance = (self.a * circle.center.x - circle.center.y + self.b) / math.sqrt(1 + self.a * self.a)
            return abs(distance) < circle.r

    def find_collision_point_circle(self, circle):
        if self.angle in [90, 270]:
            A = circle.center.x
            B = circle.center.y
            r = circle.r
            x1 = self.start.x
            x2 = x1
            y1 = B - math.sqrt(-pow(A, 2) + 2 * A * x1 + pow(r, 2) - pow(x1, 2))
            y2 = B + math.sqrt(-pow(A, 2) + 2 * A * x2 + pow(r, 2) - pow(x2, 2))
        else:
            a = self.a
            b = self.b
            cx = circle.center.x
            cy = circle.center.y
            r = circle.r
            A = pow(a, 2) + 1
            B = 2 * (a * b - a * cy - cx)
            C = pow(cy, 2) - pow(r, 2) + pow(cx, 2) - 2 * b * cy + pow(b, 2)

            if pow(B, 2) - 4 * A * C <= 0:
                return False

            x1 = (- B + math.sqrt(pow(B, 2) - 4 * A * C)) / (2 * A)
            x2 = (- B - math.sqrt(pow(B, 2) - 4 * A * C)) / (2 * A)

            y1 = a * x1 + b
            y2 = a * x2 + b

        distance1 = math.sqrt(pow(x1 - self.start.x, 2) + pow(y1 - self.start.y, 2))
        distance2 = math.sqrt(pow(x2 - self.start.x, 2) + pow(y2 - self.start.y, 2))

        if distance1 < distance2:
            return Point(x1, y1)
        else:
            return Point(x2, y2)

    def check_is_on_line(self, point: Point):
        if self.a is None:
            return self.start.x == point.x
        elif self.angle in [0, 180]:
            return self.start.y == point.y
        else:
            y = self.a * point.x * self.b
            return y == point.y

    def find_collision_point_wall(self, wall):
        if self.angle == wall.angle:
            return False
        if self.angle in [90, 270] and wall.angle in [90, 270]:
            return False
        elif self.angle in [90, 270]:
            x = self.start.x
            y = wall.a * x + wall.b
            return Point(x, y)
        elif wall.angle in [90, 270]:
            x = wall.start.x
            y = self.a * x + self.b
            return Point(x, y)
        elif wall.angle in [0, 180]:
            y = wall.start.y
            x = (y - self.b) / self.a
            return Point(x, y)
        else:
            x = (wall.b - self.b) / (self.a - wall.a)
            y = (self.a * (wall.b - self.b)) / (self.a - wall.a) * x + self.b
            return Point(x, y)

    def calculate_deflection_angle_wall(self, wall):

        # return 180 - self.angle + wall.angle
        return (wall.angle * 2 - self.angle) % 360

    def calculate_deflection_angle_circle(self, circle):
        collision = self.find_collision_point_circle(circle)
        if collision.x - circle.center.x != 0:
            a = (collision.y - circle.center.y) / (collision.x - circle.center.x)
            angle = math.sin(a) / math.cos(a)
        elif collision.y > circle.center.y:
            angle = 0
        else:
            angle = 180
        tangent = Line(collision, angle)
        return self.calculate_deflection_angle_wall(tangent)
