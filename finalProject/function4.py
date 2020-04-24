# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:25:35 2020

@author: Abigail Hutabarat

astroids: revenge of the objects
This is my fourth function for my final project. It features two stars that
circle around each other. I first worked with these stars for an assignment from
a month ago, and it was before I learned anything about objects, so I wanted
to revisit it, this time, using classes and objects to draw them, and instead
of having them get larger and smaller, this one has them circling each other
"""
#IMPORT LIBRARIES
import pygame
from random import *
import math

#VARIABLES
paleGreen = (214,246,221)
palePurp = (218,196,247)
paleRed = (244,152,156)
paleYellow = (235,210,180)
paleBlue = (172, 236, 247)
colorList = [paleGreen, palePurp, paleRed, paleYellow, paleBlue]

size = 400
window4 = pygame.display.set_mode((size,size))

pi = math.pi
# The number of pairs that will show up, meaning there will be numClumps *2 stars
numClumps = randint(4,8) 
#FUNCTIONS
def makeObjects(surface, listOfColors, canvasSize, numberOfClumps):
    '''This function makes a list of objects, and returns that list. Each object
    is a pair of stars circling each other.'''
    objectList = []
    for i in range(numberOfClumps):
        objectList.append(wackyStars(surface,listOfColors,canvasSize))
    return objectList

def draw(surface, listOfObjects):
    '''This runs the drawing function for the clumps of stars revolving around
    each other'''
    surface.fill((0,0,0)) #refills the surface so it doesn't smear into a blob
    for i in range(len(listOfObjects)):
        objectList[i].drawArcs()

#CLASSES
class wackyStars():
    def __init__(self, surface, listOfColors, canvasSize):
        '''One object is going to be one clump (a pair of stars).'''
        self.surface = surface
        self.color = choice(listOfColors)
        self.radius = randint(20,40) #radius of the circle the two things spiral each other with
        self.sideLength = randint(20,40) #used in rectangles
        #The following is a calculation for where the clumps can be so they don't get cut off the screen
        minDist = int(self.radius + self.sideLength/2)
        maxDist = int(canvasSize - self.radius - self.sideLength/2)
        #Center is the point where the two planets revolve around
        self.center = (randint(minDist,maxDist),randint(minDist,maxDist))
        #theta to put into the parametric equations for location around the circle
        self.planet1Theta = 0
        self.planet2Theta = pi
        #parametric functions for the x and y coordinates of the centers
        self.planet1 = [self.radius*math.cos(self.planet1Theta)+self.center[0],self.radius*math.sin(self.planet1Theta)+self.center[1]]
        self.planet2 = [self.radius*math.cos(self.planet2Theta)+self.center[0],self.radius*math.sin(self.planet2Theta)+self.center[1]]
        #choice of going clockwise or counterclockwise around the circle, adds variation
        speedList = [-.001,.001]
        self.speed = choice(speedList)
        
    def drawRects(self):
        '''This function draws 8 rectangles, one for each arc. The rectangles
        are based on the center positions. Theta increases so that the next 
        position is a little more and it goes around in a circle. Returns a 
        rectangle list containing all 8 rectangles.'''
        #planet 1
        #quad as in quadrant corresponding to cartesian plane
        rect1Quad1 = pygame.Rect(self.planet1[0],self.planet1[1]-self.sideLength,self.sideLength,self.sideLength)
        rect1Quad2 = pygame.Rect(self.planet1[0]-self.sideLength,self.planet1[1]-self.sideLength, self.sideLength,self.sideLength)
        rect1Quad3 = pygame.Rect(self.planet1[0]-self.sideLength,self.planet1[1],self.sideLength,self.sideLength)
        rect1Quad4 = pygame.Rect(self.planet1[0],self.planet1[1],self.sideLength,self.sideLength)
        #setting up the next position
        self.planet1 = [self.radius*math.cos(self.planet1Theta)+self.center[0],self.radius*math.sin(self.planet1Theta)+self.center[1]]
        #increasing theta
        self.planet1Theta += self.speed
        #planet 2
        rect2Quad1 = pygame.Rect(self.planet2[0],self.planet2[1]-self.sideLength,self.sideLength,self.sideLength)
        rect2Quad2 = pygame.Rect(self.planet2[0]-self.sideLength,self.planet2[1]-self.sideLength, self.sideLength,self.sideLength)
        rect2Quad3 = pygame.Rect(self.planet2[0]-self.sideLength,self.planet2[1],self.sideLength,self.sideLength)
        rect2Quad4 = pygame.Rect(self.planet2[0],self.planet2[1],self.sideLength,self.sideLength)
        
        self.planet2 = [self.radius*math.cos(self.planet2Theta)+self.center[0],self.radius*math.sin(self.planet2Theta)+self.center[1]]
        self.planet2Theta += self.speed
        
        self.rectangleList = [rect1Quad1, rect1Quad2, rect1Quad3, rect1Quad4, rect2Quad1, rect2Quad2, rect2Quad3, rect2Quad4]
        
    def drawArcs(self):
        '''This runs the drawRects function and draws the arcs.'''
        wackyStars.drawRects(self)
        #list of the start and stop angles for each arc. 8 tuples for 8 rectangles/arcs
        angleList = [(pi,3*pi/2),(3*pi/2,2*pi),(0,pi/2),(pi/2,pi),(pi,3*pi/2),(3*pi/2,2*pi),(0,pi/2),(pi/2,pi)]
        for i in range(len(self.rectangleList)):
            pygame.draw.arc(self.surface,self.color,self.rectangleList[i],angleList[i][0],angleList[i][1])
            
#OBJECTS
objectList = makeObjects(window4,colorList,size, numClumps)

#GAME LOOP
#game loop copied from Dr. Z's OOP API from https://repl.it/@sazamore/OOP-API 

run = True #variable to make the loop run
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    draw(window4,objectList)
    #update screen
    pygame.display.update()
    
pygame.quit()
