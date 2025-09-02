import random
layer1 =  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
layer2 =  [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1]
layer3 =  [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1]
layer4 =  [1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,1,0,1]
layer5 =  [1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1]
layer6 =  [1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1]
layer7 =  [1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1]
layer8 =  [1,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1]
layer9 =  [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,1]
layer10 = [1,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1]
layer11 = [1,0,1,1,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,0,1]
layer12 = [1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,1]
layer13 = [1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1]
layer14 = [1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1]
layer15 = [1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1]
layer16 = [1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,1]
layer17 = [1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,0,1,1,1]
layer18 = [1,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1]
layer19 = [1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1]
layer20 = [1,'x',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
layer21 = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
map = [layer1,
       layer2,
       layer3,
       layer4,
       layer5,
       layer6,
       layer7,
       layer8,
       layer9,
       layer10,
       layer11,
       layer12,
       layer13,
       layer14,
       layer15,
       layer16,
       layer17,
       layer18,
       layer19,
       layer20,
       layer21
       ]
#for i in map:
    #print(i)
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 'x':
            DroneY = i
            DroneX = j


def Move(direction):
    global DroneY
    global DroneX
    if direction == "w":
        if map[DroneY-1][DroneX] == 1:
            print("\n \n")
            return False
        else:
            map[DroneY][DroneX] = 0
            map[DroneY-2][DroneX] = "x"
            DroneY = DroneY-2
    if direction == "s":
        if map[DroneY+1][DroneX] == 1:
            print("\n \n")
            return False
        else:
            map[DroneY][DroneX] = 0
            map[DroneY+2][DroneX] = "x"
            DroneY = DroneY+2
    if direction == "d":
        if map[DroneY][DroneX+1] == 1:
            print("\n \n")
            return False
        else:
            map[DroneY][DroneX] = 0
            map[DroneY][DroneX+2] = "x"
            DroneX = DroneX+2
    if direction == "a":
        if map[DroneY][DroneX-1] == 1:
            print("\n \n")
            return False
        else:
            map[DroneY][DroneX] = 0
            map[DroneY][DroneX-2] = "x"
            DroneX = DroneX-2
    for i in map:
        print(i)
    print("\n \n")
    return True


score = 0
TreasureY = (random.randint(1,10)*2)-1
TreasureX = (random.randint(1,10)*2)-1


def check_if_treasure():
    global score
    global TreasureX
    global TreasureY
    if DroneY == TreasureY and DroneX == TreasureX:
        score += 1
        TreasureY = (random.randint(1, 10) * 2) - 1
        TreasureX = (random.randint(1, 10) * 2) - 1
        return True

for i in map:
    print(i)
print("\n \n")

forward = "w"

left = {"w":"a","a":"s","s":"d","d":"w"}
right = {"a":"w","s":"a","d":"s","w":"d"}
reverse = {"w":"s","s":"w","a":"d","d":"a"}
n = True
turn = 0
#while n == True:
for j in range(10000):
    directions = [left[forward],forward,right[forward],reverse[forward]]
    for i in directions:
        if Move(i):
            turn += 1
            forward = i
            if check_if_treasure():
                #n = False
                pass


            break
print("it found " + str(score) + " treasure")
print("it took " + str(turn) +" turns")
print(str(TreasureY) + " " + str(TreasureX))