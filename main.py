from pygame import*
class Settings(sprite.Sprite): # eto sania
    def __init__(self,x,y,w,h,speed,img):
        super().__init__()

        self.speed = speed
        self.width = w
        self.heaight = h
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
  class Button(): # eto sania
        def __init__(self,color,x,y,w,h,text,fsize,txt_color):

            self.width = w
            self.heaight = h
            self.color = color

            self.image = Surface([self.width, self.height])
            self.image.fill((color))

            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

            self.fsize = fsize
            self.text = text
            self.txt_color = txt_color
            self.txt_image = font.Font('font/impact.tff',fsize).render(text, True,txt_color)

        def draw(self,shift_x,shift_y):#paint button with text in middle, text moved with shift_x and shift_y
            win.blit(self.image,(self.rect.x self.rect.y))
            win.blit(self.txt_image, (self.rect.x + shift_x, self.rect.y + shift_y))


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
