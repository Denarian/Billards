import Circle as C
import Line as L
import Point as P


class Sinai:
    def __init__(self, x, y):
        self.dim = P.Point(x, y)
        self.lines = []
        self.walls = [L.Line(P.Point(x/2, 0), 45, P.Point(x, y/2)),
                      L.Line(P.Point(x, y/2), 135, P.Point(x/2, y)),
                      L.Line(P.Point(x/2, y), 225, P.Point(0, y/2)),
                      L.Line(P.Point(0, y/2), 315, P.Point(x/2, 0))]
        # self.walls = [L.Line(P.Point(0, 0), 0, P.Point(x, 0)),
        #               L.Line(P.Point(x, 0), 90, P.Point(x, y)),
        #               L.Line(P.Point(x, y), 180, P.Point(0, y)),
        #               L.Line(P.Point(0, y), 270, P.Point(0, 0))]
        self.circle = C.Circle(P.Point(x / 2, y / 2), x / 5)
        self.tangents = []

    def calculate(self, start: P.Point, angle, numOfCollisons):
        self.lines.append(L.Line(start, angle))
        for n in range(numOfCollisons):
            line: L.Line = self.lines[-1]
            if self.circle.check_if_on_circle(line.start) is False and line.check_collision_circle(self.circle):
                print('k')
                impact = line.find_collision_point_circle(self.circle)
                tangent = self.circle.calculate_tangent_in_point(impact)
                self.tangents.append(tangent)
                angle = line.calculate_deflection_angle_wall(tangent)
                self.lines.append(L.Line(impact, angle))
            else:
                for w in self.walls:
                    if w.check_is_on_line(line.start):
                        continue
                    if line.check_collision_wall(w):
                        angle = line.calculate_deflection_angle_wall(w)
                        point = line.find_collision_point_wall(w)
                        self.lines.append(L.Line(point, angle))
                        print(w.angle)
                        break
