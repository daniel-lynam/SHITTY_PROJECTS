import pygame
import math
pygame.init()
SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080


def midpoint(pos1, pos2, per):
    return [pos1[0] + (pos2[0] - pos1[0]) * per, pos1[1] + (pos2[1] - pos1[1]) * per]


def get_true_point():
    temppoints = points
    while len(temppoints) > 1:
        ttp = []
        for i in range(len(temppoints) - 1):
            ttp.append(midpoint(temppoints[i], temppoints[i + 1], t))
        temppoints = ttp
    return temppoints[0]


held = None
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("nth degree bezier")
clock = pygame.time.Clock()
points = [[100, 199], [300, 300], [600, 100], [400, 400],[math.pi,1.1],[1,4]]
colour = [(255, 255, 255), (0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 0, 255)]


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    t = 0
    while t < 1:
        tc = get_true_point()
        screen.set_at((round(tc[0]), round(tc[1])), (255, 255, 255))
        t += 0.001
    for i in range(len(points) - 1):
        pygame.draw.line(screen, colour[(i + 1) % len(colour)], points[i], points[i + 1], 1)
    for i in range(len(points)):
        pygame.draw.circle(screen, colour[i % len(colour)], points[i], 5, 2)
    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        curdis = 50
        for i in range(len(points)):
            dis = distance(points[i], [mouse_x, mouse_y])
            if dis < 50 and dis < curdis:
                held = i
                curdis = dis
        if held != None:
            points[held] = pygame.mouse.get_pos()
    else:
        held = None

    pygame.display.flip()
