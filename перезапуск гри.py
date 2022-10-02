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