import tkinter as tk
import time
import random
list1 =  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
list2 =  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
list3 =  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list4 =  [1, "p", 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, "p", 1]
list5 =  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list6 =  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
list7 =  [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list8 =  [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list9 =  [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
list10 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list11 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list12 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list13 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,'b','b', 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list14 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,'r','r','r','r','r','r', 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list15 = ['w','w','w','w','w','w', 0, 0, 0, 0, 1,'r','r','r','r','r','r', 1, 0, 0, 0, 0, 'w','w','w','w','w','w']
list16 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1,'r','r','r','r','r','r', 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list17 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list18 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list19 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list20 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
list21 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
list22 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list23 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
list24 = [1, "p", 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, "p", 1]
list25 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
list26 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
list27 = [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
list28 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
list29 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
list30 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
list31 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
lvl = 0
homey = 11
homex = 13
gmap = [list1, list2, list3, list4, list5, list6, list7,
        list8, list9, list10, list11, list12, list13,
        list14, list15, list16, list17, list18, list19,
        list20, list21, list22, list23, list24, list25,
        list26, list27, list28, list29, list30, list31]
root = tk.Tk()
for i in range(len(gmap[0])):
    if i < 3:
        label = tk.Label(root, text="     ", bg="orange")
    else:
        label = tk.Label(root, text="     ", bg="black")
    label.grid(row=31, column=i)
for i in range(len(gmap)):
    for j in range(len(gmap[i])):
        if gmap[i][j] == 0:
            label = tk.Label(root, text="     ", bg="yellow")
        elif gmap[i][j] == 1:
            label = tk.Label(root, text="     ", bg="Black")
        elif gmap[i][j] == 'w':
            label = tk.Label(root, text="     ", bg="white")
        elif gmap[i][j] == "b":
            label = tk.Label(root, text="     ", bg="brown")
        elif gmap[i][j] == "p":
            label = tk.Label(root, text="     ", bg="teal")
        else:
            label = tk.Label(root, text="     ", bg="purple")
        label.grid(row=i, column=j)
huntmode = False
redy = 11
redx = 13
pinky = 11
pinkx = 14
cyany = 11
cyanx = 15
orangey = 11
orangex = 16

rscared = False
pscared = False
cscared = False
oscared = False

rdead = False
pdead = False
cdead = False
odead = False

lredm = None
lpinkm = None
lcyanm = None
lorangem = None
inversemove = {"up":"down","down":"up","left":"right","right":"left"}

redfy = -4
redfx = 25

pinkfy = -4
pinkfx = 2

cyanfy = 31
cyanfx = 27

orangefy = 31
orangefx = 0

play = True
def reset():
    global redy
    global redx
    global pinkx
    global pinky
    global cyany
    global cyanx
    global orangex
    global orangey
    global lcyanm
    global lredm
    global lpinkm
    global pposy
    global pposx
    global lorangem
    global rdead
    global pdead
    global cdead
    global odead
    label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pposy, column=pposx)
    if gmap[redy][redx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[redy][redx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=redy, column=redx)
    if gmap[pinky][pinkx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[pinky][pinkx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pinky, column=pinkx)
    if gmap[cyany][cyanx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[cyany][cyanx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=cyany, column=cyanx)
    if gmap[orangey][orangex] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[orangey][orangex] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=orangey, column=orangex)
    redy = 11
    redx = 13
    pinky = 11
    pinkx = 14
    cyany = 11
    cyanx = 15
    orangey = 11
    orangex = 16
    pposy = 23
    pposx = 14
    lredm = None
    lpinkm = None
    lcyanm = None
    lorangem = None
    label = tk.Label(root, text="     ", bg="crimson")
    label.grid(row=redy, column=redx)
    label = tk.Label(root, text="     ", bg="pink")
    label.grid(row=pinky, column=pinkx)
    label = tk.Label(root, text="     ", bg="cyan")
    label.grid(row=cyany, column=cyanx)
    label = tk.Label(root, text="     ", bg="purple")
    label.grid(row=orangey, column=orangex)


    play = False
    time.sleep(1)
    play = True

def nextlevel():
    if True:
        global lvl
        global gmap
        global list1
        global list2
        global list3
        global list4
        global list5
        global list6
        global list7
        global list8
        global list9
        global list10
        global list11
        global list12
        global list13
        global list14
        global list15
        global list16
        global list17
        global list18
        global list19
        global list20
        global list21
        global list22
        global list23
        global list24
        global list25
        global list26
        global list27
        global list28
        global list29
        global list30
        global list31
        global redy
        global redx
        global pinkx
        global pinky
        global cyany
        global cyanx
        global orangex
        global orangey
        global lcyanm
        global lredm
        global lpinkm
        global pposy
        global pposx
        global lorangem
        global rdead
        global pdead
        global cdead
        global odead
        global enemyspeed
        global playerspeed

    if True:
        list1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        list2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        list3 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list4 = [1, "p", 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, "p", 1]
        list5 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list6 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        list7 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list8 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list9 = [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
        list10 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list11 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list12 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list13 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 'b', 'b', 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list14 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 'r', 'r', 'r', 'r', 'r', 'r', 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list15 = ['w', 'w', 'w', 'w', 'w', 'w', 0, 0, 0, 0, 1, 'r', 'r', 'r', 'r', 'r', 'r', 1, 0, 0, 0, 0, 'w', 'w', 'w',
                  'w', 'w', 'w']
        list16 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 'r', 'r', 'r', 'r', 'r', 'r', 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list17 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list18 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list19 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list20 = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1]
        list21 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        list22 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list23 = [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1]
        list24 = [1, "p", 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, "p", 1]
        list25 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
        list26 = [1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
        list27 = [1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1]
        list28 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        list29 = [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
        list30 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        list31 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


        gmap = [list1, list2, list3, list4, list5, list6, list7,
                list8, list9, list10, list11, list12, list13,
                list14, list15, list16, list17, list18, list19,
                list20, list21, list22, list23, list24, list25,
                list26, list27, list28, list29, list30, list31]
    label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pposy, column=pposx)
    if gmap[redy][redx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[redy][redx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=redy, column=redx)
    if gmap[pinky][pinkx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[pinky][pinkx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pinky, column=pinkx)
    if gmap[cyany][cyanx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[cyany][cyanx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=cyany, column=cyanx)
    if gmap[orangey][orangex] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[orangey][orangex] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=orangey, column=orangex)
    redy = 11
    redx = 13
    pinky = 11
    pinkx = 14
    cyany = 11
    cyanx = 15
    orangey = 11
    orangex = 16
    pposy = 23
    pposx = 14
    lvl += 1
    playerspeed += 0
    enemyspeed += 0
    for i in range(len(gmap)):
        for j in range(len(gmap[i])):
            if gmap[i][j] == 0:

                label = tk.Label(root, text="     ", bg="yellow")

            elif gmap[i][j] == 1:


                continue
            elif gmap[i][j] == 'w':
                continue
            elif gmap[i][j] == "b":
                continue
            elif gmap[i][j] == "p":
                label = tk.Label(root, text="     ", bg="teal")
            else:
                continue
            label.grid(row=i, column=j)

def got_killed(py,px,ey,ex):
    global lives
    global play
    if py == ey and px == ex:
        print("\n\n\n\n\n\n")
        lives -= 1
        if lives == 2:
            label = tk.Label(root, text="     ", bg="black")
            label.grid(row=31, column=2)
        elif lives == 1:
            label = tk.Label(root, text="     ", bg="black")
            label.grid(row=31, column=1)

        print("lives: " + str(lives))
        reset()
    if lives <= 0:
        play = False
        time.sleep(1)
        root.destroy()
    pass


enemyspeed = 250
playerspeed = 200
chasetime = 7
lives = 3
gametime = 0
score = 0
scatter = False
def scatterconstant():
    global gametime
    global scatter
    gametime += 1
    if gametime > 25:
        gametime = 0
    if gametime%25 > 20+lvl:
        scatter = True
    else:
        scatter = False
    root.after(1000, scatterconstant)
def constant():
    print(score)
    if func6():
        nextlevel()


    if pscared != True:
        got_killed(pposy, pposx, pinky, pinkx)
    else:
        goteaten(pinky, pinkx, "pink")
    if rscared != True:
        got_killed(pposy, pposx, redy, redx)
    else:
        goteaten(redy, redx, "red")
    if oscared != True:
        got_killed(pposy, pposx, orangey, orangex)
    else:
        goteaten(orangey, orangex, "orange")
    if cscared != True:
        got_killed(pposy, pposx, cyany, cyanx)
    else:
        goteaten(cyany, cyanx, "cyan")
    if play == True:
        move()
    root.after(playerspeed, constant)

def econstant():

    if play == True:
        emove()
    root.after(enemyspeed, econstant)


def scattermove(ghost):
    moves = []
    if ghost == "pink":
        targety = pinkfy
        targetx = pinkfx
        y = pinky
        x = pinkx
    elif ghost == "red":
        targety = redfy
        targetx = redfx
        y = redy
        x = redx
    elif ghost == "cyan":
        targety = cyanfy
        targetx = cyanfx
        y = cyany
        x = cyanx
    else:
        targety = orangefy
        targetx = orangefx
        y = orangey
        x = orangex
    if gmap[y - 1][x] not in [1, "b", "r"]:
        moves.append("up")
    if x == 0 or gmap[y][x - 1] not in [1, "b", "r"]:
        moves.append("left")
    if gmap[y + 1][x] not in [1, "b", "r"]:
        moves.append("down")
    if x == len(gmap[0]) - 1 or gmap[y][x + 1] not in [1, "b", "r"]:
        moves.append("right")
    if ghost == "red":
        if lredm != None:
            if inversemove[lredm] in moves:
                moves.remove(inversemove[lredm])
    if ghost == "pink":
        if lpinkm != None:
            if inversemove[lpinkm] in moves:
                moves.remove(inversemove[lpinkm])
    if ghost == "cyan":
        if lcyanm != None:
            if inversemove[lcyanm] in moves:
                moves.remove(inversemove[lcyanm])
    if ghost == "orange":
        if lorangem != None:
            if inversemove[lorangem] in moves:
                moves.remove(inversemove[lorangem])
    minimum = 10000
    curbest = None
    for i in moves:
        if i == "up":
            if ((y - 1 - targety) ** 2) + ((x - targetx) ** 2) < minimum:
                minimum = ((y - 1 - targety) ** 2) + ((x - targetx) ** 2)
                curbest = i
        elif i == "left":
            if ((y - targety) ** 2) + ((x - 1 - targetx) ** 2) < minimum:
                minimum = ((y - targety) ** 2) + ((x - 1 - targetx) ** 2)
                curbest = i
        elif i == "down":
            if ((y + 1 - targety) ** 2) + ((x - targetx) ** 2) < minimum:
                minimum = ((y + 1 - targety) ** 2) + ((x - targetx) ** 2)
                curbest = i
        elif i == "right":
            if ((y - targety) ** 2) + ((x + 1 - targetx) ** 2) < minimum:
                minimum = ((y - targety) ** 2) + ((x + 1 - targetx) ** 2)
                curbest = i
    return curbest

def scaredmove(y,x,ghost):
    moves = []
    if gmap[y - 1][x] not in [1, "b", "r"]:
        moves.append("up")
    if x == 0 or gmap[y][x - 1] not in [1, "b", "r"]:
        moves.append("left")
    if gmap[y + 1][x] not in [1, "b", "r"]:
        moves.append("down")
    if x == len(gmap[0]) - 1 or gmap[y][x + 1] not in [1, "b", "r"]:
        moves.append("right")
    if ghost == "red":
        if lredm != None:
            if inversemove[lredm] in moves:
                moves.remove(inversemove[lredm])
    if ghost == "pink":
        if lpinkm != None:
            if inversemove[lpinkm] in moves:
                moves.remove(inversemove[lpinkm])
    if ghost == "cyan":
        if lcyanm != None:
            if inversemove[lcyanm] in moves:
                moves.remove(inversemove[lcyanm])
    if ghost == "orange":
        if lorangem != None:
            if inversemove[lorangem] in moves:
                moves.remove(inversemove[lorangem])
    return random.choice(moves)

    pass

def chaseend():
    global huntmode
    global rscared
    global pscared
    global cscared
    global oscared
    rscared = False
    pscared = False
    cscared = False
    oscared = False
    huntmode = False

chasedurationtotal = 0
def chasecount():

    global chasedurationtotal
    if chasedurationtotal > 0:
        chasedurationtotal =chasedurationtotal - 1
        print(chasedurationtotal)
        root.after(1000, chasecount)
    else:
        chaseend()


def chase():
    global redy
    global redx
    global pinkx
    global pinky
    global cyany
    global cyanx
    global orangex
    global orangey
    global lcyanm
    global lredm
    global lpinkm
    global lorangem
    global chasedurationtotal
    global huntmode
    global rscared
    global pscared
    global cscared
    global oscared
    chasedurationtotal += chasetime
    rscared = True
    pscared = True
    cscared = True
    oscared = True
    huntmode = True

    if gmap[redy][redx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    elif gmap[redy][redx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=redy, column=redx)
    nmove = inversemove[lredm]
    if nmove == "up":
        redy = redy-1
    if nmove == "down":
        redy = redy+1
    if nmove == "left":
        if redx != 0:
            redx = redx-1
        else:
            redx = len(gmap[0])-1
    if nmove == "right":
        if redx != len(gmap[0])-1:
            redx = redx+1
        else:
            redx = 0

    label = tk.Label(root, text="     ", bg="crimson")
    label.grid(row=redy, column=redx)

    lredm = nmove

    if gmap[pinky][pinkx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    elif gmap[pinky][pinkx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pinky, column=pinkx)

    nmove = inversemove[lpinkm]
    if nmove == "up":
        pinky = pinky-1
    if nmove == "down":
        pinky = pinky+1
    if nmove == "left":
        if pinkx != 0:
            pinkx = pinkx-1
        else:
            pinkx = len(gmap[0])-1
    if nmove == "right":
        if pinkx != len(gmap[0])-1:
            pinkx = pinkx+1
        else:
            pinkx = 0

    label = tk.Label(root, text="     ", bg="pink")
    label.grid(row=pinky, column=pinkx)

    lpinkm = nmove

    if gmap[orangey][orangex] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[orangey][orangex] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=orangey, column=orangex)

    nmove = inversemove[lorangem]
    if nmove == "up":
        orangey = orangey-1
    if nmove == "down":
        orangey = orangey+1
    if nmove == "left":
        if orangex != 0:
            orangex = orangex-1
        else:
            orangex = len(gmap[0])-1
    if nmove == "right":
        if orangex != len(gmap[0])-1:
            orangex = orangex+1
        else:
            orangex = 0
    lorangem = nmove

    label = tk.Label(root, text="     ", bg="purple")
    label.grid(row=orangey, column=orangex)

    if gmap[cyany][cyanx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[cyany][cyanx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=cyany, column=cyanx)

    nmove = inversemove[lcyanm]
    if nmove == "up":
        cyany = cyany-1
    if nmove == "down":
        cyany = cyany+1
    if nmove == "left":
        if cyanx != 0:
            cyanx = cyanx-1
        else:
            cyanx = len(gmap[0])-1
    if nmove == "right":
        if cyanx != len(gmap[0])-1:
            cyanx = cyanx+1
        else:
            cyanx = 0

    label = tk.Label(root, text="     ", bg="cyan")
    label.grid(row=cyany, column=cyanx)

    lcyanm = nmove
    chasecount()

def revive(ghost):
    global rdead
    global odead
    global cdead
    global pdead
    global rscared
    global cscared
    global pscared
    global oscared
    if ghost == "red":
        if redy == homey and redx == homex:
            rscared = False
            rdead = False
            pass
    elif ghost == "pink":
        if pinky == homey and pinkx == homex:
            pscared = False
            pdead = False
            pass
    elif ghost == "cyan":
        if cyany == homey and cyanx == homex:
            cscared = False
            cdead = False
            pass
    elif ghost == "orange":
        if orangey == homey and orangex == homex:
            oscared = False
            odead = False
            pass

def emove():
    redmove()
    pinkmove()
    cyanmove()
    orangemove()

def best_move(y,x,targety,targetx, ghost):
    moves = []
    if gmap[y-1][x] not in [1,"b","r"]:
        moves.append("up")
    if x == 0 or gmap[y][x-1] not in [1,"b","r"]:
        moves.append("left")
    if gmap[y+1][x] not in [1,"b","r"]:
        moves.append("down")
    if x == len(gmap[0])-1 or gmap[y][x+1] not in [1,"b","r"]:
        moves.append("right")
    if ghost == "red":
        if lredm != None:
            if inversemove[lredm] in moves:
                moves.remove(inversemove[lredm])
    if ghost == "pink":
        if lpinkm != None:
            if inversemove[lpinkm] in moves:
                moves.remove(inversemove[lpinkm])
    if ghost == "cyan":
        if lcyanm != None:
            if inversemove[lcyanm] in moves:
                moves.remove(inversemove[lcyanm])
    if ghost == "orange":
        if lorangem != None:
            if inversemove[lorangem] in moves:
                moves.remove(inversemove[lorangem])
    minimum = 10000
    curbest = None
    for i in moves:
        if i == "up":
            if ((y-1 - targety) ** 2) + ((x-targetx) ** 2) < minimum:
                minimum = ((y-1 - targety) ** 2) + ((x-targetx) ** 2)
                curbest = i
        elif i == "left":
            if ((y - targety) ** 2) + ((x-1-targetx) ** 2) < minimum:
                minimum = ((y - targety) ** 2) + ((x-1-targetx) ** 2)
                curbest = i
        elif i == "down":
            if ((y+1 - targety) ** 2) + ((x-targetx) ** 2) < minimum:
                minimum = ((y+1 - targety) ** 2) + ((x-targetx) ** 2)
                curbest = i
        elif i == "right":
            if ((y - targety) ** 2) + ((x+1-targetx) ** 2) < minimum:
                minimum = ((y - targety) ** 2) + ((x+1-targetx) ** 2)
                curbest = i
    return curbest
def redmove():
    global redy
    global redx
    global lredm
    if rdead:
        revive("red")
    elif rscared:
        goteaten(redy,redx,"red")
    else:
        got_killed(pposy, pposx, redy, redx)
    if gmap[redy][redx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    elif gmap[redy][redx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=redy, column=redx)
    targety = pposy
    targetx = pposx
    if rdead == True:
        nmove = deadmove("red")
    elif rscared == True:
        nmove = scaredmove(redy, redx, "red")
    elif scatter == True:
        nmove = scattermove("red")
    else:
        nmove = best_move(redy, redx, targety, targetx,"red")
    if nmove == "up":
        redy = redy-1
    if nmove == "down":
        redy = redy+1
    if nmove == "left":
        if redx != 0:
            redx = redx-1
        else:
            redx = len(gmap[0])-1
    if nmove == "right":
        if redx != len(gmap[0])-1:
            redx = redx+1
        else:
            redx = 0
    if rdead:
        label = tk.Label(root, text="     ", bg="grey")
    elif rscared == True:
        label = tk.Label(root, text="     ", bg="darkblue")
    else:
        label = tk.Label(root, text="     ", bg="crimson")
    label.grid(row=redy, column=redx)
    if rdead:
        revive("red")
    elif rscared:
        goteaten(redy,redx,"red")
    else:
        got_killed(pposy, pposx, redy, redx)
    lredm = nmove

    pass
def pinkmove():
    global pinky
    global pinkx
    global lpinkm
    if pdead:
        revive("pink")
    elif pscared:
        goteaten(pinky,pinkx,"pink")
    else:
        got_killed(pposy, pposx, pinky, pinkx)
    if gmap[pinky][pinkx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    elif gmap[pinky][pinkx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=pinky, column=pinkx)
    if dire == "up":
        targety = pposy-2
        targetx = pposx
    elif dire == "down":
        targety = pposy+2
        targetx = pposx
    elif dire == "right":
        targety = pposy
        targetx = pposx+2
    else:
        targety = pposy
        targetx = pposx-2
    if pdead:
        nmove = deadmove("pink")
    elif pscared == True:
        nmove = scaredmove(pinky, pinkx, "pink")
    elif scatter == True:
        nmove = scattermove("pink")
    else:
        nmove = best_move(pinky, pinkx, targety, targetx,"pink")
    if nmove == "up":
        pinky = pinky-1
    if nmove == "down":
        pinky = pinky+1
    if nmove == "left":
        if pinkx != 0:
            pinkx = pinkx-1
        else:
            pinkx = len(gmap[0])-1
    if nmove == "right":
        if pinkx != len(gmap[0])-1:
            pinkx = pinkx+1
        else:
            pinkx = 0

    if pdead:
        label = tk.Label(root, text="     ", bg="grey")
    elif pscared == True:
        label = tk.Label(root, text="     ", bg="darkblue")
    else:
        label = tk.Label(root, text="     ", bg="pink")
    label.grid(row=pinky, column=pinkx)
    if pdead:
        revive("pink")
    elif pscared:
        goteaten(pinky,pinkx,"pink")
    else:
        got_killed(pposy, pposx, pinky, pinkx)
    lpinkm = nmove
    pass
def orangemove():
    global orangey
    global orangex
    global lorangem

    if odead:
        revive("orange")
    elif oscared:
        goteaten(orangey,orangex,"orange")
    else:
        got_killed(pposy, pposx, orangey, orangex)
    if gmap[orangey][orangex] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[orangey][orangex] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=orangey, column=orangex)
    if odead:
        nmove = deadmove("orange")
    elif oscared:
        nmove = scaredmove(orangey,orangex,"orange")
    elif scatter == True:
        nmove = scattermove("orange")
    else:
        if ((orangey - pposy)**2)+((orangex - pposx)**2) <= 64:
            nmove = best_move(orangey,orangex,orangefy,orangefx,"orange")
        else:
            nmove = best_move(orangey,orangex,pposy,pposx,"orange")
    if nmove == "up":
        orangey = orangey-1
    if nmove == "down":
        orangey = orangey+1
    if nmove == "left":
        if orangex != 0:
            orangex = orangex-1
        else:
            orangex = len(gmap[0])-1
    if nmove == "right":
        if orangex != len(gmap[0])-1:
            orangex = orangex+1
        else:
            orangex = 0
    if odead:
        label = tk.Label(root, text="     ", bg="grey")
    elif oscared == True:
        label = tk.Label(root, text="     ", bg="darkblue")
    else:
        label = tk.Label(root, text="     ", bg="purple")
    label.grid(row=orangey, column=orangex)
    if odead:
        revive("orange")
    elif oscared:
        goteaten(orangey,orangex,"orange")
    else:
        got_killed(pposy, pposx, orangey, orangex)
    lorangem = nmove
def cyanmove():
    global cyany
    global cyanx
    global lcyanm
    if cdead:
        revive("cyan")
    elif cscared:
        goteaten(cyany,cyanx,"cyan")
    else:
        got_killed(pposy, pposx, cyany, cyanx)

    if gmap[cyany][cyanx] == 0:
        label = tk.Label(root, text="     ", bg="yellow")
    elif gmap[cyany][cyanx] == "p":
        label = tk.Label(root, text="     ", bg="teal")
    else:
        label = tk.Label(root, text="     ", bg="white")
    label.grid(row=cyany, column=cyanx)
    if dire == "up":
        targety = pposy-2-redy
        targetx = pposx-redx
    elif dire == "down":
        targety = pposy+2-redy
        targetx = pposx-redx
    elif dire == "right":
        targety = pposy-redy
        targetx = pposx+2-redx
    else:
        targety = pposy-redy
        targetx = pposx-2-redx
    if cdead == True:
        nmove = deadmove("cyan")
    elif cscared == True:
        nmove = scaredmove(cyany,cyanx,"cyan")
    elif scatter == True:
        nmove = scattermove("cyan")
    else:
        nmove = best_move(cyany,cyanx,targety,targetx,"cyan")
    if nmove == "up":
        cyany = cyany-1
    if nmove == "down":
        cyany = cyany+1
    if nmove == "left":
        if cyanx != 0:
            cyanx = cyanx-1
        else:
            cyanx = len(gmap[0])-1
    if nmove == "right":
        if cyanx != len(gmap[0])-1:
            cyanx = cyanx+1
        else:
            cyanx = 0
    if cdead:
        label = tk.Label(root, text="     ", bg="grey")
    elif cscared == True:
        label = tk.Label(root, text="     ", bg="darkblue")
    else:
        label = tk.Label(root, text="     ", bg="cyan")
    if cdead:
        revive("cyan")
    elif cscared == True:
        goteaten(cyany,cyanx,"cyan")
    else:
        got_killed(pposy, pposx, cyany, cyanx)
    label.grid(row=cyany, column=cyanx)
    lcyanm = nmove

    pass

def deadmove(ghost):
    if ghost == "red":
        y = redy
        x = redx
    elif ghost == "pink":
        y = pinky
        x = pinkx
    elif ghost == "cyan":
        y = cyany
        x = cyanx
    else:
        y = orangey
        x = orangex
    moves = []
    if gmap[y - 1][x] not in [1, "b", "r"]:
        moves.append("up")
    if x == 0 or gmap[y][x - 1] not in [1, "b", "r"]:
        moves.append("left")
    if gmap[y + 1][x] not in [1, "b", "r"]:
        moves.append("down")
    if x == len(gmap[0]) - 1 or gmap[y][x + 1] not in [1, "b", "r"]:
        moves.append("right")
    if ghost == "red":
        if lredm != None:
            if inversemove[lredm] in moves:
                moves.remove(inversemove[lredm])
    if ghost == "pink":
        if lpinkm != None:
            if inversemove[lpinkm] in moves:
                moves.remove(inversemove[lpinkm])
    if ghost == "cyan":
        if lcyanm != None:
            if inversemove[lcyanm] in moves:
                moves.remove(inversemove[lcyanm])
    if ghost == "orange":
        if lorangem != None:
            if inversemove[lorangem] in moves:
                moves.remove(inversemove[lorangem])
    minimum = 10000
    curbest = None
    for i in moves:
        if i == "up":
            if ((y - 1 - homey) ** 2) + ((x - homex) ** 2) < minimum:
                minimum = ((y - 1 - homey) ** 2) + ((x - homex) ** 2)
                curbest = i
        elif i == "left":
            if ((y - homey) ** 2) + ((x - 1 - homex) ** 2) < minimum:
                minimum = ((y - homey) ** 2) + ((x - 1 - homex) ** 2)
                curbest = i
        elif i == "down":
            if ((y + 1 - homey) ** 2) + ((x - homex) ** 2) < minimum:
                minimum = ((y + 1 - homey) ** 2) + ((x - homex) ** 2)
                curbest = i
        elif i == "right":
            if ((y - homey) ** 2) + ((x + 1 - homex) ** 2) < minimum:
                minimum = ((y - homey) ** 2) + ((x + 1 - homex) ** 2)
                curbest = i
    return curbest


dire = "up"
pposy = 23
pposx = 14
def move():
    global score
    global pposy
    global pposx
    if gmap[pposy][pposx] == 0:
        gmap[pposy][pposx] = "w"
        score += 100
    if gmap[pposy][pposx] == "p":
        gmap[pposy][pposx] = "w"
        score += 1000
        chase()

    if dire == "up" and gmap[pposy-1][pposx] not in [1,"b","r"]:
        label = tk.Label(root, text="     ", bg="white")
        label.grid(row = pposy, column = pposx)
        gmap[pposy][pposx] = "w"
        pposy -= 1

    elif dire == "down" and gmap[pposy+1][pposx] not in [1,"b","r"]:
        label = tk.Label(root, text="     ", bg="white")
        label.grid(row=pposy, column=pposx)
        gmap[pposy][pposx] = "w"
        pposy += 1

    elif dire == "left" and gmap[pposy][pposx-1] not in [1,"b","r"]:
        label = tk.Label(root, text="     ", bg="white")
        label.grid(row=pposy, column=pposx)
        gmap[pposy][pposx] = "w"
        if pposx == 0:
            pposx = len(gmap[0])
        pposx -= 1
    elif pposx == len(gmap[0])-1 or dire == "right" and gmap[pposy][pposx+1] not in [1,"b","r"]:
        label = tk.Label(root, text="     ", bg="white")
        label.grid(row=pposy, column=pposx)
        gmap[pposy][pposx] = "w"
        if pposx == len(gmap[0])-1:
            pposx = -1
        pposx += 1

    label = tk.Label(root, text="     ", bg="orange")
    label.grid(row=pposy, column=pposx)
    pass



def func(event):
    global dire
    dire = "up"
def func4(event):
    global dire
    dire = "down"
def func2(event):
    global dire
    dire = "left"
def func3(event):
    global dire
    dire = "right"

def func6():
    for i in gmap:
        for j in i:
            if j == 0 or j == "p":

                return False
    return True


def goteaten(gy,gx,ghost):
    if gy == pposy and gx == pposx:
        kill(ghost)
def kill(ghost):
    global rdead
    global odead
    global cdead
    global pdead
    if ghost == "red":
        rdead = True
    elif ghost == "pink":
        pdead = True
    elif ghost == "cyan":
        cdead = True
    else:
        odead = True


root.bind('<w>', func)

root.bind('<a>', func2)

root.bind('<d>', func3)

root.bind('<s>', func4)

root.bind('<W>', func)

root.bind('<A>', func2)

root.bind('<D>', func3)

root.bind('<S>', func4)



scatterconstant()
constant()
econstant()
root.mainloop()
