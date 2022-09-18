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