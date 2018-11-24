#!/usr/bin/env python3

import game
import random

s = game.Spiel(debug=False, size=20)

s.pos = 90
s.dir = 1
s.length = 5

s.kipos = 210
s.kidir = 1
s.kilength = 5

s.create()

s.level[random.randint(0,399)] = random.randint(-3,-1)

def alleme():
    for ind in range(400):
        if s.level[ind] > 0 and s.level[ind] < 400:
            s.level[ind] = s.level[ind] - 1

def level1():
    s.level[9]=400
    s.level[10]=400

    s.level[390]=400
    s.level[389]=400

    s.level[200]=400
    s.level[180]=400

    s.level[219]=400
    s.level[199]=400

    s.level[189]=400
    s.level[190]=400
    s.level[209]=400
    s.level[210]=400

    s.level[168]=400
    s.level[171]=400
    s.level[228]=400
    s.level[231]=400

level1()

def newpos(pos, dir):
    np = pos + dir
    if np > 400:
        np = np - 400
    if np < 0:
        np = np + 400
    if (np % 20 == 0) and (dir == 1):
        np = np - 20
    if (np % 20 == 19) and (dir == -1):
        np = np + 20
    return np


def newkidir():
    simpos = newpos(s.kipos, s.kidir)
    if s.level[simpos] > 0:
        for dir in [-1, 1, 20, -20]:
            searchpos = newpos(s.kipos, dir)
            if s.level[searchpos] == 0:
                return dir
    return s.kidir


def schritt():
    s.pos = newpos(s.pos, s.dir)
    if s.level[s.pos] > 0:
        print("Spieler tot!")
        print("Punkte: ", s.length)
        print("Punkte KI: ", s.kilength)
        s.exit()
    if s.level[s.pos] < 0:
        print("yummy")
        s.length = s.length + (s.level[s.pos] * -1)
        s.level[random.randint(0,399)] = random.randint(-3,-1)
    s.level[s.pos] = s.length

    s.kidir = newkidir()
    s.kipos = newpos(s.kipos, s.kidir)
    if s.level[s.kipos] > 0:
        print("KI tot!")
        print("Punkte: ", s.length)
        print("Punkte KI: ", s.kilength)
        s.exit()
    if s.level[s.kipos] < 0:
        print("yummy")
        s.kilength = s.kilength + (s.level[s.kipos] * -1)
        s.level[random.randint(0,399)] = random.randint(-3,-1)
    s.level[s.kipos] = s.kilength


def tastendruck(taste):
    if taste == "Up":
        s.dir = -20
    if taste == "Down":
        s.dir = 20
    if taste == "Left":
        s.dir = -1
    if taste == "Right":
        s.dir = 1

s.addStep(alleme)
s.addStep(schritt)
s.addKeylistener(tastendruck)

s.start()
