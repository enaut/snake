from tkinter import *
from time import sleep


class Spiel():
    """
    Diese Klasse macht das programmieren eines Pixelspiels mit
    Python einfach.
    
    Der Entstanden ist diese Datei für den Unterricht der
    Waldorfschule Uhlandshöhe.
    Der Quelltext wird unter den Bedingungen der GPL V3 oder höher
    publiziert.
    """
    border = 0
    blocks =[]
    texts = []
    steps = []
    keylisteners = []
    debug = True

    def __init__(self, size=20, pixelsize=20, debug=True, speed=200):
        """
        Das Spiel ist die Grund-Klasse mit ihr öffnet sich das
        Fenster und die Spielwelt wird initialisiert.

        Parameter (optional):
            * size: die Größe des Spielfeldes
            * pixelsize: die Größe der einzelnen Pixel
            * debug: Anzeigen von Zahlen für jeden Pixel
            * speed: Die Geschwindigkeit des Spiels.
        """
        self.size = size
        self.pixelsize = pixelsize
        self.speed = speed
        self.debug = debug
        self.game = Tk()
        self.level = [0]*size*size
        self.levelindex = list(range(size*size))
        self.steps = []
        self.keylisteners = []
        self.canvas = Canvas(self.game,
                             width = size*pixelsize,
                             height = size*pixelsize)
        self.canvas.pack()

    def addStep(self, function):
        """ Hinzufügen einer Funktion die jeden Spielschritt
            ausgeführt wird. """
        self.steps.append(function)

    def addKeylistener(self, function):
        """Hinzufügen einer Funktion die bei einem Tastendruck
        ausgeführt wird."""
        self.keylisteners.append(function)


    def createlevel(self):
        """ Initialisieren des Levels. Und der zugehörigen
            Pixelflächen.
        """
        for i in self.levelindex:
            x,y = self.number2coord(i)
            block = self.canvas.create_rectangle(x,
                                       y,
                                       x+self.pixelsize-self.border,
                                       y+self.pixelsize-self.border,
                                       fill="white")
            self.blocks.append(block)
        if self.debug:
            for i in self.levelindex:
                x,y = self.number2coord(i)
                tex = self.canvas.create_text(x+self.pixelsize/2 - 3,
                                           y+self.pixelsize/2,
                                           fill="white",
                                           text=str(self.level[i]),
                                           font=("Courier 11 bold"))
                self.texts.append(tex)

    def create(self):
        """
        Erstellen und zeichnen des Spieles.
        """
        self.createlevel()
        self.registerkeys()


    def start(self):
        """
        starten des Spiels
        """
        self.game.after(10, self.animate)
        self.game.mainloop()

    def react(self, event):
        #print("Reagiere auf Tastendruck: ", event.keysym)
        "Auf einen Tastendruck reagieren."
        for f in self.keylisteners:
            f(event.keysym)

    def registerkeys(self):
        """ Alle verwendeten Tasten registrieren. """
        self.game.bind('<Escape>', self.react)
        self.game.bind('<Up>', self.react)
        self.game.bind('<Down>', self.react)
        self.game.bind('<Left>', self.react)
        self.game.bind('<Right>', self.react)
        self.game.bind('a', self.react)
        self.game.bind('w', self.react)
        self.game.bind('s', self.react)
        self.game.bind('d', self.react)

    def draw(self):
        """ Das Spielfeld zeichnen. """
        for i in self.levelindex:
            if self.level[i] > 0:
                self.canvas.itemconfig(self.blocks[i],
                                       fill = 'Blue',
                                       width=0)
            elif self.level[i] == -1:
                self.canvas.itemconfig(self.blocks[i],
                                       fill = 'red',
                                       width=0)
            elif self.level[i] == -2:
                self.canvas.itemconfig(self.blocks[i],
                                       fill = 'purple',
                                       width=0)
            elif self.level[i] <= -3:
                self.canvas.itemconfig(self.blocks[i],
                                       fill = 'green',
                                       width=0)
            else:
                self.canvas.itemconfig(self.blocks[i],
                                       fill = 'white',
                                       width=0)

        if self.debug:
            for i in self.levelindex:
                self.canvas.itemconfig(self.texts[i], text=str(self.level[i])if self.level[i] else "")

    def animate(self):
        """ Einen Animationsschritt durchführen. """
        self.game.update()
        for f in self.steps:
            f()
        try:
            self.draw()
        except:
            pass
        self.game.after(self.speed, self.animate)

    def number2coord(self, num):
        """ Umrechnen einer Zahl in eine x,y Koordinate. """
        x = (num%self.size) * self.pixelsize
        y = int(num/self.size) * self.pixelsize
        return x,y

    def coord2number(self,x,y):
        """ Koordinate in eine Eindimmensionale Zahl umrechnen. """
        if x>self.size-1 or y>self.size-1:
            raise Exception("Not a coordiante numbers too big!")
        else:
            return self.size*y + x

    def exit(self):
        """Beenden des Spiels."""
        print("beende das Spiel.")
        self.game.destroy()

