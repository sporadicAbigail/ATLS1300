# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 20:37:19 2020

@author: Abigail Hutabarat

This is the third of my generative art modules that will be combined in a larger
generative art gallery project. There are a number of "clumps" which each have
a set number of circles part of the clump. Each circle is a randomized distance
apart from each other, and has a randomized maximum size. The circles then grow
and shrink in sucessession with each other to make what I like to call worms.

Inspiration for this piece of generative art is from Saskia Freeke: 
    https://twitter.com/sasj_nl/status/1234960586687098882
"""
#BUGS: None! Like my first function, this worked almost immediately with little error
import pygame
from random import *
import time #it's seizure inducing without it

#VARIABLES
paleGreen = (214,246,221)
palePurp = (218,196,247)
paleRed = (244,152,156)
paleYellow = (235,210,180)
paleBlue = (172, 236, 247)
colorList = [paleGreen, palePurp, paleRed, paleYellow, paleBlue]

size = 400
window3 = pygame.display.set_mode((size,size))

# these are the only variables needed that aren't set from the master
numCircles = 5
numClumps = 18

#FUNCTIONS

def makeObjects(canvasSize, surface, numberOfCircles):
    '''This function makes a list of the objects. Each object is a clump, which
    is why the for loop iterates numClumps times. Returns that list.'''
    funkyCircleList = []
    for i in range(numClumps):
        funkyCircleList.append(funkyCircles(canvasSize, surface, numberOfCircles))
    return funkyCircleList

def draw(surface, listOfObjects):
    '''This function calls the drawing function from the class funkyCircles.'''
    time.sleep(.05) #slows down Python so the circle movement is visible and its not a series of flashes
    surface.fill((0,0,0))
    for i in range(numClumps):
        listOfObjects[i].drawCircles()

#CLASSES
class funkyCircles():
    def __init__(self, canvasSize, surface, numCircles):
        '''Initializing the attributes for the object. 1 object is 1 clump.'''
        self.numCircles = numCircles #this numCircles is used later
        self.scootch = randint(3,15) #scootch is the distance apart from each other
        self.width = 2 #stroke width
        self.speed = 1 #the amount the radius increases or decreases
        self.maxRadius = randint(15,50) #maximum radius that the circles can have
        self.color = choice(colorList) #random colors~
        self.surface = surface #surface needed for pygame
        self.radiusList = [] #list of radii for each circle so they have different radii
        self.speedList = [] #list of speeds so that each circle moves independently
            #it creates that nice wave look
        for i in range(numCircles):
            #the initial radii are created smaller than the one to the left
            self.radiusList.append((self.maxRadius - i*2*self.speed))
            self.speedList.append(self.speed)
        #the following variables are so that the center of the starting circle
            #doesn't 
        maxX = canvasSize - self.maxRadius -(self.scootch*numCircles)
        maxY = canvasSize - self.maxRadius
        #this center is actually the center of the left most circle
        #starts at self.radius so it doesn't cut off top or left part
        self.center = (randint(self.maxRadius,maxX),randint(self.maxRadius,maxY)) 

    def drawCircles(self):
        '''Let's draw some circles!'''            
        #since one object is a clump, the drawing function needs to draw the 
        #number of circles wanted, defined by numCircles (a parameter)
        for i in range(self.numCircles): 
            #each x position of the circle is scootch amount apart from each other
            xPos = int(self.center[0] + i*self.scootch)
            #the actual drawing part
            pygame.draw.circle(self.surface, self.color, (xPos, int(self.center[1])), self.radiusList[i], self.width)
            #the radii are stored in radiusList, so for each i (circle)
            #it needs to decrease or increase by the speed set in the speed list
            self.radiusList[i] -= self.speedList[i]
            #this statement checks to make sure that when the circle reaches its
            #max or minimum size, it needs to change directions
            if self.radiusList[i] <= self.width+(2*self.speedList[i]):
                self.speedList[i] *= -1
            elif self.radiusList[i] >= self.maxRadius:
                self.speedList[i] *= -1
                
        
#OBJECTS
objectList = makeObjects(size,window3,numCircles)

#also, game loop copied from Dr. Z's OOP API from https://repl.it/@sazamore/OOP-API 
#GAME LOOP
run = True #variable to make the loop run

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    draw(window3, objectList)
    #update screen
    pygame.display.update()
    
pygame.quit()
