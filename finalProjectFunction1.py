# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 23:09:51 2020

@author: Abigail Hutabarat

This is the first of my generative art modules that will be combined in a larger
generative art gallery project. The screen is divided into a random number of
sections, with each side having anywhere from 3-6 squares,
and a point is randomly chosen. From there, that point will be randomly chosen
to go move in the x or the y direction. And since I'm using polygons, it will
connect the points so we'll have fun triangle shapes.

Inspiration for this piece of generative art is from Saskia Freeke: 
    https://twitter.com/sasj_nl/status/1240000082319224834
    I really like her style of generative art, which is geometric shapes that
    move in mesmerizing ways. I saw this work and thought 'hey, I can do that'
    which is why I chose to do this one. As an added element of uniqueness I
    randomized the number of squares that are on each side.
"""
import pygame
from random import *
import time

#VARIABLES
#These next variables are things that should be from the master
canvasSize = 400
screen1 = pygame.display.set_mode((canvasSize,canvasSize))
paleGreen = (214,246,221)
palePurp = (218,196,247)
paleRed = (244,152,156)
paleYellow = (235,210,180)
paleBlue = (172, 236, 247)
colorList = [paleGreen, palePurp, paleRed, paleYellow, paleBlue]

#variables needed for the function to run
numBoxesOnSide = randint(3,6) #adds some more randomness
sideLength = canvasSize/numBoxesOnSide 
strokeWidth = 6 #width of the shapes being drawn
 

#FUNCTIONS
def makeObjects(numberBoxes, listOfColors):
    '''This creates objects from the class boxSidesThatMove and returns the
    object list that was created. Each object is one box, and the numberBoxes
    parameters determines how many boxes down and up we should make.'''
    objectList = []
    for i in range(numberBoxes): #counts to the right
        for j in range(numberBoxes): #counts down
                objectList.append(boxSidesThatMove(i, j, listOfColors))
    return objectList

def draw(screen, objectList):
    '''Drawing function. It takes the objectList and for the number of objects
    given, it draws a polygon using the class method.'''
    #it needs to keep filling it so it doesn't just blend into a mess
    screen.fill((0,0,0))
    time.sleep(.05)
    for i in range(len(objectList)):
        objectList[i].drawPolygons()

# CLASS
class boxSidesThatMove:
    def __init__(self, countRight, countDown, listOfColors):
        '''Initializing function for an object. Each object is one box.'''
        #listOfColors and speed gets a little convoluted since its kind of
        #following a train out, but this is to make sure that every method
        #and function doesn't rely on a global variable
        self.color = choice(listOfColors) #randomly chosen color from a list
        #top left point
        self.homePosition = (sideLength*countRight, sideLength*countDown) 
        #top right point
        self.positionTopRight = [self.homePosition[0]+sideLength, self.homePosition[1]]
        #bottom right point
        self.positionBottomRight = [self.homePosition[0]+sideLength, self.homePosition[1]+sideLength]
        #bottom left point
        self.positionBottomLeft = [self.homePosition[0], self.homePosition[1]+sideLength]
        ##how much the points move with each run of the code (looks like speed)
        self.speed = randint(1,8)
        #this determines which point moves.
        self.movingPoint = randint(0,3)
        #this determines which direction that point will move
        self.directionChoice = randint(0,1)
    def drawPolygons(self):
        '''Draw a polygon with a single point that moves'''
        #this is what draws the thing
        pygame.draw.polygon(screen1, self.color, (self.homePosition, self.positionTopRight, self.positionBottomRight, self.positionBottomLeft),strokeWidth)
        #It's super repetitive, but since each thing is just *slightly*
        #different from each other, it needs to be individualized
        if self.movingPoint == 0:
            #move the top right
            if self.directionChoice == 0:
                #move x direction
                self.positionTopRight[0] -= self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionTopRight[0] <= self.homePosition[0]:
                    self.speed *= -1
                elif self.positionTopRight[0] >= self.homePosition[0]+sideLength:
                    self.speed *= -1
            else:
                #move y direction
                self.positionTopRight[1] += self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionTopRight[1] >= self.positionBottomRight[1]:
                    self.speed *= -1
                elif self.positionTopRight[1] <= self.homePosition[1]:
                    self.speed *= -1
        elif self.movingPoint == 1:
            #move the bottom right
            if self.directionChoice == 0:
                #move x direction
                self.positionBottomRight[0] -= self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionBottomRight[0] <= self.positionBottomLeft[0]:
                    self.speed *= -1
                elif self.positionBottomRight[0] >= self.positionTopRight[0]:
                    self.speed *=-1
            else:
                #move y direction
                self.positionBottomRight[1] -= self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionBottomRight[1] <= self.positionTopRight[1]:
                    self.speed *= -1
                elif self.positionBottomRight[1] >= self.positionBottomLeft[1]:
                    self.speed *= -1
        else:
            #move the bottom left
            if self.directionChoice == 0:
                #move x direction
                self.positionBottomLeft[0] += self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionBottomLeft[0] >= self.positionBottomRight[0]:
                    self.speed *= -1
                elif self.positionBottomLeft[0] <= self.homePosition[0]:
                    self.speed *= -1
            else:
                #move y direction
                self.positionBottomLeft[1] -= self.speed
                #this if statement checks to see if it has reached its maximum
                #or minimum position, if it has, it switches direction of speed
                if self.positionBottomLeft[1] <= self.positionTopRight[1]:
                    self.speed *= -1
                elif self.positionBottomLeft[1] >= self.positionBottomRight[1]:
                    self.speed *= -1
                            
# OBJECTS
objectList = makeObjects(numBoxesOnSide, colorList)
    
#also, game loop copied from Dr. Z's OOP API from https://repl.it/@sazamore/OOP-API 
#GAME LOOP

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    draw(screen1, objectList)
    #update screen
    pygame.display.update()
    
pygame.quit()
