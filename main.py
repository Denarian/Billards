from Sinai import Sinai
from Point import Point
import pygame

size = (800, 800)
depth = 1
max_depth = 30 + 1
start = Point(300, 20)
s = Sinai(size)
tab = []
tab.append(s.calculate(start, 30, max_depth))
tab.append(s.calculate(start, 30.00001, max_depth))
tab.append(s.calculate(start, 29.99999, max_depth))
tab.append(s.calculate(start, 30.00005, max_depth))
tab.append(s.calculate(start, 29.99995, max_depth))

for lines in tab:
    for l in lines:
        print('a: ' + str(l.a) + ' b : ' + str(l.b) + ' x: ' + str(l.start.x) + ' y: ' + str(
            l.start.y) + ' angle: ' + str(
            l.angle))
        # print('x: ' + str(l.start.x) + ' y: ' + str(l.start.y) + ' angle: ' + str(l.angle))

pygame.init()
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 36)
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_LEFT:
                depth -= 1
                depth %= max_depth
            if event.key == pygame.K_RIGHT:
                depth += 1
                depth %= max_depth
    # clear screen
    screen.fill((0, 0, 0))
    depth_text = font.render(str(depth), False, (255, 255, 255))
    screen.blit(depth_text, [size[0] / 2 - depth_text.get_rect().centerx, size[1] / 2 - depth_text.get_rect().centery])
    # central circle
    pygame.draw.circle(screen, (255, 255, 255), (s.circle.center.x, s.circle.center.y), s.circle.r, 1)

    # walls
    walls = []
    for w in s.walls:
        walls.append(pygame.Vector2(w.start.x, w.start.y))
    pygame.draw.lines(screen, (255, 255, 255), True, walls, 4)

    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]

    # trajectories
    for i, lines in enumerate(tab):
        lin = []
        for j, l in enumerate(lines):
            if j > depth:
                break
            lin.append(pygame.Vector2(l.start.x, l.start.y))
        if len(lin) > 1:
            pygame.draw.lines(screen, colors[i % len(colors)], False, lin)

    pygame.display.flip()
pygame.quit()
