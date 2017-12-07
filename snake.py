import game
import random

s = game.Spiel(debug=False, size=20)

s.create()

s.level[random.randint(0,399)] = random.randint(-3,-1)
s.level[random.randint(0,399)] = random.randint(-3,-1)
s.level[random.randint(0,399)] = random.randint(-3,-1)

koordinate = [10,1]

position = [10,10]
richtung = [0,1]
länge = 10

def coord2index(coord):
    result = coord[0] + coord[1] * 20
    return result

print("umrechnung: ", coord2index(coord = koordinate))

def neueposition():
    position[0] = position[0] + richtung[0]
    position[1] = position[1] + richtung[1]
    if position[0] == 20:
        position[0] = 0
    if position[1] == 20:
        position[1] = 0
    if position[0] == -1:
        position[0] = 19
    if position[1] == -1:
        position[1] = 19

print("alte position: ", position)
neueposition()
print("neue pos: ", position)
    

def alleme(l):
    for ind in range(len(l)):
        if l[ind] > 0:
            l[ind] = l[ind] - 1
    return l

def schritt():
    global länge
    s.level = alleme(s.level)
    neueposition()
    index = coord2index(position)
    if s.level[index] > 0:
        print("game over")
        print("Punkte: ", länge)
        s.exit()
    if s.level[index] < 0:
        print("yummy")
        länge = länge + (s.level[index] * -1)
        s.level[random.randint(0,399)] = random.randint(-3,-1)
    s.level[index] = länge

def tastendruck(taste):
    global richtung
    if taste == "Up":
        richtung = [0,-1]
    if taste == "Down":
        richtung = [0,1]
    if taste == "Left":
        richtung = [-1,0]
    if taste == "Right":
        richtung = [1,0]

s.addStep(schritt)
s.addKeylistener(tastendruck)

s.start()

