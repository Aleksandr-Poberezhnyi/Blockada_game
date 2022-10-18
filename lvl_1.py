def lvl_1():
    mixer.music.load('sounds/game.ogg')
    mixer.music.play()
    game = True
    while game: 
        time.delay(5)
        win.blit(bg, (0,0))
        keys = key.get_pressed()
        pos_x, pos_y = mouse.get_pos()

        for e in event.get():
            if e.type == QUIT:
                game = False
            if btn_pause.rectcollidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                    click.play()
                    mixer.music.stop()
                    pause()
                    game = False
        en1.update()
        en2.update()
        en3.update()
        en4.update()
        hero.r_1()
        mana.update()
        btn_pause.draw(10 , 0)
        collider()
        if keys [K_SPACE]:
            mana.rect.x,mana.rect.y = hero.rect.centerx, hero.rect.top
            manas.add(mana)
            items.add(mana)
            fire_s.play()

        camera.update(hero)
        for i in items:
            win.blit(i.image, camera.apply(i))

        if sprite.collide_rect(hero, en1) or sprite.collide_rect(hero, en2) or sprite.collide_rect(hero, en3) or sprite.collide_rect(hero, en4):
            restart()
            game = False
        if sprite.collide_rect(hero, portal):
            tv.play()
            lvl_end()
            game = False
        display.update()
menu()
