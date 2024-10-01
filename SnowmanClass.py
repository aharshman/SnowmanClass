# -*- coding: utf-8 -*-
"""
Alexander Harshman
12/16/21
CS 135 Final
Description:  This class draws a snowman tha the user can make shorter and taller.
If the snowman gets to tall the window will display a meesage.  The same things goes
for if it is to small.
"""

from graphics import *
from button import Button

class Snowman:
    
    """The __init__ function sets all of our variables that we will need later"""
    def __init__(self):
        
        win = GraphWin('Frosty', 500, 500)
        win.setCoords(0, 0, 100, 100)
        win.setBackground('lightblue')
        
        self.win = win
        self.mes = Text(Point(50, 90), ' ').draw(win)
        self.c = 3
            
        self.__createbuttons()
        self.__createcircles()
        self.__createface()
        
    
    """The __createbuttons function makes all three buttons. It is a privite class"""
    def __createbuttons(self):
        
        bspecs = [(25,30,15,10,'Melt'), (25,15,15,10,'Freeze'), (75,22.5,15,10,'Quit',)]
                  
        self.buttons = []
        
        for (cx, cy, w, h, label) in bspecs:
            
            self.buttons.append(Button(self.win, Point(cx, cy), w, h, label, 'lightgray'))
            
        for b in self.buttons:
            
            b.activate()
            
    """The __createcircles function makes all four possible circles
        and keeps them in a list. It is a privite class"""
    def __createcircles(self):
        
        Cspecs = [(50, 10,), (50, 30,), (50, 50,), (50, 70,)]
                  
        self.circles = []
        
        for (cx, cy) in Cspecs:
            
            self.circles.append(Circle(Point(cx, cy), 10))
            
        for i in range(4):
            self.circles[i].setFill('white')
        
        for i in range(3):
            self.circles[i].draw(self.win)
            
    """The __createface function makes the face of the snowman and puts
        all of it's attributes in an easy to access list.  It is a privite class"""
    def __createface(self):
        
        self.face = []
        
        eye1 = Circle(Point(46, 55), 1.5)
        eye1.setFill('black')
        self.face.append(eye1)
        eye2 = Circle(Point(54, 55), 1.5)
        eye2.setFill('black')
        self.face.append(eye2)
        
        m1 = Circle(Point(43,48), 1)
        m1.setFill('black')
        self.face.append(m1)
        m2 = m1.clone()
        m2.move(3, -2)
        self.face.append(m2)
        m3 = m2.clone()
        m3.move(4, -1)
        self.face.append(m3)
        m4 = m3.clone()
        m4.move(4, 1)
        self.face.append(m4)
        m5 = m4.clone()
        m5.move(3, 2)
        self.face.append(m5)
        
        nose = Polygon(Point(51, 52), Point(54, 48), Point(50, 49))
        nose.setFill('orange')
        self.face.append(nose)
    
        for item in self.face:
            item.draw(self.win)
    
    """The getbutton function returns the label of the button clicked.  It finds out which
        button was pressed"""
    def getbutton(self):
        
        while True:
            
            p = self.win.getMouse()
            
            for b in self.buttons:
                
               if b.clicked(p):
                
                    return b.getlabel()
    
    """The process buttons function knows what to do based on which button is pressed"""
    def processButton(self, key):
        
        if key == 'Quit':
            self.win.close()
            
        elif key == 'Melt':
            
            self.c -= 1
            if self.c <= 0:
                self.mes.setText('Is It Spring yet?')
                self.c += 1
            else:
                for item in self.face:
                    item.move(0, -20)
                self.circles[self.c].undraw()
                self.mes.setText(' ')
            
        elif key == 'Freeze':
            
            
            if self.c >= 4:
                self.mes.setText('Happy Holidays!')
                
            else:
                self.circles[self.c].draw(self.win)
                for item in self.face:
                    item.move(0, 20)
                    item.undraw()
                    item.draw(self.win)
                self.c += 1
                self.mes.setText(' ')
            
    """The run function starts a forever loop of all of the functions
        making the program run."""
    def run(self):
        
        while True:
            
            key = self.getbutton()
            self.processButton(key)
        
"""The main function activates our run function."""
def main():
    
    s = Snowman()
    s.run()
    
    
main()
    