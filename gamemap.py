import pygame as p
import os
#os.chdir('C:/Users/desktop/pythonstuff')
map1 = p.image.load('images/background.png')

class gameMap(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.velocity = 6
        
    def draw(self,w):
        w.blit(map1, (self.x,self.y))

