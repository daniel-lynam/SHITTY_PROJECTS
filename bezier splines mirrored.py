import pygame
import threading

pygame.init()
SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080

held = None
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("bezier splines mirror")
clock = pygame.time.Clock()

#start,ms,me,end/start,ms,me
points = [[100,100],[200,200],[300,300],[400,400],[500,400],[600,400],[700,400]]
colour = [(255,255,255),(0,0,255),(0,255,0),(255,0,0),(0,255,255),(255,255,0),(255,0,255)]
#0-3,3-6,
#i*3-i*3+3
def distance(point1,point2):
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2) ** 0.5
def midpoint(pos1, pos2, per):
    return [pos1[0] + (pos2[0] - pos1[0]) * per, pos1[1] + (pos2[1] - pos1[1]) * per]
def get_true_point():

    temppoints = [points[int(u)*3],points[int(u)*3+1],points[int(u)*3+2],points[int(u)*3+3]]
    while len(temppoints)>1:
        ttp = []
        for i in range(len(temppoints)-1):
            ttp.append(midpoint(temppoints[i], temppoints[i+1], u%1))
        temppoints = ttp

    return temppoints[0]

def get_train_point(tp):
    if int(tp)*3+3 >= len(points):
        temppoints = [points[int(tp-1) * 3], points[int(tp-1) * 3 + 1], points[int(tp-1) * 3 + 2], points[int(tp-1) * 3 + 3]]
    else:
        temppoints = [points[int(tp)*3],points[int(tp)*3+1],points[int(tp)*3+2],points[int(tp)*3+3]]
    while len(temppoints)>1:
        ttp = []
        for i in range(len(temppoints)-1):
            if tp > 0 and tp > (len(points)-1)/3:

                ttp.append(midpoint(temppoints[i], temppoints[i+1], 1))
            else:
                ttp.append(midpoint(temppoints[i], temppoints[i + 1], tp%1))
        temppoints = ttp

    return temppoints[0]

#which formula = (int(i)*3)
#per = i%1
tempp = []
key = True
def access_delay():
    global key
    key = True
def access_accepted():
    global key
    global tempp
    global points
    if key:
        timer = threading.Timer(0.4,access_delay)
        timer.start()
        key = False
        mouse_x, mouse_y = pygame.mouse.get_pos()
        tempp.append([mouse_x, mouse_y])
        if len(tempp) == 3:
            for i in tempp:
                points.append(i)
            tempp = []

traintime = 0
def selfrecurve():
    global traintime
    tl = (len(points)-1)/3
    if traintime < tl:

        timer = threading.Timer(0.025, selfrecurve)
        traintime += 0.0025

        timer.start()







running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    x = 4
    while x < len(points):
        points[x - 2] = [points[x - 1][0] * 2 - points[x][0], points[x - 1][1] * 2 - points[x][1]]
        x += 3
    if pygame.mouse.get_pressed()[2]:
        access_accepted()
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
    if held != None:
        if held % 3 == 0:
            pass
        elif held>1 and held % 3 == 1:
            points[held-2] = [(points[held-1][0]*2)-points[held][0],(points[held-1][1]*2)-points[held][1]]
        elif held<len(points)-2 and held % 3 == 2:
            points[held+2] = [(points[held+1][0]*2)-points[held][0],(points[held+1][1]*2)-points[held][1]]

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        traintime = 0
        selfrecurve()

    u = 0
    while u < (len(points)-1)/3:
        tc = get_true_point()
        screen.set_at((round(tc[0]), round(tc[1])), (255, 255, 255))
        u += 0.001
    for i in range(len(points)-1):
        if i%3 != 1:
            pygame.draw.line(screen,colour[int(int(i)/3)],points[i],points[i+1])
    for i in range(len(points)):
        pygame.draw.circle(screen, colour[int(int(i)/3) % len(colour)], points[i], 5, 2)
    for i in range(len(tempp)):
        pygame.draw.circle(screen, (100,100,100),tempp[i],5,2)

    pygame.draw.circle(screen, colour[int(traintime) % len(colour)], get_train_point(traintime), 5, 2)
    pygame.display.flip()