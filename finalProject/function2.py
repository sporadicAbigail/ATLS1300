# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 21:10:29 2020

@author: Abigail Hutabarat

This is the second function in my series of functions for my final project. It
draws four circles that ease in and out to make diamond sort of shapes. 

Inspiration for this came from Saskia Freeke:
    https://twitter.com/sasj_nl/status/1239304797330845697
    I really like her style of generative art which is geometric shapes that
    move in a sort of mesmerizing way, and I saw the circles in this one and
    thought, 'hey, I can do that' which is why I chose to do this one.
"""

import pygame
from random import *
import time #it's seizure inducing without it

#VARIABLES
# variables needed to work
numClumps = randint(10,20) #a clump is a group of four dots that look together
#the circles moving in and out have a sort of calming feel, so I'm going to have one speed to rule them all
speedConst = 1 #speed is how much the dots move with each run

# variables in the master that are here just to make it work
size = 400 #window size
window = pygame.display.set_mode((size,size))
paleGreen = (214,246,221)
palePurp = (218,196,247)
paleRed = (244,152,156)
paleYellow = (235,210,180)
paleBlue = (172, 236, 247)
colorList = [paleGreen, palePurp, paleRed, paleYellow, paleBlue]

#FUNCTIONS
def makeObjects(size, speedConstant, surface):
    '''This function makes a master object list that gets returned. One object
    is a group of four dots.'''
    function2Objects = []
    for i in range(numClumps):
        function2Objects.append(explodingDots(size, speedConst, window)) 
    return function2Objects
                               
def draw(numberOfClumps, objectList):
    '''Draws the circles'''
    time.sleep(.05) #slows down Python so the circle movement is visible and its not a series of flashes
    for i in range(numberOfClumps):
        objectList[i].drawDots()

#CLASSES                                
class explodingDots():
    def __init__(self, canvasSize, speed, surface):
        '''Initializing the object and giving it attributes.'''
        self.maxDistance = randint(20,50)
        self.radius = 5 #arbitrarily chosen constant
        #the following four variables are calculations so that the dots will not go off screen
        xMin = 0+self.maxDistance+self.radius
        yMin = 0+self.maxDistance+self.radius
        xMax = canvasSize-self.maxDistance-self.radius
        yMax = canvasSize-self.maxDistance-self.radius
        #home position is the center of the four dots radiating outward
        self.homePosition = (randint(xMin,xMax),randint(yMin,yMax))
        #The following four variables are so that they all originate at the
        #defined home position. But I need four variables to put 
        homePositionOne = [self.homePosition[0],self.homePosition[1]]
        homePositionTwo = [self.homePosition[0],self.homePosition[1]]
        homePositionThree = [self.homePosition[0],self.homePosition[1]]
        homePositionFour = [self.homePosition[0],self.homePosition[1]]
        #Order of dots: unit circle: right, up, left, down
        #Position dots has a list of tuples, each tuple is a position that can be independently changed
        self.positionDots = [homePositionOne, homePositionTwo, homePositionThree, homePositionFour]
        #list of speeds so they start moving in the correct direction. 
        #(Not all will move in the same direction at the same time)
        self.speedDots = [speed, -speed, -speed, speed]
        self.surface = surface
        self.color = choice(colorList)
        
    def drawDots(self):
        '''This draws the dots and also does the changes in position so it animates.'''
        for i in range(4): #range of four dots that comprise the up, down, left, right
            pygame.draw.circle(self.surface,self.color,self.positionDots[i],self.radius)
            if i%2 == 0:
                '''If it is an even number, 0 or 2, the x direction is the one
                that moves.'''
                self.positionDots[i][0] += self.speedDots[i]
            else:
                '''If it isn't an even number, it must be an odd number, 1 or 3,
                and the y direction is the one that moves.'''
                self.positionDots[i][1] += self.speedDots[i]

        if self.positionDots[0][0] >= (self.homePosition[0] + self.maxDistance) or self.positionDots[0][0] <= self.homePosition[0]:
            '''This checks if the right moving dot x position is greater 
            than the max distance it should travel or less than the origin 
            position, it will cause all of the speeds to flip direction.
            This is because they all move the same distance, so when one
            changes direction, all of them will.'''
            for i in range(4):
                self.speedDots[i] *= -1
            
#LETS MAKE OBJECTS
objectList = makeObjects(size, speedConst, window)
        
#also, game loop copied from Dr. Z's OOP API from https://repl.it/@sazamore/OOP-API 
#GAME LOOP

run = True

while run:
    window.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
    draw(numClumps, objectList)
    #update screen
    pygame.display.update()
    
pygame.quit()
