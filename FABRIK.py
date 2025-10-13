import pygame
import math
pygame.init()


WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("FABRIK Algorithm")


fps = 30
leg_scale = 1
lengths = [96*leg_scale,60*leg_scale,305*leg_scale,116*leg_scale,205*leg_scale,146*leg_scale,61*leg_scale,0]
target_angles = [0]*(len(lengths))
curent_angles = [0]*(len(lengths))
global_angles = [0]*(len(lengths))
thickness = [14,10,7,7,7,7,7,7]
TOLERANCE = 1.0

chain = []
last_pos = (WIDTH // 2, HEIGHT // 2)
chain.append(last_pos)

for i in range(len(lengths)):
    last_pos = (last_pos[0]+math.sin(curent_angles[i])*lengths[i],last_pos[1]+math.cos(curent_angles[i])*lengths[i])
    chain.append(last_pos)



def midpoint(pos1, pos2, per):
    return [pos1[0] + (pos2[0] - pos1[0]) * per, pos1[1] + (pos2[1] - pos1[1]) * per]




def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def fabrik(chain, target):
    chain[-1] = target
    for i in range(len(chain) - 2, -1, -1):
        direction = (
            (chain[i][0] - chain[i + 1][0]),
            (chain[i][1] - chain[i + 1][1]),
        )
        length = distance(chain[i], chain[i + 1])
        scale = lengths[i] / (length+0.00001)
        chain[i] = (
            chain[i + 1][0] + direction[0] * scale,
            chain[i + 1][1] + direction[1] * scale,
        )
    chain[0] = (WIDTH // 2, HEIGHT // 2)  # Anchor point
    for i in range(1, len(chain)):
        direction = (
            (chain[i][0] - chain[i - 1][0]),
            (chain[i][1] - chain[i - 1][1]),
        )
        length = distance(chain[i], chain[i - 1])
        scale = lengths[i - 1] / (length+0.00001)
        chain[i] = (
            chain[i - 1][0] + direction[0] * scale,
            chain[i - 1][1] + direction[1] * scale,
        )

def normalise_angle(angle):
    return (angle + math.pi) % (2 * math.pi) - math.pi

def get_true_point():
    temppoints = chain
    while len(temppoints) > 1:
        ttp = []
        for i in range(len(temppoints) - 1):
            ttp.append(midpoint(temppoints[i], temppoints[i + 1], t))
        temppoints = ttp
    return temppoints[0]


ffp = 0
my_font = pygame.font.SysFont('Papyrus MS', 30)
procact = False
running = True
clock = pygame.time.Clock()
target = (WIDTH // 2, HEIGHT // 2)
selected_seg = 0

bonus_data = ""
bonus_data2 = ""
bonus_data3 = ""
bonus_data4 = ""

curent_angles[0] = math.atan2(chain[1][1] - chain[0][1], chain[1][0] - chain[0][0])
for i in range(1, len(curent_angles)):
    curent_angles[i] = math.atan2(chain[i + 1][1] - chain[i][1],
                                  chain[i + 1][0] - chain[i][0])
global_angles = curent_angles
print(global_angles)

templist = []
templist.append(normalise_angle(curent_angles[0]))
for i in range(1, len(curent_angles)):
    templist.append(normalise_angle(curent_angles[i] - curent_angles[i - 1]))
curent_angles = templist
manang = [chain[0]]
for i in range(len(chain) - 1):



    angle = sum(curent_angles[:i+1])
    ep = (manang[i][0]+math.cos(angle)*lengths[i],manang[i][1]+math.sin(angle)*lengths[i])
    manang.append(ep)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                if ffp <= 0:
                    procact = not(procact)
                    selected_seg = 0
                    if procact == False:

                        curent_angles[0] = math.atan2(chain[1][1] - chain[0][1], chain[1][0] - chain[0][0])
                        for i in range(1, len(curent_angles)):
                            curent_angles[i] = math.atan2(chain[i + 1][1] - chain[i][1],
                                                          chain[i + 1][0] - chain[i][0])
                        global_angles = curent_angles
                        print(global_angles)

                        templist = []
                        templist.append(normalise_angle(curent_angles[0]))
                        for i in range(1, len(curent_angles)):
                            templist.append(normalise_angle(curent_angles[i] - curent_angles[i - 1]))
                        curent_angles = templist

            if keys[pygame.K_w]:
                selected_seg += 1
                selected_seg %= len(lengths)-1

            if keys[pygame.K_s]:
                if selected_seg == 0:
                    selected_seg = len(lengths)-2
                selected_seg -= 1

            if keys[pygame.K_e]:
                target_angles = []
                for i in curent_angles:
                    target_angles.append(normalise_angle(i))

            if keys[pygame.K_f]:
                procact = False
                ffp = fps

        elif event.type == pygame.MOUSEMOTION:
            target = event.pos


    if not procact:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:
            curent_angles[selected_seg] += 0.05
            curent_angles[selected_seg] = normalise_angle(curent_angles[selected_seg])
        if keys[pygame.K_a]:
            curent_angles[selected_seg] -= 0.05
            curent_angles[selected_seg] = normalise_angle(curent_angles[selected_seg])

    screen.fill((0,0,0))

    t = 0
    #while t < 1:
    #    tc = get_true_point()
    #    screen.set_at((round(tc[0]), round(tc[1])), (255, 255, 255))
    #    t += 0.001

    bonus_data4 = "target angles:   "
    for i in target_angles:
        bonus_data4 += f"{round(i,3)}    "


    if procact:
        pygame.draw.circle(screen, (155,0,0), target, 8)  # Draw target
        text_surface = my_font.render("mode: procedural", False, (244, 244, 255))
        curent_angles[0] = math.atan2(chain[1][1] - chain[0][1], chain[1][0] - chain[0][0])

        for i in range(1, len(curent_angles)):
            curent_angles[i] = math.atan2(chain[i + 1][1] - chain[i][1],
                                          chain[i + 1][0] - chain[i][0])
        global_angles = curent_angles

        templist = []
        templist.append(normalise_angle(curent_angles[0]))
        for i in range(1, len(curent_angles)):
            templist.append(normalise_angle(curent_angles[i] - curent_angles[i - 1]))
        curent_angles = templist

        if distance(chain[-1], target) > TOLERANCE:
            fabrik(chain, target)

    else:
        chain = manang
        text_surface = my_font.render(f"mode: manual -- selected segment: {selected_seg}", False, (244, 244, 255))

    bonus_data = "current point coords:    "
    for i in chain:
        bonus_data += str((int(i[0]),int(i[1])))

    screen.blit(text_surface, (300, 0))

    bonus_data2 = "current relative angles:    "
    for i in curent_angles:
        bonus_data2 += str(round(i,3)) + "  "

    bonus_data3 = "difference in angles:    "
    if ffp <= 0:
        difs = []
        for i in range(len(curent_angles)):
            dif = (target_angles[i]-curent_angles[i])
            difs.append(dif)
            bonus_data3 += f"{round(dif,3)},  "

    if ffp > 0:
        for i in range(len(curent_angles)):
            curent_angles[i] += difs[i]/fps
        ffp -= 1




    manang = [chain[0]]
    for i in range(len(chain) - 1):
        pygame.draw.line(screen, (0,0,144), chain[i], chain[i + 1], 8)  # Draw segments
        pygame.draw.circle(screen, (144,144,144), (int(chain[i][0]), int(chain[i][1])), 5)



        angle = sum(curent_angles[:i+1])
        ep = (manang[i][0]+math.cos(angle)*lengths[i],manang[i][1]+math.sin(angle)*lengths[i])
        manang.append(ep)
        pygame.draw.line(screen, (133, 0, 144), manang[i], ep, thickness[i])  # Draw segments
        pygame.draw.circle(screen, (244, 144, 144), ep, 3)




    text_surface = my_font.render(bonus_data, False, (244, 244, 255))
    screen.blit(text_surface, (300, 100))
    text_surface = my_font.render(bonus_data2, False, (244, 244, 255))
    screen.blit(text_surface, (300, 140))
    text_surface = my_font.render(bonus_data3, False, (244, 244, 255))
    screen.blit(text_surface, (300, 180))
    text_surface = my_font.render(bonus_data4, False, (244, 244, 255))
    screen.blit(text_surface, (300, 220))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()




