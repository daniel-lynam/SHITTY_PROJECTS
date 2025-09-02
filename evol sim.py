import random

import pygame
#import time
from pygame.locals import *
import keyboard
import math

pygame.init()
X = 1920
Y = 1080
speed = 1000
size = 10
scrn = pygame.display.set_mode((X, Y))
killSpeed = 50
killZoneSize = [250, 250]
increaseTime = 10
legamnt = 1
numspiders = 10000


def IncrSpd():
    global speed
    speed += 100


def DcrSpd():
    global speed
    if speed != 10:
        speed += -10


class leg():
    def __init__(self, a=None, g1=None, g2=None, l1=None, l2=None):
        if a == None:
            a = (random.uniform(0, 1) * 2 * math.pi)
        if g1 == None:
            g1 = random.uniform(0, 1)
        if g2 == None:
            g2 = random.uniform(0, 1)
        if l1 == None:
            l1 = random.uniform(0, 1)
        if l2 == None:
            l2 = random.uniform(0, 1)
        self.angle = a
        self.g1 = g1
        self.g2 = g2
        self.l1 = l1
        self.l2 = l2

    def move(self):
        move1 = (self.l2 - self.l1) * self.g1
        move2 = (self.l1 - self.l2) * self.g2
        x = 0
        x += move1 * math.cos(self.angle)
        x += move2 * math.cos(self.angle)
        y = 0
        y += move1 * math.sin(self.angle)
        y += move2 * math.sin(self.angle)
        return [x * size, y * size]


class spider():
    def __init__(self):
        self.gen = 0
        self.lega = legamnt
        self.pos = [random.randint(100, Y - 100), random.randint(100, X - 100)]
        self.legs = []
        for i in range(self.lega):
            self.legs.append(leg())

    def walk(self):
        for i in range(len(self.legs)):
            x = self.legs[i].move()[0]
            y = self.legs[i].move()[1]
            self.pos[0] = self.pos[0] + x
            self.pos[1] = self.pos[1] + y
            pass

    def die(self):
        if potentialParents != []:
            parent = random.choice(potentialParents)
            self.lega = parent.lega
            self.pos = parent.pos
            self.legs = []
            self.gen = parent.gen + 1
            for i in range(len(parent.legs)):
                self.legs.append(leg(parent.legs[i].angle * (1 + random.uniform(-0.05, 0.05)),
                                     parent.legs[i].g1 * (1 + random.uniform(-0.05, 0.05)),
                                     parent.legs[i].g2 * (1 + random.uniform(-0.05, 0.05)),
                                     parent.legs[i].l1 * (1 + random.uniform(-0.05, 0.05)),
                                     parent.legs[i].l2 * (1 + random.uniform(-0.05, 0.05))))
        else:
            self.lega = 2
            self.pos = [random.randint(100, Y - 100), random.randint(100, X - 100)]
            self.legs = []
            for i in range(self.lega):
                self.legs.append(leg())

    def getspeed(self):
        pos = [0, 0]
        for i in range(len(self.legs)):
            x = self.legs[i].move()[0]
            y = self.legs[i].move()[1]
            pos[0] = pos[0] + x
            pos[1] = pos[1] + y
        ld = (pos[0] ** 2 + pos[1] ** 2) ** 0.5
        return ld


def increaseAll():
    global killZoneSize
    global killSpeed
    killSpeed = killSpeed * 0.99
    killZoneSize = [int(killZoneSize[0] + (increaseTime / 10)), int(killZoneSize[1] + (increaseTime / 10))]
    for i in allspiders:
        i.pos = [random.randint(100, Y - 100), random.randint(100, X - 100)]


allspiders = []
for i in range(numspiders):
    allspiders.append(spider())
myfont = pygame.font.SysFont("monospace", 45)
spiderSize = pygame.font.SysFont("monospace", 5)
keyboard.add_hotkey('up', IncrSpd)
keyboard.add_hotkey('down', DcrSpd)
potentialParents = []
n = True
mouse_pos = pygame.mouse.get_pos()
print(mouse_pos)
timer = 0
t2 = 0
go = True


def tstop():
    global go
    if go:
        go = False
    else:
        go = True


def setKillZone():
    global xs
    global ys
    global xe
    global ye
    global timer
    based = [random.randint(100, Y - 100), random.randint(100, X - 100)]
    xs = based[1] - killZoneSize[0] / 2
    ys = based[0] - killZoneSize[1] / 2
    xe = based[1] + killZoneSize[0] / 2
    ye = based[0] + killZoneSize[1] / 2
    timer = 0


def killZoneDone():
    global potentialParents
    global t2
    t2 += 1
    potentialParents = []

    for i in allspiders:
        if i.pos[0] > ys and i.pos[0] < ye and i.pos[1] > xs and i.pos[1] < xe:
            i.die()
        else:
            potentialParents.append(i)
    if t2 == increaseTime:
        increaseAll()
        t2 = 0
    setKillZone()


ys = 0
ye = 0
xs = 0
xe = 0

keyboard.add_hotkey('space', setKillZone)
keyboard.add_hotkey('f', tstop)
while n:
    for event in pygame.event.get():
        if event.type == QUIT:
            n = False
    scrn.fill((0, 0, 0))
    if go:
        label = myfont.render(("↓ " + str(speed) + " ↑"), 1, (255, 255, 255))
        scrn.blit(label, (100, 100))
        label = myfont.render(("↓ " + str(int(killSpeed * 10) / 10) + " ↑"), 1, (255, 255, 255))
        scrn.blit(label, (400, 100))
        label = myfont.render(("↓ " + str(killZoneSize) + " ↑"), 1, (255, 255, 255))
        scrn.blit(label, (700, 100))
        for i in allspiders:
            if i.pos[0] > ys and i.pos[0] < ye and i.pos[1] > xs and i.pos[1] < xe:
                i.walk()
            label = spiderSize.render(" <    > ", 1, (255, 255, 255))
            scrn.blit(label, (i.pos[1], i.pos[0]))
        timer += 1
        if timer >= killSpeed:
            killZoneDone()
        pygame.display.flip()
        #time.sleep(100 / speed)
    else:
        scrn.fill((0, 0, 0))
        sspeed = 0
        gen = 0
        bestspi = allspiders[0]
        for i in allspiders:
            if i.gen > gen:
                gen = i.gen
            if abs(i.getspeed()) > sspeed:
                sspeed = abs(i.getspeed())
                bestspi = i

        label = myfont.render(("highest gen = " + str(gen)), 1, (255, 255, 255))
        scrn.blit(label, (100, 100))

        label = myfont.render(("highest speed = " + str(sspeed)), 1, (255, 255, 255))
        scrn.blit(label, (100, 200))
        spistats = []
        for i in bestspi.legs:
            spistats.append(([i.g1, i.l1], [i.g2, i.l2]))

        for i in bestspi.legs:
            pygame.draw.circle(scrn, (120, 120, 120), (X / 6 - (i.move()[0] * 20), Y / 5 * 3 - (i.move()[1] * 20)), 20)
            pygame.draw.line(scrn, (120, 120, 120), [X / 6, Y / 5 * 3],
                             [X / 6 - (i.move()[0] * 20), Y / 5 * 3 - (i.move()[1] * 20)], 5)
        pygame.draw.circle(scrn, (255, 255, 255), (X / 6, Y / 5 * 3), 20)
        label = myfont.render(("speed stats = "), 1, (255, 255, 255))
        scrn.blit(label, (100, 300))
        for i in range(len(spistats)):
            label = myfont.render(("              " + str(spistats[i][0])), 1, (255, 255, 255))
            scrn.blit(label, (100, 300 + 200 * i))
            label = myfont.render(("              " + str(spistats[i][1])), 1, (255, 255, 255))
            scrn.blit(label, (100, 300 + 200 * i + 100))

        pygame.display.flip()