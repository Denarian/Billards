from Sinai import Sinai
from Point import Point
import pygame

size = (1000, 1000)
depth = 10
max_depth = 51
start_point = [Point(300, 20),Point(300, 20), Point(300, 20), Point(300, 20), Point(300, 20), Point(300, 20)]
start_angle = [30, 30, 30, 30, 30, 30]
shift = 1
shift_angle = 1
line_edit = 0
max_line_count = 6
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255)]
s = Sinai(size)
tab = []
tab.append(s.calculate(start_point[0], start_angle[0], depth))
# tab.append(s.calculate(start_point[1], start_angle[1], depth))
# tab.append(s.calculate(start_point[2], start_angle[2], depth))
# tab.append(s.calculate(start_point[1], start_angle[1], depth))
# tab.append(s.calculate(start_point[1], start_angle[1], depth))
# tab.append(s.calculate(start_point[1], start_angle[1], depth))


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
            if event.key == pygame.K_EQUALS and len(tab) < max_line_count:
                tab.append(s.calculate(start_point[0], start_angle[0], depth))
                line_edit = len(tab)-1
            if event.key == pygame.K_MINUS and len(tab) > 1:
                tab.pop(-1)
                line_edit = len(tab)-1
            if event.key == pygame.K_UP:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    shift_angle *= 2
                else:
                    shift *= 2
            if event.key == pygame.K_DOWN:
                if pygame.key.get_mods() & pygame.KMOD_SHIFT:
                    shift_angle /= 2
                else:
                    shift /= 2
            if event.key == pygame.K_LEFT and depth > 0:
                depth -= 1
            if event.key == pygame.K_RIGHT and depth < max_depth:
                depth += 1
            if event.key in range(49, 49 + len(tab)):
                line_edit = event.key - 49
            if event.key == pygame.K_s:
                start_point[line_edit].y += shift
            if event.key == pygame.K_w:
                start_point[line_edit].y -= shift
            if event.key == pygame.K_a:
                start_point[line_edit].x -= shift
            if event.key == pygame.K_d:
                start_point[line_edit].x += shift
            if event.key == pygame.K_e:
                start_angle[line_edit] += shift_angle
                start_angle[line_edit] %= 360
            if event.key == pygame.K_q:
                start_angle[line_edit] -= shift_angle
                start_angle[line_edit] %= 360

            start_point[line_edit].x %= size[0]
            start_point[line_edit].y %= size[1]
            tab[line_edit] = s.calculate(start_point[line_edit], start_angle[line_edit], depth)

    # clear screen
    screen.fill((0, 0, 0))
    depth_text = font.render("Głębokość: " + str(depth), False, colors[line_edit])
    shift_text = font.render("Przesunięcie: " + str(shift) + " | " + str(shift_angle) + "°", False, colors[line_edit])
    screen.blit(depth_text, [size[0] / 2 - depth_text.get_rect().centerx, size[1] / 2 - depth_text.get_rect().centery])
    screen.blit(shift_text,
                [size[0] / 2 - shift_text.get_rect().centerx, size[1] / 2 - shift_text.get_rect().centery + 25])
    # central circle
    pygame.draw.circle(screen, (255, 255, 255), (s.circle.center.x, s.circle.center.y), s.circle.r, 1)

    # walls
    walls = []
    for w in s.walls:
        walls.append(pygame.Vector2(w.start.x, w.start.y))
    pygame.draw.lines(screen, (255, 255, 255), True, walls, 4)

    # trajectories
    for i, lines in enumerate(tab):
        lin = []
        for j, l in enumerate(lines):
            lin.append(pygame.Vector2(l.start.x, l.start.y))
        if len(lin) > 1:
            pygame.draw.lines(screen, colors[i % len(colors)], False, lin)

    pygame.display.flip()
pygame.quit()
