import math
import pygame
import sys


class Planetoid:
    def __init__(self, mass, x, y, angle=0.0, sforce=0):
        self.mass = mass
        self.x = x
        self.y = y
        self.angle = angle
        self.force = sforce
        self.next_step = None

    def next_move(self):
        self.x = self.next_step[0]
        self.y = self.next_step[1]
        self.angle = self.next_step[2]
        self.force = self.next_step[3]
        pass


# imma use degrees
# R2 = F1^2+ F2^2 – 2 F1 F2 Cos ( 180 – θ )


n = True
# while n == True:
#    pass
# F = force(cos(theta))x,
#    force(sin(theta))y

pygame.init()

SCREEN_WIDTH = 1980
SCREEN_HEIGHT = 1080

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("two body problem")

clock = pygame.time.Clock()

# Main loop
planetoids = [Planetoid(3, 490, 540, math.pi * 3/2, 2000)]
planetoids.append(Planetoid(4, 990, 540, math.pi, 0))
planetoids.append(Planetoid(3, 1540, 880, 3, 199))
GC = 5
leeway = 10
physicsspeed = 1
do_stuff = True
running = True
next_frame = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    if do_stuff or next_frame > 0:
        for i in range(len(planetoids)):
            gps = []
            for j in range(len(planetoids)):
                if i == j:
                    pass
                else:
                    gps.append([planetoids[j].mass, planetoids[j].x, planetoids[j].y])

            forceslist = []
            for m in gps:

                ang = math.atan2((m[2] - planetoids[i].y),(m[1] - planetoids[i].x))#r m is the other planet

                force = ((1 / (((planetoids[i].x - m[1]) ** 2) + ((planetoids[i].y - m[2]) ** 2))) * m[0] * GC)
                forceslist.append([force * math.cos(ang), force * math.sin(ang)])  # getting force to planetoid
                if ((((planetoids[i].x - m[1]) ** 2) + ((planetoids[i].y - m[2]) ** 2))**0.5) < leeway:
                    print(f"planet collision occured")


            forceslist.append([planetoids[i].force / 10000 * math.cos(planetoids[i].angle,),
                               planetoids[i].force / 10000 * math.sin(planetoids[i].angle,)])

            fx = 0
            fy = 0

            for k in forceslist:
                fx += k[0]
                fy += k[1]

            planetoids[i].next_step = [planetoids[i].x + fx/physicsspeed, planetoids[i].y + fy/physicsspeed,math.atan2(fy, fx),planetoids[i].force]


            # do next frame effects on i(speed per pysics frame) round(number, 6)

        next_frame = 0

    # ---------------display shit---------------
    for i in range(len(planetoids)):
        pygame.draw.line(screen, (100, 100, 100), (planetoids[i].x, planetoids[i].y),
                         (planetoids[i].x + (math.cos(planetoids[i].angle) * planetoids[i].force),
                          planetoids[i].y + (math.sin(planetoids[i].angle) * planetoids[i].force)))
        pygame.draw.circle(screen, (0, (i + 1) * 20, (i + 1) * 20 ), [planetoids[i].x, planetoids[i].y], 10, 10)
        planetoids[i].next_move()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        if do_stuff:
            do_stuff = False
        else:
            do_stuff = True
    keys = pygame.key.get_pressed()
    if not do_stuff and keys[pygame.K_e]:
        next_frame = 1

    pygame.display.flip()

# Quit PyGame
pygame.quit()
sys.exit()
