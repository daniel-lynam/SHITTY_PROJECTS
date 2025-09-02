import random
import pygame
from pygame.locals import *
import math

pygame.init()
clock = pygame.time.Clock()
class MAP:
    def __init__(self,walles,checkpoints):
        self.walls = walles
        self.checkpoints = checkpoints

#--------------------------- non map constants --------------------------------------
#                              DO NOT CHANGE
MAPs = []
MAPs.append(MAP([((0, 0), (432, 0)), ((420, 0), (0, 0)), ((0, 0), (0, 0)), ((136, 0), (0, 121)), ((0, 121), (0, 734)), ((0, 734), (278, 985)), ((278, 985), (844, 986)), ((844, 986), (1155, 676)), ((1155, 676), (1155, 235)), ((1156, 235), (910, 1)), ((910, 1), (425, 0)), ((394, 9), (288, 218)), ((288, 218), (255, 2)), ((255, 2), (135, 0)), ((293, 220), (287, 614)), ((287, 614), (423, 704)), ((423, 704), (776, 706)), ((776, 706), (905, 445)), ((908, 442), (714, 267)), ((713, 266), (558, 496)), ((293, 208), (292, 226))]
,[((4, 314), (289, 314)), ((286, 526), (0, 558)), ((0, 733), (287, 612)), ((373, 673), (157, 880)), ((366, 986), (427, 707)), ((566, 705), (551, 985)), ((733, 706), (728, 984)), ((790, 682), (985, 842)), ((857, 550), (1161, 675)), ((901, 443), (1155, 441)), ((819, 362), (1056, 139)), ((747, 301), (902, 2)), ((707, 273), (596, 0)), ((668, 330), (335, 121)), ((606, 426), (293, 270)), ((559, 483), (327, 639)), ((580, 467), (592, 702)), ((617, 408), (839, 582)), ((887, 475), (682, 315))]
))
MAPs.append(MAP([((326, 325), (0, 334)), ((0, 0), (0, 334)), ((0, 0), (934, 0)), ((934, 0), (1306, 360)), ((1306, 360), (1324, 867)), ((1324, 867), (956, 1079)), ((0, 241), (80, 334)), ((47, 22), (7, 86)), ((45, 24), (71, 0)), ((12, 80), (0, 113)), ((44, 295), (151, 328)), ((0, 186), (25, 268)), ((321, 325), (843, 340)), ((843, 339), (975, 547)), ((975, 547), (950, 744)), ((951, 1079), (278, 1079)), ((276, 1079), (314, 323)), ((312, 439), (478, 333)), ((484, 1079), (284, 950)), ((950, 742), (784, 856)), ((784, 856), (499, 840)), ((499, 840), (519, 554)), ((519, 554), (722, 567)), ((590, 554), (637, 554))]
, [((315, 326), (329, 0)), ((588, 336), (601, 0)), ((780, 343), (806, 0)), ((847, 349), (1083, 118)), ((953, 509), (1329, 393)), ((968, 630), (1318, 672)), ((948, 740), (1184, 942)), ((840, 822), (952, 1079)), ((676, 853), (646, 1079)), ((504, 842), (352, 1079)), ((499, 770), (291, 743)), ((515, 628), (300, 572)), ((520, 558), (439, 351)), ((612, 550), (626, 331)), ((715, 559), (894, 419)), ((722, 567), (963, 688)), ((711, 569), (715, 852)), ((560, 559), (549, 844))]
))
MAPs.append(MAP([((0, 0), (1919, 0)), ((1919, 0), (1919, 1079)),
                ((1919, 1079), (82, 1079)), ((82, 1079), (0, 1079)), ((0, 1079), (1919, 1079)),
                 ((0, 1079), (0, 0)), ((208, 3), (204, 256)), ((204, 256), (267, 408)),
                 ((267, 408), (192, 549)), ((7, 329), (73, 411)), ((73, 411), (4, 506)),
                 ((191, 547), (260, 759)), ((3, 505), (71, 791)), ((71, 788), (196, 1073)),
                 ((262, 756), (343, 868)), ((345, 866), (486, 888)), ((611, 1079), (842, 1037)),
                 ((842, 1036), (973, 951)), ((973, 951), (1034, 861)), ((1034, 861), (1054, 718)),
                 ((1054, 718), (1013, 617)), ((1013, 617), (898, 544)), ((898, 544), (776, 521)),
                 ((484, 889), (730, 852)), ((730, 852), (793, 811)), ((793, 811), (802, 784)),
                 ((802, 784), (489, 885)), ((782, 518), (547, 662)), ((544, 664), (474, 653)),
                 ((474, 653), (424, 604)), ((424, 604), (442, 3)), ((539, 666), (545, 663)),
                 ((542, 659), (546, 659)), ((547, 660), (547, 660))],
                [((3, 264), (203, 254)), ((237, 326), (75, 408)), ((67, 425), (223, 490)),
                 ((24, 590), (196, 553)), ((66, 779), (261, 752)), ((157, 985), (342, 863))
                    , ((416, 879), (329, 1078)), ((508, 888), (535, 1079)), ((669, 862), (708, 1061)),
                 ((756, 838), (882, 1010)), ((797, 799), (1041, 818)), ((799, 782), (1030, 659)), ((784, 786),
                (897, 548)), ((772, 790), (747, 539)), ((674, 826), (610, 623)), ((536, 865), (534, 666)),
                 ((390, 870), (473, 653)), ((261, 759), (432, 611)), ((192, 556), (424, 569)), ((266, 406),
                (430, 418)), ((208, 254), (434, 266)), ((211, 28), (445, 43))])
)
MAPs.append(MAP([((0, 0), (256, 1)), ((0, 0), (0, 1079)), ((0, 1079), (1919, 1079)), ((1919, 1079), (1919, 0)), ((1919, 0), (0, 0)), ((1, 364), (172, 532)), ((172, 532), (604, 530)), ((226, 7), (220, 199)), ((222, 197), (609, 210)), ((609, 210), (1002, 524)), ((1002, 524), (1024, 1079)), ((602, 533), (624, 1079))]
,[((9, 198), (223, 195)), ((91, 459), (339, 201)), ((385, 201), (376, 534)), ((607, 211), (549, 530)), ((602, 548), (891, 431)), ((607, 636), (1008, 648)), ((607, 787), (1012, 777)), ((614, 909), (1025, 909)), ((625, 1059), (1026, 1058))]
))

wallit = 0
parents = None
TMER = 0
tmsec = 0
cars = []
it = 0 #generation of cars
my_font = pygame.font.SysFont('Comic Sans MS', 30)
king = [-1, 10000000]#compares to this first to find first in line
#------------------------------ MAP LAYOUT ------------------------------------------
#                             DO NOT CHANGE
walls = MAPs[wallit].walls
checkpoints = MAPs[wallit].checkpoints
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920
scrn = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ai end")
lead_node_display_size = (500,300)
lead_node_display_location = (SCREEN_WIDTH-lead_node_display_size[0],SCREEN_HEIGHT)
#------------------------------- VARIABLES -------------------------------------------
#                                 CHANGE
laysize = [5, 4, 3, 2] #first digit should always be 5 last digit should always be two otherwise feel free to alter or add
tickspeed = False #boolean has frame cap [y/n] display of time fucks up if high tps or there is too many calculations to do per tick
tickpersecond = 10 #how many ticks can happen per second max
starting_gen = 100 #how many random cars to start with higher is slower but gives a much better starting point
evo_size = 40 #how many cars are spawned from the best car in the previous generation
turnmult = 0.015 #higher means sharper turns lower means smoother drives but cant turn well
genvariance = 0.8 #genetic diversity lower means small but constant gains
                  #while higher increases the chance for a car to overcome a turn which previous generations struggled with
start_weight_variablility = 8#dont worry bout this for now
data_x=500 #where the data is displayed


wall_width = 10#they should not be able to fuck off now but if they do increase this
#------------------------------------------------------------------------------------

def disline(pos1,pos2,width1):
    if width1 < 0:
        colour = (155,0,0)
    else:
        colour = (155,155,155)
    pygame.draw.line(scrn, colour, pos1, pos2,width=abs(width1)+1)

def display_beams(player_pos, player_angle, show=True):
    player_x = player_pos[0]
    player_y = player_pos[1]
    #if show:
    #    pygame.draw.line(scrn, (155, 155, 155),
    #                     (player_x, player_y),
    #                     (player_x + math.cos(player_angle + math.pi / 2) * 100,
    #                      player_y + math.sin(player_angle + math.pi / 2) * 100))
    XS = 0
    x = player_x
    y = player_y
    s1dis = 0
    while 1 < x < SCREEN_WIDTH - 1 and 1 < y < SCREEN_HEIGHT - 1:
        s1dis += 1
        x += -math.sin(player_angle)
        y += math.cos(player_angle)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255) and show:
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y + XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y + XS), (x, y))
            break
    x = player_x
    y = player_y
    s2dis = 0
    while 1 < x < SCREEN_WIDTH - 1 and 1 < y < SCREEN_HEIGHT - 1:
        s2dis += 1
        x += -math.sin(player_angle + math.pi / 2)
        y += math.cos(player_angle + math.pi / 2)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255) and show:
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y + XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y + XS), (x, y))
            break
    x = player_x
    y = player_y
    s3dis = 0
    while 0 < x < SCREEN_WIDTH - 1 and 0 < y < SCREEN_HEIGHT - 1:
        s3dis += 1
        x += -math.sin(player_angle - math.pi / 2)
        y += math.cos(player_angle - math.pi / 2)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255) and show:
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y + XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y + XS), (x, y))
            break
    x = player_x
    y = player_y
    s4dis = 0
    while 0 < x < SCREEN_WIDTH - 1 and 0 < y < SCREEN_HEIGHT - 1:
        s4dis += 1
        x += -math.sin(player_angle - math.pi / 4)
        y += math.cos(player_angle - math.pi / 4)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255) and show:
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y + XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y + XS), (x, y))
            break
    x = player_x
    y = player_y
    s5dis = 0
    while 0 < x < SCREEN_WIDTH - 1 and 0 < y < SCREEN_HEIGHT - 1:
        s5dis += 1
        x += -math.sin(player_angle + math.pi / 4)
        y += math.cos(player_angle + math.pi / 4)
        if scrn.get_at((int(x), int(y))) == (255, 255, 255) and show:
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y - XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x + XS, y + XS), (x, y))
            pygame.draw.line(scrn, (155, 155, 155), (x - XS, y + XS), (x, y))
            break
    txtlist = [s1dis, s2dis, s3dis, s4dis, s5dis]
    return txtlist


def sigmoid(x):
    return (1 / (1 + (math.e ** (-x))) - 0.5) * 2


def sigmoids(x):
    return (1 / (1 + (math.e ** (-(x / 1000)))) - 0.5) * 2


def discir(x, y, d=False, p=False):
    if d == False and p == True:
        pygame.draw.circle(scrn, (150, 255, 150), (x, y), 20)
    elif not d:
        pygame.draw.circle(scrn, (254, 255, 255), (x, y), 20)
    else:
        if p:
            pygame.draw.circle(scrn, (100, 175, 100), (x, y), 20)
        else:
            pygame.draw.circle(scrn, (100, 100, 100), (x, y), 20)


class end_node:
    def __init__(self):
        self.value = 0


class basic_node:
    def __init__(self, nextlay):
        self.weights = {}
        for i in range(len(nextlay)):
            self.weights[nextlay[i]] = random.uniform(a=-start_weight_variablility, b=start_weight_variablility)
        self.value = 0


class child_node:
    def __init__(self, nextlay, parent_node):
        self.weights = {}
        self.value = 0
        baseweight = list(parent_node.weights.values())
        for i in range(len(nextlay)):
            self.weights[nextlay[i]] = baseweight[i] * random.uniform(1-(genvariance/2), 1+(genvariance/2))


class bcar:
    def __init__(self, parent):
        self.pos = [100, 100]
        self.angle = math.pi * 2
        self.alive = True
        self.chp = 0
        self.front = False
        self.layers = []
        l2 = []
        tl = []
        for i in range(laysize[-1]):
            tl.append(end_node())
        l2.append(tl)

        for i in range(1, len(laysize)):
            tl = []
            for j in range(laysize[-(i + 1)]):
                tl.append(child_node(l2[i - 1], parent.layers[-i - 1][j]))
                pass
            l2.append(tl)

        for i in range(len(l2)):
            self.layers.append(l2[-(i + 1)])

    def next_move(self, show=False):
        if not self.alive:
            display_beams(self.pos, self.angle, show)

            return
        else:
            tla = display_beams(self.pos, self.angle, show)
            for i in range(len(self.layers[0])):
                self.layers[0][i].value = sigmoids(tla[i])
            for i in range(1, len(self.layers)):
                for j in self.layers[i]:
                    j.value = 0

            for i in range(1, len(self.layers)):
                for j in range(len(self.layers[i])):
                    for k in self.layers[i - 1]:
                        self.layers[i][j].value += k.value * k.weights[self.layers[i][j]]  # layer[1][0]

                    self.layers[i][j].value = sigmoid(self.layers[i][j].value)
            turn = (self.layers[-1][1].value - self.layers[-1][0].value) * turnmult

            m = True
            for i in range(5):
                if scrn.get_at(
                        (
                                int(self.pos[0] + -math.sin(self.angle) * i),
                                int(self.pos[1] + math.cos(self.angle) * i))) == (
                        255, 255, 255):
                    m = False
                    self.pos[0] += -math.sin(self.angle) * (i - 1)
                    self.pos[1] += math.cos(self.angle) * (i - 1)
                    break
            if m:
                self.pos[0] += -math.sin(self.angle) * 5
                self.pos[1] += math.cos(self.angle) * 5

            self.angle += turn


class car:
    def __init__(self):
        self.pos = [100, 100]
        self.angle = math.pi * 2
        self.alive = True
        self.chp = 0
        self.front = False
        if parents is None:
            self.layers = []
            l2 = []
            tl = []
            for i in range(laysize[-1]):
                tl.append(end_node())
            l2.append(tl)
            for i in range(len(laysize) - 1):
                tl = []
                for j in range(laysize[-(i + 2)]):
                    tl.append(basic_node(l2[i]))
                    pass
                l2.append(tl)

            for i in range(len(l2)):
                self.layers.append(l2[-(i + 1)])

    def next_move(self, show=False):
        if not self.alive:
            display_beams(self.pos, self.angle, show)

            return
        else:
            tla = display_beams(self.pos, self.angle, show)
            for i in range(len(self.layers[0])):
                self.layers[0][i].value = sigmoids(tla[i])
            for i in range(1, len(self.layers)):
                for j in self.layers[i]:
                    j.value = 0

            for i in range(1, len(self.layers)):
                for j in range(len(self.layers[i])):
                    for k in self.layers[i - 1]:
                        self.layers[i][j].value += k.value * k.weights[self.layers[i][j]]

                    self.layers[i][j].value = sigmoid(self.layers[i][j].value)
            turn = (self.layers[-1][1].value - self.layers[-1][0].value) * turnmult

            m = True
            for i in range(5):
                if scrn.get_at(
                        (
                                int(self.pos[0] + -math.sin(self.angle) * i),
                                int(self.pos[1] + math.cos(self.angle) * i))) == (
                        255, 255, 255):
                    m = False
                    self.pos[0] += -math.sin(self.angle) * (i - 1)
                    self.pos[1] += math.cos(self.angle) * (i - 1)
                    break
            if m:
                self.pos[0] += -math.sin(self.angle) * 5
                self.pos[1] += math.cos(self.angle) * 5

            self.angle += turn


for i in range(starting_gen):
    cars.append(car())
pygame.font.init()

n = True
while n:
    for event in pygame.event.get():
        if event.type == QUIT:
            n = False
    scrn.fill((0, 0, 0))

    p = 0
    for i in checkpoints:
        pygame.draw.line(scrn, (0, 255 - p, 0), i[0], i[1], width=15)
        p += 1

    for i in walls:
        pygame.draw.line(scrn, (255, 255, 255), i[0], i[1], wall_width)
    m = True
    tbd = []
    for i in range(len(cars)):
        if scrn.get_at((int(cars[i].pos[0]), int(cars[i].pos[1]))) == (255, 255, 255):
            cars[i].alive = False
        if scrn.get_at((int(cars[i].pos[0]), int(cars[i].pos[1]))) == (0, 255 - cars[i].chp, 0):
            cars[i].chp += 1
            if cars[i].chp == p:
                m=False
                print(f"the map was solved in {it} generations by car{i}")
                wallit += 1
                if wallit == len(MAPs):
                    n = False
                    break
                walls = MAPs[wallit].walls
                checkpoints = MAPs[wallit].checkpoints
                for i in cars:
                    i.chp = 0
                break
        if cars[i].alive:
            cars[i].next_move(True)
            # discir(cars[i].pos[0], cars[i].pos[1])
    if not n:
        print("all maps solved")
        break
    tk = cars[0]
    king = [-1, 10000000]
    for i in range(len(cars)):
        cars[i].front = False
        dckp = [(checkpoints[cars[i].chp][0][0] + checkpoints[cars[i].chp][1][0]) / 2,
                (checkpoints[cars[i].chp][0][1] + checkpoints[cars[i].chp][1][1]) / 2]
        if (cars[i].chp > king[0]                                               #is further then cur lead
                or ((cars[i].chp == king[0])                                    #if its on the same checkpoint as lead
                and ((cars[i].pos[0] - dckp[0]) ** 2 + (cars[i].pos[1] - dckp[1]) ** 2) < king[1])): #distance to chp
            king = [cars[i].chp, (cars[i].pos[0] - dckp[0]) ** 2 + (cars[i].pos[1] - dckp[1]) ** 2]
            tk = cars[i]
    tk.front = True
    for i in range(len(cars)):
        if not cars[i].alive:

            discir(cars[i].pos[0], cars[i].pos[1], d=True, p=cars[i].front)
        else:

            discir(cars[i].pos[0], cars[i].pos[1], p=cars[i].front)
    if not m:
        cars = []
        tk.pos = [100, 100]
        tk.angle = math.pi * 2
        tk.alive = True
        tk.chp = 0
        tk.front = False
        it += 1
        cars.append(tk)
        for i in range(evo_size):
            cars.append(bcar(tk))  # Next gen tk = KING
        cars.append(car())
        continue
    for i in range(len(cars)):
        pass

    cc = True
    for i in range(len(cars)):
        if cars[i].alive:
            cc = False
            break
    if cc:
        cars = []
        tk.pos = [100, 100]
        tk.angle = math.pi * 2
        tk.alive = True
        tk.chp = 0
        tk.front = False
        it += 1
        cars.append(tk)
        for i in range(evo_size):
            cars.append(bcar(tk))  # Next gen tk = KING
        cars.append(car())
    text_surface = my_font.render(f"iteration: {it}", False, (244, 244, 255))
    scrn.blit(text_surface, (data_x, 0))
    if tickspeed:
        text_surface = my_font.render(f"time(seconds): {tmsec}", False, (244, 244, 255))
        scrn.blit(text_surface, (data_x, 100))
    else:
        text_surface = my_font.render(f"time(seconds): NAN", False, (244, 244, 255))
        scrn.blit(text_surface, (data_x, 100))
    for i in range(len(tk.layers) - 1):

        for j in range(len(tk.layers[i])):  # start pos
            startpos = (
            ((lead_node_display_size[0] / (len(tk.layers) + 1)) * (i + 1))+SCREEN_WIDTH-lead_node_display_size[0], (lead_node_display_size[1] / (len(tk.layers[i]) + 1)) * (j + 1))
            for k in range(len(tk.layers[i + 1])):  # end pos
                endpos = (lead_node_display_size[0] / (len(tk.layers) + 1)) * (i + 2)+SCREEN_WIDTH-lead_node_display_size[0], lead_node_display_size[1] / (len(tk.layers[i + 1]) + 1) * (
                            k + 1)
                w2 = tk.layers[i][j].weights[tk.layers[i + 1][k]]

                disline(startpos, endpos, int(w2))
    pygame.display.flip()
    TMER += 1
    if TMER == tickpersecond:
        TMER = 0
        tmsec += 1
    if tickspeed:
        clock.tick(tickpersecond)
