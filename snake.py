import game
import random

s = game.Spiel(debug=False, size=20)

s.create()

s.level[random.randint(0,399)] = random.randint(-3,-1)
s.level[random.randint(0,399)] = random.randint(-3,-1)
s.level[random.randint(0,399)] = random.randint(-3,-1)

koordinate = [10,1]

class Spieler():
    def __init__(self, name, pos, dir, length, alive):
        self.name = name
        self.position = pos
        self.direction = dir
        self.length = length
        self.alive = alive
        
dieSpieler = [Spieler(name="peter", pos=[ 5,5], dir=[0,1], length=10, alive=True),
              Spieler(name="paul",  pos=[15,5], dir=[0,1], length=10, alive=True),
              ]

def coord2index(coord):
    result = coord[0] + coord[1] * 20
    return result

def neueposition(pos, dir):
    pos[0] = (pos[0] + dir[0]) % 20
    pos[1] = (pos[1] + dir[1]) % 20
    return pos
    

def alleme(l):
    for ind in range(len(l)):
        if l[ind] > 0:
            l[ind] = l[ind] - 1
    return l

def schritt():
    global dieSpieler
    s.level = alleme(s.level)
    for sp in dieSpieler:
        if sp.alive:
            np = neueposition(sp.position, sp.direction)
            index = coord2index(np)
            if s.level[index] > 0:
                print("Crashed game over for: ", sp.name)
                print("Punkte: ", sp.length)
                sp.alive = False
                break
            if s.level[index] < 0:
                print("yummy")
                sp.length = sp.length + (s.level[index] * -1)
                s.level[random.randint(0,399)] = random.randint(-3,-1)
            s.level[index] = sp.length
    
    if not(dieSpieler[0].alive or dieSpieler[1].alive):
        print("Beide Spieler sind tot!")
        s.exit()

def tastendruck(taste):
    global dieSpieler
    if taste == "Up":
        dieSpieler[0].direction = [ 0,-1]
    if taste == "Down":
        dieSpieler[0].direction = [ 0, 1]
    if taste == "Left":
        dieSpieler[0].direction = [-1, 0]
    if taste == "Right":
        dieSpieler[0].direction = [ 1, 0]
    if taste == "w":
        dieSpieler[1].direction = [ 0,-1]
    if taste == "s":
        dieSpieler[1].direction = [ 0, 1]
    if taste == "a":
        dieSpieler[1].direction = [-1, 0]
    if taste == "d":
        dieSpieler[1].direction = [ 1, 0]

s.addStep(schritt)
s.addKeylistener(tastendruck)

s.start()

