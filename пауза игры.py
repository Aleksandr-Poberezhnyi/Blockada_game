def pause(): # nayзa    
    stop = True

    mixer.music.stop() # зупинка вси звуKİв

    while stop:

        for e in event.get(): # закpиваемо вiкно гри
            if e.type == QUIT: 
                stop = False

        time.delay(15)

        win.fill((0, 0, 0))
        win.blit(pausa, (440, 200)) 
        # відображення кнопок
        btn_continue.draw(58, 5)
        btn_restart.draw(60, 5)
        btn_menu.draw(0, 5)

        pos_x, pos_y= mouse.get_pos()

        for e in event.get():
            # продовжуємо ГРУ
            if btn_continue.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN: 
                click.play()
                stop = False
                mixer.music.stop()
                lvl_1()
            # перезапуск рiвня
            if btn_restart.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                res_pos()
                mixer.music.stop()
                stop = False
                1v1_1()
            # меню
            if btn_menu.rect.collidepoint((pos_x, pos_y)) and e.type == MOUSEBUTTONDOWN:
                click.play()
                mixer.music.stop()
                stop = False 
                game = False
                menu()
        display.update()