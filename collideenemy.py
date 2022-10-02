#Уничтожение врагов - Никита Большов
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
