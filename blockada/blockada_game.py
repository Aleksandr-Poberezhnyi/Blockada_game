from pygame import*
from random import *
import os
width = 1280
height = 720
FPS = 60

win = display.set_mode((width,height))
display.set_caption("blockada")
background = transform.scale(image.load("background.jpg"),(width,height))
win.blit(background,(0,0))
game = True 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()

hero1 = "hero_right.png"
hero2 = "hero_left.png"
