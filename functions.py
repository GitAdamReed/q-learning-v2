# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 15:30:59 2020

@author: Adam
"""

#import pygame
import random
#import numpy as np
import classes

def drawItems(numItems, itemGroup, colour, seed):
    random.seed(seed)
    i = 0
    
    while i < numItems:
        x = random.randint(20, 770)
        y = random.randint(20, 570)
        item = classes.Item(colour, x, y, 10, 10)
        itemGroup.add(item)
        i = i + 1