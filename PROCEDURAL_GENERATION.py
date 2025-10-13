import pygame
import math

pygame.init()
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("procedural generation")

tickpersecond = 60
clock = pygame.time.Clock()
held = False

points = [[0,0],[20,20],[40,40],[60,60],[0,0],[20,20],[40,40],[60,60]]
pointsize = [20,23,26,29,32,35,40,30]
disired_dis = 30
middle = half_w,half_h = SCREEN_WIDTH//2,SCREEN_HEIGHT//2
def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def find_new_location(anchor, variable, distance):


    x_anchor, y_anchor = anchor
    x_var, y_var = variable

    dx = x_var - x_anchor
    dy = y_var - y_anchor

    length = math.sqrt(dx**2 + dy**2)

    dx_normalized = dx / length
    dy_normalized = dy / length

    x_new = x_anchor + dx_normalized * distance
    y_new = y_anchor + dy_normalized * distance

    return (x_new, y_new)


angle = 0
target = 0,0

def midpoint(pos1, pos2, per):
    return [pos1[0] + (pos2[0] - pos1[0]) * per, pos1[1] + (pos2[1] - pos1[1]) * per]

def get_true_point(points,per):
    temppoints = points
    while len(temppoints) > 1:
        ttp = []
        for i in range(len(temppoints) - 1):
            ttp.append(midpoint(temppoints[i], temppoints[i + 1], per))
        temppoints = ttp
    return temppoints[0]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            target = event.pos
    screen.fill((0, 0, 0))

    for j in range(len(points) - 1):

        for i in range(len(points)-1):
            curdis = distance(points[i],points[i+1])

            if curdis > disired_dis:
                points[i] = find_new_location(points[i+1],points[i],disired_dis)


    points[-1] = target
    angle += 0.03
    angle %= math.pi*2

    for i in range(len(points)):
        pygame.draw.circle(screen,(50,144,144),points[i],pointsize[i])

    tatpper = [points[3], midpoint(points[3],points[5],0.33), midpoint(points[6],points[4],0.33),points[6]]
    for i in range(50):

        tatp = get_true_point(tatpper, i / 50)

        pygame.draw.circle(screen, (30, 124, 124), (int(tatp[0]), int(tatp[1])), 5)
    for i in range(50):
        tp = get_true_point([points[3], points[4], points[5],points[6]], i / 50)

        pygame.draw.circle(screen, (100, 144, 144), (int(tp[0]),int(tp[1])), 6)



    pygame.display.flip()

    clock.tick(tickpersecond)