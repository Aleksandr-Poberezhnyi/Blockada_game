# додаєио калькулятор зібраних монет
    coin_c = font2.render(': ' + str(c_count), True,(255,255,255))
    win.blit(transform.scale(image.load('images/coin.png'), (50,50)), (10,10))
    win.blit(coin_c, (55,15))

    for c in coin:
        if sprite.collide_rect(hero, c):
            c_coll.play()
            c_count += 1
            coins.remove(c)
            items.remove(c)
    