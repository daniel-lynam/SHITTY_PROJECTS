import pygame
from pygame.locals import *
import math
import keyboard

pygame.init()

SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920

player_x = 100
player_y = 100
player_angle = math.pi*2
clock = pygame.time.Clock()

scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("player controlled car")
walls = []
temp_val = []

def sigmoid(x):
    return (1 / (1 + (1.5 ** (-(x/100))))-0.5)*2

def display_beams():

    pygame.draw.line(scrn, (155, 155, 155),
                     (player_x,player_y),
                     (player_x+math.cos(player_angle+math.pi/2)*100,
                      player_y+math.sin(player_angle+math.pi/2)*100))

    x = player_x
    y = player_y
    s1dis = 0
    while 1<x<SCREEN_WIDTH-1 and 1<y<SCREEN_HEIGHT-1:
        s1dis += 1
        x += -math.sin(player_angle)
        y += math.cos(player_angle)
        if scrn.get_at((int(x),int(y))) == (255,255,255):
            pygame.draw.line(scrn, (155, 155, 155),(x-30,y-30),(x,y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y + 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y + 30), (x, y))
            break
    x = player_x
    y = player_y
    s2dis = 0
    while 1 < x < SCREEN_WIDTH - 1 and 1 < y < SCREEN_HEIGHT - 1:
        s2dis += 1
        x += -math.sin(player_angle+math.pi/2)
        y += math.cos(player_angle+math.pi/2)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255):
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y + 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y + 30), (x, y))
            break
    x = player_x
    y = player_y
    s3dis = 0
    while 0 < x < SCREEN_WIDTH -1 and 0 < y < SCREEN_HEIGHT - 1:
        s3dis += 1
        x += -math.sin(player_angle - math.pi / 2)
        y += math.cos(player_angle - math.pi / 2)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255):
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y + 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y + 30), (x, y))
            break
    x = player_x
    y = player_y
    s4dis = 0
    while 0 < x < SCREEN_WIDTH - 1 and 0 < y < SCREEN_HEIGHT - 1:
        s4dis += 1
        x += -math.sin(player_angle - math.pi / 4)
        y += math.cos(player_angle - math.pi / 4)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255):
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y + 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y + 30), (x, y))
            break
    x = player_x
    y = player_y
    s5dis = 0
    while 0 < x < SCREEN_WIDTH - 1 and 0 < y < SCREEN_HEIGHT - 1:
        s5dis += 1
        x += -math.sin(player_angle + math.pi / 4)
        y += math.cos(player_angle + math.pi / 4)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255):
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y - 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + 30, y + 30), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - 30, y + 30), (x, y))
            break
    txtlist = [s1dis,s2dis,s3dis,s4dis,s5dis]
    font = pygame.font.Font(None, 74)
    for i in range(5):
        text = font.render(str(txtlist[i]), True, (55,55,55))
        scrn.blit(text, (100+200*i, 1000))
        text = font.render(str(sigmoid(txtlist[i]))[0:4], True, (55, 55, 55))
        scrn.blit(text, (700 + 200 * i, 10))
checkpoints = []
def write_wall():
    global walls
    global temp_val
    pos = pygame.mouse.get_pos()
    print(pos[0],pos[1])
    temp_val.append((pos[0],pos[1]))

    if len(temp_val) == 2:
        walls.append(tuple(temp_val))
        temp_val = []

def print_data():
    print(walls)
    print("^walls")
    print(checkpoints)
    print("^chp")
t2val = []
def write_ckp():
    global t2val
    global checkpoints
    pos = pygame.mouse.get_pos()
    print(pos[0], pos[1])
    t2val.append((pos[0], pos[1]))

    if len(t2val) == 2:
        checkpoints.append(tuple(t2val))
        t2val = []
keyboard.add_hotkey('q', write_wall)
keyboard.add_hotkey('e', print_data)
keyboard.add_hotkey('t', write_ckp)
n = True
while n:

    for event in pygame.event.get():
        if event.type == QUIT:
            n = False

    scrn.fill((0, 0, 0))
    for i in range(len(checkpoints)):
        pygame.draw.line(scrn, (0, 255-i, 0), checkpoints[i][0], checkpoints[i][1], 10)
    for i in walls:
        pygame.draw.line(scrn, (255, 255, 255), i[0], i[1], 10)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_angle -= 0.03

    if keys[pygame.K_RIGHT]:
        player_angle += 0.03

    if keys[pygame.K_UP]:
        m = True
        for i in range(5):
            if scrn.get_at((int(player_x + -math.sin(player_angle) * i), int(player_y + math.cos(player_angle) * i))) == (255,255,255):
                m = False
                player_x += -math.sin(player_angle) * (i-1)
                player_y += math.cos(player_angle) * (i-1)
                break
        if m:
            player_x += -math.sin(player_angle) * (5)
            player_y += math.cos(player_angle) * (5)

    display_beams()
    pygame.draw.circle(scrn, (255, 255, 255), (player_x, player_y), 5)
    pygame.display.flip()
    clock.tick(60)
