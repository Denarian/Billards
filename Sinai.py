import Circle as C
import Line as L
import Point as P


class Sinai:
    def __init__(self, size):
        x = size[0]
        y = size[1]
        self.dim = P.Point(x, y)
        # self.walls = [L.Line(P.Point(x/2, 0), 45, P.Point(x, y/2)),
        #               L.Line(P.Point(x, y/2), 135, P.Point(x/2, y)),
        #               L.Line(P.Point(x/2, y), 225, P.Point(0, y/2)),
        #               L.Line(P.Point(0, y/2), 315, P.Point(x/2, 0))]
        self.walls = [L.Line(P.Point(0, 0), 0, P.Point(x, 0)),
                      L.Line(P.Point(x, 0), 90, P.Point(x, y)),
                      L.Line(P.Point(x, y), 180, P.Point(0, y)),
                      L.Line(P.Point(0, y), 270, P.Point(0, 0))]
        self.circle = C.Circle(P.Point(x / 2, y / 2), x / 4)
        self.tangents = []

    def calculate(self, start: P.Point, angle, numOfCollisons):
        lines = []
        lines.append(L.Line(start, angle))
        for n in range(numOfCollisons):
            line: L.Line = lines[-1]
            impact = line.find_collision_circle(self.circle)
            if self.circle.check_if_on_circle(line.start) is False and impact:
                # print('k')
                tangent = self.circle.calculate_tangent_in_point(impact)
                self.tangents.append(tangent)
                angle = line.calculate_deflection_angle_wall(tangent)
                lines.append(L.Line(impact, angle))
            else:
                for w in self.walls:
                    if w.check_is_on_line(line.start):
                        continue
                    impact = line.find_collision_wall(w)
                    if impact:
                        angle = line.calculate_deflection_angle_wall(w)
                        lines.append(L.Line(impact, angle))
                        # print(w.angle)
                        break
        return lines