#on start rando entry
#each gen
#   ttl cars = []
#   if gen parents is empty
#       add random cars to list
#   else make near perfect genetic copies of the gen parents combined and divided
import random

import pygame
from pygame.locals import *
import math

pygame.init()
clock = pygame.time.Clock()
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
laysize = [5,4,3,2]
scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ai display")
def sigmoid(x):
    return (1 / (1 + (math.e ** (-(x)))) - 0.5) * 2
def discir(x,y):
    pygame.draw.circle(scrn, (255, 255, 255), (x, y), 20)
def disline(pos1,pos2,width1):
    if width1 < 0:
        colour = (155,0,0)
    else:
        colour = (155,155,155)
    pygame.draw.line(scrn, colour, pos1, pos2,width=abs(width1)+1)
class end_node:
    def __init__(self):
        self.value = 0



class basic_node:
    def __init__(self,nextlay):
        self.weights = {}
        for i in range(len(nextlay)):
            self.weights[nextlay[i]] = random.uniform(a=-8,b=8)
        self.value = 0


layers = []
l2 = []
tl = []
for i in range(laysize[-1]):
    tl.append(end_node())
l2.append(tl)
for i in range(len(laysize)-1):
    tl = []
    for j in range(laysize[-(i+2)]):
        tl.append(basic_node(l2[i]))
        pass
    l2.append(tl)

for i in range(len(l2)):
    layers.append(l2[-(i+1)])
for i in range(len(layers[0])):
    if i <3:
        layers[0][i].value = 1
    else:
        layers[0][i].value = 0
n = True


turnMULT = 0.3

while n:

    for event in pygame.event.get():
        if event.type == QUIT:
            n = False
    scrn.fill((0, 0, 0))

    for i in range(len(layers)-1):

        for j in range(len(layers[i])):#start pos
            startpos = (((SCREEN_WIDTH/(len(layers)+1))*(i+1)),(SCREEN_HEIGHT/(len(layers[i])+1))*(j+1))
            for k in range(len(layers[i+1])):#end pos
                endpos = (SCREEN_WIDTH/(len(layers)+1))*(i+2),SCREEN_HEIGHT/(len(layers[i+1])+1)*(k+1)
                w2 = layers[i][j].weights[layers[i+1][k]]

                disline(startpos,endpos,int(w2))

    for i in range(len(layers)):
        for j in range(len(layers[i])):
            discir(((SCREEN_WIDTH/(len(layers)+1))*(i+1)),(SCREEN_HEIGHT/(len(layers[i])+1))*(j+1))

    for i in layers[0]:
        i.value = 1
    for i in range(1,len(layers)):
        for j in layers[i]:
            j.value = 0




    for i in range(1,len(layers)):
        for j in range(len(layers[i])):
            for k in layers[i-1]:
                layers[i][j].value += k.value*k.weights[layers[i][j]]

            layers[i][j].value = sigmoid(layers[i][j].value)

    print(f"base val left{layers[-1][0].value}")
    print(f"sig val left{sigmoid(layers[-1][0].value)}")
    print(f"base val right{layers[-1][1].value}")
    print(f"sig val right{sigmoid(layers[-1][1].value)}")
    turn = sigmoid(layers[-1][1].value)-sigmoid(layers[-1][0].value)*turnMULT
    print(round(turn,4))
    pygame.display.flip()
    clock.tick(1)