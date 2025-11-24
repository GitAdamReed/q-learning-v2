# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:07:47 2020

@author: Adam
"""

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, texture, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(texture)
        
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 10
    
    def get_pos(self):
        self.pos = [self.rect.x, self.rect.y]
        return self.pos
        
class Item(pygame.sprite.Sprite):
    def __init__(self, texture, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(texture)
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Scan(pygame.sprite.Sprite):
    def __init__(self, texture, width, height):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([width, height])
        self.image.fill(texture)
        
        self.rect = self.image.get_rect()