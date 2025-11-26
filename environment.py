# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 00:11:47 2020

@author: Adam
"""

import pygame
import numpy as np
import time
import classes
import functions
import create_q_matrix as cqm
import select_action as sa
import update_q_matrix as uqm

pygame.init()
pygameCheck = pygame.get_init()

gameRunning = False

winW = 800
winH = 600
gameDisplay = pygame.display.set_mode((winW, winH))
clock = pygame.time.Clock()
startTimer = time.time()
timeList = []
fps = 60
score = 0
gameNum = 0
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255)
itemColour = pygame.Color(100, 100, 100)
itemNearby = False
cDimensions = 20
character = classes.Player(red, cDimensions, cDimensions)
charGroup = pygame.sprite.GroupSingle()
charGroup.add(character)
oldPos = np.array([0, 0])
reward = 0
nReward = 1
itemGroup = pygame.sprite.Group()
numItems = 20
scanGroup = pygame.sprite.GroupSingle()
epsilon = 1 #PROBABILITY OF RANDOM ACTION BEING CHOSEN

functions.drawItems(numItems, itemGroup, itemColour, 0)

#These two variables are the width and height of the area that
#the sprite is allowed to move in
gameW = winW - cDimensions
gameH = winH - cDimensions
#These two variables are the width and height of the area that
#is relevent to the Q-matrix
#This is creating a grid with a cell size of 5x5
QW = 160
QH = 120
qArray = np.array([QW, QH])

Q = cqm.RL_create_qmatrix(qArray, 4)

if pygameCheck == True:
    gameRunning = True
else:
    print("An initialisation error with Pygame has occured!")

while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gameRunning = False
    
    gameDisplay.fill(blue)
    charGroup.draw(gameDisplay)
    itemGroup.draw(gameDisplay)
    scanGroup.draw(gameDisplay)
    
    #Accounting for movement beyond the bounds of the game
    if charGroup.sprite.rect.x < cDimensions:
        charGroup.sprite.rect.x = gameW
    elif charGroup.sprite.rect.x > gameW:
        charGroup.sprite.rect.x = cDimensions
    elif charGroup.sprite.rect.y < cDimensions:
        charGroup.sprite.rect.y = gameH
    elif charGroup.sprite.rect.y > gameH:
        charGroup.sprite.rect.y = cDimensions
    
    #Agent movement
    playerPos = charGroup.sprite.get_pos()
    #Accounting for Q-matrix dimension squish
    playerPosQW = int(round(playerPos[0] / 5))
    playerPosQH = int(round(playerPos[1] / 5))
    playerPosQ = np.array([playerPosQW, playerPosQH])
    action = sa.RL_select_action(Q, playerPosQ, epsilon)
    
    if action == 0:
        charGroup.sprite.rect.y -= cDimensions
        reward = nReward
    elif action == 1:
        charGroup.sprite.rect.x -= cDimensions
        reward = nReward
    elif action == 2:
        charGroup.sprite.rect.y += cDimensions
        reward = nReward
    elif action == 3:
        charGroup.sprite.rect.x += cDimensions
        reward = nReward
    
    #Collection and scanning
    collision = pygame.sprite.groupcollide(charGroup, itemGroup, False, True, collided = None)
    itemNearby = False
    agentX = playerPos[0]
    agentY = playerPos[1]
    scanWidth = 100
    scanHeight = 100
    scanX = agentX - 50
    scanY = agentY - 50
    scanSprite = classes.Item(pygame.Color(100, 100, 100), scanX, 
                              scanY, scanWidth, scanHeight)
    scanGroup.add(scanSprite)
    scanCollision = pygame.sprite.groupcollide(scanGroup, itemGroup, True, False, collided = None)
    #Item nearby
    if scanCollision != {}:
        itemNearby = True
        reward = 5
        #print("There is an item nearby!")
    #No item nearby
    else:
        #reward = 10
        scanGroup.empty()
        #print("There isn't another item nearby")
    
    #Item collision
    if collision != {}:
        #Item collected and another item nearby
        if itemNearby:
            reward = 30
        #Item collected and no other items nearby
        else:
            reward = 20
        
        score += 1
        print("Score: " + str(score))
        
        cTimer = time.time() - startTimer
        print("Time: " + str(format(cTimer, ".3f")))
    
    #print(reward)
    Q = uqm.RL_update_QMatrix(Q, oldPos, playerPosQ, reward, action)
    
    oldPos = playerPosQ
    
    pygame.display.update()
    clock.tick(fps)
    
    if score == numItems:
        charGroup.sprite.rect.x = 20
        charGroup.sprite.rect.y = 20
        functions.drawItems(numItems, itemGroup, itemColour, 0)
        score = 0
        if epsilon > 0:
            epsilon -= 0.1
        timeList.append(cTimer)
        print("Total time: " + str(format(cTimer, ".3f")))
        gameNum += 1
        if gameNum >= 2:
            timeDiff = timeList[-1] - timeList[-2]
            if timeDiff > 0:
                print("Time difference: +" + str(format(timeDiff, ".3f")))
            else:
                print("Time difference: " + str(format(timeDiff, ".3f")))
            
            timeArray = np.array(timeList)
            avTime = np.average(timeArray)
            print("Average time: " + str(format(avTime, ".3f")))
        timeNum = 1
        for x in timeList:
            print("Time " + str(timeNum) + ": " + str(format(x, ".3f")))
            timeNum += 1
        startTimer = time.time()
        print("**NEW GAME STARTED**")
        
pygame.quit()
