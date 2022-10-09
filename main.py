from pygame import*
#список уровня
lavel = ["                                                            ",
"                                                                     ",
"       0   0                      0 0 0                              ",
"       -------          0       -------                              ",
"                        0                             0              ",
"         0    0      ----------          0   0        -------        ",
"         0    0                       --------                       ",
"       --------                                    0                 ",
"                                                ------               ",
"                                                                     ",
"                                   ----------                        ",
"                                                                     ",
"                                                               0 0 0 ",
"---------------------------------------------------------------------",
]
# Главный класс
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
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y))
# Класс главный герой        
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

class Button():# Класс кнопок
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
            
            
class Camera(object):
    def __init__(self, camera-func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0,0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def camera_configure(camera, target_rect):
    l, t, _, _= target_rect
    _, _, w, h = camera
    l, t = 1 + W / 2, -t + H / 2

    l = min(0,1)
    l = max(-(camera.width - W), 1)
    t = max(-(camera.width - H), t)
    t = min(0, t)

    return Rect(l, t, w, h)


            
class Mana(Settings):
    def __init__(self, x, y, w, h, speed, img, side):
        Settings.__init__(self, x, y, w, h, speed, img)
        
        self.side = side
    
    def update(self):
        global side 

        if self.side == 'left':
            self.rect.x -= self.speed
        if self.side == 'right':
            self.rict.x += self.speed
            

mana = Mana(0, -100, 25, 25, 35, power, 'left')
            
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
            
# Класс камера и функция к ней
for r in blocks_r:

    if sprite.spritecollide(r,manas,True):
        kick.play()
        items.remove(mana)

    if sprite.collide_rect(hero,r):
        hero.rect.x = r.rect.x + hero.width - 5

    if sprite.collide_rect(en1,r):
        en1.side = "left"
        en1.image = transform.scale(image.load(enemy_l),(en1.width,en1.height))  
    
    
    if sprite.collide_rect(en2,r):
        en2.side = "left"
        en2.image = transform.scale(image.load(enemy_l),(en2.width,en2.height))  

        
    if sprite.collide_rect(en3,r):
        en3.side = "left"
        en3.image = transform.scale(image.load(enemy_l),(en3.width,en3.height)) 
    
    if sprite.collide_rect(en4,r):
        en4.side = "left"
        en4.image = transform.scale(image.load(enemy_l),(en3.width,en4.height)) 
        
        
 for l in blocks_l:

    if sprite.spritecollide(r,manas,True):
        kick.play()
        items.remove(mana)

    if sprite.collide_rect(hero,l):
        hero.rect.x = r.rect.x + hero.width - 5

    if sprite.collide_rect(en1,l):
        en1.side = "right"
        en1.image = transform.scale(image.load(enemy_r),(en1.width,en1.height))  
    
    
    if sprite.collide_rect(en2,l):
        en2.side = "right"
        en2.image = transform.scale(image.load(enemy_r),(en2.width,en2.height))  

        
    if sprite.collide_rect(en3,l):
        en3.side = "right"
        en3.image = transform.scale(image.load(enemy_r),(en3.width,en3.height)) 
    
    if sprite.collide_rect(en4,l):
        en4.side = "right"
        en4.image = transform.scale(image.load(enemy_r),(en3.width,en4.height)) 
        
        
# Переменные картинок
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
#  Музыка

# добавляем текст в игре

background = transform.scale(image.load('images/background.jpg'),(widght,height))
# Создание окна
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

# Создание кнопок
btn_start = Button((178, 34 , 34),470,300,280,70,"Start game",50,(255,255,255))
btn_control = Button((178, 34 , 34),470,450,280,70,"How to play",50,(255,255,255))
btn_exit = Button((178, 34 , 34),470,600,280,70,"exit game",50,(255,255,255))
btn_menu = Button((178, 34 , 34),470,600,280,70,"back to menu",50,(255,255,255))
btn_restart = Button((178, 34 , 34),470,450,280,70,"restart the game",50,(255,255,255))
btn_continue = Button((178, 34 , 34),470,450,280,70,"continue the game",50,(255,255,255))
btn_pause = Button((178, 34 , 34),1200,15,50,50,"I I",40,(255,255,255))

#текст в игре(пауза, вы проинарали и далее...)
font.init()

font1 = font.SysFont(('font/ariblk.ttf'), 200)
gname= font1.render('Blockada', True, (106, 90, 205), (250, 235, 215))

font2 = font.SysFont(('font/ariblk.ttf'), 60)
e_tap =font2.render('press (e)', True, (255,0,255))
k_need = font2.render('You need a key to open!', True, (255, 0 , 255))
space = font2.render('press (space) to kill the enemy', True, (255,0,255))

font3 = font.SysFont(('font/calibrib.ttf'), 45)
wasd_b =font3.render('WASD - move buttons. You can only go up and down the stairs', True, (255,0,0))
space_b = font3.render('Space - shoot button. You are a wizard who only knows one spell', True, (255, 0 , 0))
e_b = font3.render('E - interaction button. open doors, collect keys, activate portals', True, (255,0,0))

font4 = font.SysFont(('font/ariblk.ttf'), 150)
done =font4.render('LEVEL DONE!', True, (0,255,0), (255, 100, 0))
lose = font4.render('YOU LOSE!', True, (255, 0 , 0), (245, 222, 179))
pausa = font4.render('PAUSE', True, (255,0,0), (245, 222, 179))

# Создание списков и групп спрайтов (перенести в функцию перезапуска
blocks_r = []
blocks_l = []
coins = []
stairs = []
platforms = []

items = sprite.Group()

items.add(door)
items.add(key1)
items.add(key2)
items.add(portal)
items.add(chest)
items.add(en1)
items.add(en2)
items.add(en3)
items.add(en4)
items.add(hero)

k_door = False
k_chest = False
o_chest = False

FPS = 60
clock = time.Clock()
game = True
# Рисуем уровень (перенести в функцию перезапуска
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

        if c == '0':
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
# Функция перезапуска игры
# Создание спрайтов (перенести в функцию перезапуска
# Добавляем спрайты в группу
while game:

    time.delay(15)
    win.blit(bg,(0,0))
    keys = key.get_pressed()

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    en1.update()
    en2.update()

    hero.r_l()

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


    for r in blocks_r:
        if sprite.collide_rect(hero, r):
            hero.rect.x = r.rect.x + hero.width

        if sprite.collide_rect(en1, r):
            en1.side = 'left'
            en1.image = transform.scale(image.load(enemy_l), (en1.width, en1.heaight))

        if sprite.collide_rect(en2, r):
            en2.side = 'left'
            en2.image = transform.scale(image.load(enemy_l), (en2.width, en2.heaight))

    for l in blocks_l:
        if sprite.collide_rect(hero, l):
            hero.rect.x = l.rect.x - hero.width

        if sprite.collide_rect(en1, l):
            en1.side = 'right'
            en1.image = transform.scale(image.load(enemy_r), (en1.width, en1.heaight))

        if sprite.collide_rect(en2, l):
            en2.side = 'right'
            en2.image = transform.scale(image.load(enemy_r), (en2.width, en2.heaight))

    coin_c = font2.render(': ' + str(c_count), True,(255,255,255))
    win.blit(transform.scale(image.load('images/coin.png'), (50,50)), (10,10))
    win.blit(coin_c, (55,15))

    for c in coin:
        if sprite.collide_rect(hero, c):
            c_coll.play()
            c_count += 1
            coins.remove(c)
            items.remove(c)
# поднимаемся по лестнице Большов Никита
    if sprite.collide_rect(hero, key1):
        win.blit(e_tab, (500, 50))
        if keys[K_e]
            k_chest = True
            key1.rect.y = -100
            items.remove(key1)
            k_up.play()
    if sprite.collide_rect(hero, key2):
        win.blit(e_tab, (500, 50))
        if keys[K_e]:
            k_door = True
            key2.rect.y = -100
            items.remove(key2)
            k_up.play()
if sprite.collide_rect(hero,door) and k_door == False:
    win.blit(k_need, (450,50))
    hero.rect.x = door.rect.x - 47

if sprie.collide_rect(hero, door) and k_door == True:
    hero.rect.x = door.rect.x - 47
    win.blit(e_tap,(500,50))
    if keys[K_e]:
        door.rect.x += 1500
        d_o.play()
        k_door = False
if sprite.collide_rect(hero,chest) and k_chest == False:
    win.blit(k_need, (450,50))


if sprie.collide_rect(hero, chest) and k_chest == True:
    win.blit(e_tap,(500,50))
    if keys[K_e]:
        o_chest = True
        c_count += 10
        chest.image = transform.scale(image.load(chest_open),(chest.width,chest.height))
        cst_o.play()
        k_chest = True
    if sprite.spritecollide(en1, manas, True):
        en1.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en2, manas, True):
        en2.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en3, manas, True):
        en3.rect.y = -150
        items.remove(mana)
        kick.play()
    if sprite.spritecollide(en4, manas, True):
        en4.rect.y = -150
        items.remove(mana)
        kick.play()
# касание портала
# движение камеры
    display.update()
    clock.tick(FPS)
#Функция меню
def rules():
    rule = True
    mixer.music.stop()

    while rule:

        for e in event.get():
            if e.type == QUIT:
                rule = False

        time.delay(15)
        
        
        win.blit(bg, (0, 0 ))
        win.blit(gname, (320, 70 ))
        win.blit(wasd_b, (50, 250 ))
        win.blit(space_b, (50, 350 ))
        win.blit(e_b, (50, 450 ))

        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if btn_menu.rect.collidepoint((pos_, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                rule = False
                menu()

            if e.type == QUIT:
                rule = False

        display.update()
# Пауза в игре
def restart(): # пepeзanyck

    over = True

    mixer.music.stop()
    mixer.music.load('sounds/game_over.ogg')
    mixer.music.play()

    while over:

        for e in event.get(): # закриваємо вікно гри
            if e.type == QUIT:
                over = False

        time.delay(15)

        win.fill((0, 0, 0))
        win.blit(lose, (350, 200))

        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            # перезапускаемо гру
            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                over = False
                res_pos()
                lvl_1()
            # меню
            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN: 
                click.play()   
                over = False               
                menu()


        display.update()
# Уровень пройден
