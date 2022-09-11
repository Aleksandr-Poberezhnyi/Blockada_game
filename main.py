from pygame import*

widght = 1280
height = 720

win = display.set_mode((widght, height))
win.blit(background, (0,0))

win.set_caption('Name_Game')

FPS = 60

game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
