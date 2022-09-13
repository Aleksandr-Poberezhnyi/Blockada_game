from pygame import*

widght = 1280
height = 720

background = transform.scale(image.load('images/background.jpg'),(widght,height))

win = display.set_mode((widght, height))
win.blit(background, (0,0))

display.set_caption('Name_Game')

FPS = 60
clock = time.Clock()
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
