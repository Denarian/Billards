import pytest

import Line
import Point


def _test_line_deflection():
    wall = Line.Line(Point.Point(10,0),90, Point())