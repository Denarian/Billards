import pygame

from Sinai import Sinai
from Line import Line
from Circle import Circle
from Point import Point

s = Sinai(500, 500)
# s.calculate(Point(401, 200), 185, 20)
s.calculate(Point(170, 100), 80, 3)
# s.calculate(Point(400, 250), 30, 10)

# s.calculate(Point(250, 50), 270, 1)
# s.calculate(Point(450, 250), 0, 1)
# s.calculate(Point(50, 250), 180, 1)
# s.calculate(Point(250, 450), 90, 1)

for l in s.lines:
    print('a: ' + str(l.a) + ' b : ' + str(l.b) + ' x: ' + str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(
        l.angle))
    # print('x: ' + str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(l.angle))

# Simple pygame program

# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    # screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (s.circle.center.x, s.circle.center.y), s.circle.r)

    walls = []
    for w in s.walls:
        walls.append(pygame.Vector2(w.start.x, w.start.y))
    pygame.draw.lines(screen, (255, 255, 255), True, walls)

    lines = []
    for l in s.lines:
        lines.append(pygame.Vector2(l.start.x, l.start.y))
    pygame.draw.lines(screen, (255, 0, 0), False, lines)

    # if len(s.tangents):
    #     tangents = []
    #     for l in s.tangents:
    #         pygame.draw.line(screen, (0, 255, 0), (l.start.x - 10, l.y(l.start.x - 10)),
    #                          (l.start.x + 10, l.y(l.start.x + 10)))
    #         pygame.draw.line(screen, (125, 0, 255), (l.start.x, l.start.y), (s.circle.center.x, s.circle.center.y))

    # Flip the display
    pygame.display.flip()

    # Done! Time to quit.
pygame.quit()
