from pygame import*
class settings(sprite.Sprite):
    def __init__(self,x,y,w,h,speed,img):
        super().__init__()

        self.speed = speed
        self.width = w
        self.heaight = h
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Enemy(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)
        
        self.side = side
    
    def update(self):
        global side

        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed

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
