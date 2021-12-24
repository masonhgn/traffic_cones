import pygame as p
import json
from gamemap import *
from entity import *

import os
import random
os.chdir('C:/Users/desktop/pythonstuff')
SCREEN_W = 800
SCREEN_H = 800

p.display.set_caption("CONE CHAOS! v0.0.1") #title of window, current version

w = p.display.set_mode((SCREEN_W, SCREEN_H))
game_state = 2 #game state variable, 2 means you're actively playing and dodging cones, 3 means you've died
velocity = 14 #speed player can move side to side
score = 0 #current score during game. SCORE IS JUST A TIMER THAT GOES UP 1 UNIT EVERY 1.5 SECONDS
highscore = 0 #player high score, stored in json file
score_count = 0 #made so the score is displayed accurately.
flag = 2 #made for only playing death sound once when player dies, otherwise it loops because it's in a loop


#data stuff
#open data file to get player's high score, can hold more data if needed
data = {
    'highscore': 0
}
with open('data.json') as f:
    data = json.load(f)
    highscore = data['highscore']


#game init, clock
p.init()
c = p.time.Clock()

#sound stuff, initialize sounds, load them
p.mixer.init()
music_sound = p.mixer.Sound('trafficcones/music/gamemusic.wav')
death_sound = p.mixer.Sound('trafficcones/music/gamesound.wav')
p.mixer.music.load('trafficcones/music/gamemusic.wav')
p.mixer.music.play(-1)

player_img = p.image.load('trafficcones/images/character.png')
lost_image = p.image.load('trafficcones/images/gameover.png')




class player(object):
    def __init__(self, x,y,width,height, leftReached, rightReached):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.leftReached = False
        self.rightReached = False
        
    def draw(self, w):
        self.right = self.x + self.width
        self.left = self.x
        self.bottom = self.y + self.height
        

        w.blit(player_img, (self.x,self.y))

        if (self.x > 720):
            self.rightReached = True
        if (self.x < 20):
            self.leftReached = True

        
                

    def moveRight(self):
        if not self.rightReached:
            self.x += velocity
        self.leftReached = False
    
    def moveLeft(self):
        if not self.leftReached:
            self.x -= velocity
        self.rightReached = False


map1 = gameMap(0,0)

cone = entity(20, 800, 60,60)
cone2 = entity(90, 800, 60,60)
cone3 = entity(160, 800, 60,60)
cone4 = entity(230, 800, 60,60)
cone5 = entity(300, 800, 60,60)
cone6 = entity(370, 800, 60,60)
cone7 = entity(440, 800, 60,60)
cone8 = entity(510, 800, 60,60)
cone9 = entity(580, 800, 60,60)
cone10 = entity(650, 800, 60,60)
cone11 = entity(720, 800, 60,60)
current_player = player(400,578,61,108, False, False)

def drawGame():
    if game_state == 2:
        map1.draw(w)
        current_player.draw(w)

        for e in entities:
            e.draw(w)
    p.display.update()


font = p.font.SysFont('chalkduster.ttf',40) #doesn't work
font2 = p.font.SysFont('chalkduster.ttf', 24)
BLACK = (0,0,0)
img = font.render('Your score: ', True, BLACK)


def resetGame():
    
    for e in entities:
        e.y = random.randint(-1000,-60)
    current_player.x = 330

    p.mixer.music.load('trafficcones/music/gamemusic.wav')
    p.mixer.music.play(-1)


run = True

while run:

    p.time.delay(30)

    for e in entities:
        rect1 = p.Rect(e.x+20,e.y+20, e.width-20, e.height-20)
        rect2 = p.Rect(current_player.x+20,current_player.y+20,current_player.width-20, current_player.height-20)
        collide = rect1.colliderect(rect2) #RECTANGLE COLLISION BETWEEN PLAYER AND ENTITIES
        if collide:
            game_state = 3


    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    if game_state == 2: #game currently being played
        
        score = round(p.time.get_ticks() / 1500) - score_count
        cap = "SCORE: " + str(score)
        
        for e in entities:
            e.conedrop()
    if game_state == 3:
        if flag == 2:
            p.mixer.Sound.play(death_sound)
            flag = 3
        w.blit(lost_image, (189, 254))
        
        img = font.render(cap, True, BLACK)
        w.blit(img, (330,430))
        if score > highscore:
            highscore = score
            data['highscore'] = highscore
            with open('data.json', 'w') as f: #data dump if new high score is reached
                json.dump(data, f)
        img2 = font.render("HIGH SCORE: " + str(highscore), True, BLACK)
        img3 = font2.render("Press G to start again or E to exit...", True, BLACK)
        w.blit(img3, (270, 470))
        w.blit(img2, (300, 320))

        
    k = p.key.get_pressed() 
    if k[p.K_d]:
        current_player.moveRight()
    elif k[p.K_a]:
        current_player.moveLeft()
    elif k[p.K_g] and game_state == 3:
        score_count = score
        resetGame()
        game_state = 2
        flag = 2
        
    elif k[p.K_e]:
        run = False
    
    drawGame()





p.quit()





