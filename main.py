from pygame import*
class Settings(sprite.Sprite): # sania
    def __init__(self,x,y,w,h,speed,img):
        super().__init__()

        self.speed = speed
        self.width = w
        self.heaight = h
        self.image = transform.scale(image.load(img),(self.width,self.height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class Player(Settings):
    
    def r_l(self):
        global mana, img, f
        f = 1
        keys = key.get_pressed()
        if keys [K_a]:
            self.rect.x -= self.speed
            f = 1
            mana.side = 'left'
        if keys [K_d]:
            self.rect.x += self.speed
            mana.side = 'right' 
            f = 0
        
        if f ==1:
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
        if f ==0:
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))

    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys [K_s]:
            self.rect.y += self.speed        

class Button():# sania
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
        
 class Player(Settings): #?
    
    def r_l(self):
        global mana, img, f
        f = 1
        keys = key.get_pressed()
        if keys [K_a]:
            self.rect.x -= self.speed
            f = 1
            mana.side = 'left'
        if keys [K_d]:
            self.rect.x += self.speed
            mana.side = 'right' 
            f = 0
        
        if f ==1:
            self.image = transform.scale(image.load(hero_r), (self.width, self.height))
        if f ==0:
            self.image = transform.scale(image.load(hero_l), (self.width, self.height))

    def u_d(self):
        keys = key.get_pressed()
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys [K_s]:
            self.rect.y += self.speed       
     
            
            
            
class Enemy(Settings): #nik
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)
        
        self.side = side
    
    def update(self):
        global side

        if self.side == 'right':
            self.rect.x -= self.speed
        if self.side == 'left':
            self.rect.x += self.speed
            
            
hero_r = "images/sprite1_r.png"
hero_l = "images/sprite1.png"

enemy_l = "images/cyborg.png"
enemy_r = "images/cyborg_r.png"

coin = "images/coin.png"
door_img = "images/door.png"
key_img = "images/key.png"
chest_open = "images/cst_open.png"
chest_close = "images/cst_close.png"
cyborg = "images/cyborg.png"
stair = "images/stair.png"
port = "images/portal.png"
platform = "images/platform.png"
nothing = "images/nothing.png"
power = "images/mana.png"
widght = 1280
height = 720

background = transform.scale(image.load('images/background.jpg'),(widght,height))

win = display.set_mode((widght, height))
win.blit(background, (0,0))

display.set_caption('Name_Game')

hero = Player(300, 650, 50, 50, 5, hero_1)

en1 = Enemy(400, 480, 50, 50, 3, enemy_1, 'left')
en2 = Enemy(230, 320, 50, 50, 3, enemy_1, 'left')

door = Settings(1000, 580, 40, 120, 0, door_img)

key1 = Settings(160, 350, 50, 20, 0, key_img)
key2 = Settings(1500, 350, 50, 20, 0, key_img)

portal = Settings(2700, 600, 100, 100, 0, port)

chest = Settings(450, 130, 80, 80, 0, chest_close)

camera = Camera(camera_configure, level_width, level_height)

blocks_r = []
blocks_l = []
coins = []
stairs = []
platforms = []

items = sprite.Group()

FPS = 60
clock = time.Clock()
game = True

x=y=0

for r in level:
    for c in r:
        if c == 'r':
            r1 = Settings(x, y, 40, 40,0, nothing)
            blocks_r.append(r1)
            items.add(r1)

        if c == 'l':
            r1 = Settings(x, y, 40, 40,0, nothing)
            blocks_l.append(r1)
            items.add(r1)

        if c == '/':
            r2 = Settings(x, y - 40, 40, 180, 0, stair)
            stairs.append(r2)
            items.add(r2)

        if c == '':
            r1 = Settings(x, y, 40, 40,0, coin)
            coins.append(r3)
            items.add(r3)

        if c == '*':
            r4 = Settings(x,y, 40,40 , 0, portal)
            items.add(r4)

        if c == '-':
            r5 = Settings(x, y, 40, 40 ,0 , platform)
            platforms.append(r5)
            items.add(r5)

        if c == '>':
            r6 = Settings(x, y - 40, 80, 80, 0, chest_close)
            items.add(r6)

        x +=40
    y+=40
    x = 0

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)
