import pygame as p
import random
entity_velocity = 14
entity_collide = False
entities = []


cone = p.image.load('images/cone.png')

if entity_collide:
    entity_velocity = 0

class entity(object):
    def __init__(self, x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        entities.append(self)

    

    def draw(self, w):
        self.bottom = self.y + self.height
        w.blit(cone, (self.x, self.y))

    
    def conedrop(self):
        
        self.y += entity_velocity
        if self.y > 800:
            self.y = random.randint(-1000,-60)
            


