from game.engine import global_var

engine_root = global_var.engine_root
current_scene = None

engine_root.moding_virtual_screen(mod='default')

#software render
btn = [engine_root.load_image('game/assets/images/btn_off.png', 300, 120), engine_root.load_image('game/assets/images/btn_on.png', 300, 120)]
btn_mini = [engine_root.load_image('game/assets/images/btn_off.png', 150, 60), engine_root.load_image('game/assets/images/btn_on.png', 150, 60)]
dialog_icon = [engine_root.load_image('game/assets/images/an.png', 161, 161), engine_root.load_image('game/assets/images/wabani.png', 161, 161)]
dialog_window = engine_root.load_image('game/assets/images/dialog.png', 1200, 250)
map = engine_root.load_image('game/assets/images/map_prologue_optimized.png', 1824, 1824)

fps_font = engine_root.load_font('game/assets/font/determination.otf', 40)
border_fps = engine_root.load_image('game/assets/images/black.webp', 150, 40)

in_game = False
quick_scene = None
next_scene = None

def standart_iteria():
    for event in engine_root.walmen_const.event.get():
        if event.type == engine_root.walmen_const.QUIT:
            engine_root.exit()
        elif event.type == engine_root.walmen_const.VIDEORESIZE:
            engine_root.set_resize_window(event.size)
        elif event.type == engine_root.walmen_const.KEYDOWN:
            if event.key == engine_root.walmen_const.K_ESCAPE:
                if in_game == True:
                    return 'pause'
                else:
                    pass
            if event.key == engine_root.walmen_config.key_up:
                if in_game == True:
                    return 'up'
                else:
                    pass
            if event.key == engine_root.walmen_config.key_down:
                if in_game == True:
                    return 'down'
                else:
                    pass
            if event.key == engine_root.walmen_config.key_left:
                if in_game == True:
                    return 'left'
                else:
                    pass
            if event.key == engine_root.walmen_config.key_right:
                if in_game == True:
                    return 'right'
                else:
                    pass
            if event.key == engine_root.walmen_config.key_attack:
                if in_game == True:
                    if next_scene != None:
                        return 'next_scene'
                    else:
                        return 'used'
                else:
                    pass
        elif event.type == engine_root.MUSIC_END:
            return 'end_music'
                
def switch_scene(scene):
    global current_scene
    current_scene = scene

def menu():
    engine_root.walmen_audio.load(f'game/assets/sound/menu.ogg')
    engine_root.walmen_audio.play(-1)

    engine_root.walmen_time.sleep(0.1)

    font_size = [20, 50]

    font_20 = engine_root.load_font('game/assets/font/determination.otf', font_size[0])
    font_50 = engine_root.load_font('game/assets/font/determination.otf', font_size[1])

    run = True
    while run:
        standart_iteria()

        walmen_mouseX, walmen_mouseY = engine_root.walmen_const.mouse.get_pos()
        walmen_mouse_pressed = engine_root.walmen_const.mouse.get_pressed()
        SurfX, SurfY = engine_root.current_size_window[0]/100, engine_root.current_size_window[1]/100
        walmen_adapt_X = (engine_root.width_native/100)/SurfX
        walmen_adapt_y = (engine_root.height_native/100)/SurfY

        engine_root.draw(engine_root.load_image('game/assets/images/menu_optimized.png', engine_root.width_native, engine_root.height_native), 0, 0)

        engine_root.draw(btn[0], 820, 185)
        engine_root.draw(btn[0], 820, 310)
        engine_root.draw(btn[0], 820, 440)

        
        #engine_root.draw(engine_root.load_text(engine_root.load_font('game/assets/font/determination.otf', 50), f'{engine_root.walmen_language.get_localize('play')}'), 900, 220)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('play')}'), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('play')), 220)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('settings')}'), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('settings')), 345)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}'), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 475)
        engine_root.draw(engine_root.load_text(font_20, 'Miracle Blaze v0.01', (128,128,128)), 725, 595)
        engine_root.draw(engine_root.load_text(font_20, '         WALM 2025', (128,128,128)), 725, 620)

        if walmen_mouse_pressed == (False, False, False):
            if walmen_mouseX >= 820/walmen_adapt_X and walmen_mouseX <= 1120/walmen_adapt_X:
                if walmen_mouseY >=185/walmen_adapt_y and walmen_mouseY <= 305/walmen_adapt_y:
                    engine_root.draw(btn[1], 820, 185)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('play')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('play')), 220)

                if walmen_mouseY >=310/walmen_adapt_y and walmen_mouseY <= 430/walmen_adapt_y:
                    engine_root.draw(btn[1], 820, 310)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('settings')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('settings')), 345)

                if walmen_mouseY >=440/walmen_adapt_y and walmen_mouseY <= 560/walmen_adapt_y:
                    engine_root.draw(btn[1], 820, 440)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(820, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 475)

        if walmen_mouse_pressed == (True, False, False):
            if walmen_mouseX >= 820/walmen_adapt_X and walmen_mouseX <= 1120/walmen_adapt_X:
                if walmen_mouseY >=185/walmen_adapt_y and walmen_mouseY <= 305/walmen_adapt_y:
                    switch_scene(start_game)
                    run=False

                if walmen_mouseY >=310/walmen_adapt_y and walmen_mouseY <= 430/walmen_adapt_y:
                    switch_scene(settings)
                    run=False

                if walmen_mouseY >=440/walmen_adapt_y and walmen_mouseY <= 560/walmen_adapt_y:
                    engine_root.exit()

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_screen()

def settings():
    
    engine_root.walmen_audio.load(f'game/assets/sound/backroom.ogg')
    engine_root.walmen_audio.play(-1)

    engine_root.walmen_time.sleep(0.1)

    font_size = [40, 50, 60]

    font_40 = engine_root.load_font('game/assets/font/determination.otf', font_size[0])
    font_50 = engine_root.load_font('game/assets/font/determination.otf', font_size[1])
    font_60 = engine_root.load_font('game/assets/font/determination.otf', font_size[2])

    run = True
    while run:
        standart_iteria()

        walmen_mouseX, walmen_mouseY = engine_root.walmen_const.mouse.get_pos()
        walmen_mouse_pressed = engine_root.walmen_const.mouse.get_pressed()
        SurfX, SurfY = engine_root.current_size_window[0]/100, engine_root.current_size_window[1]/100
        walmen_adapt_X = (engine_root.width_native/100)/SurfX
        walmen_adapt_y = (engine_root.height_native/100)/SurfY

        engine_root.draw(btn[0], 895, 515)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}'), engine_root.walmen_technology.adaptive_text(895, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 550)

        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('settings')}'), 100, 40)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('fullscreen')}'), 100, 150)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('sound')}'), 100, 250)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('speak')}'), 100, 325)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('lang')}'), 100, 400)

        engine_root.draw(btn_mini[0], 650, 150)
        engine_root.draw(engine_root.load_text(font_40, f'{engine_root.walmen_language.get_localize('on')}', (255,255,255)), engine_root.walmen_technology.adaptive_text(650, 150, font_size[0], engine_root.walmen_language.get_localize('on')), 160)
        
        engine_root.draw(btn_mini[0], 825, 150)
        engine_root.draw(engine_root.load_text(font_40, f'{engine_root.walmen_language.get_localize('off')}', (255,255,255)), engine_root.walmen_technology.adaptive_text(825, 150, font_size[0], engine_root.walmen_language.get_localize('off')), 160)

        engine_root.draw(btn_mini[0], 650, 250)
        engine_root.draw(engine_root.load_text(font_60, '-'), 715, 250)

        engine_root.draw(btn_mini[0], 825, 250)
        engine_root.draw(engine_root.load_text(font_60, '+'), 890, 250)

        engine_root.draw(btn_mini[0], 650, 325)
        engine_root.draw(engine_root.load_text(font_60, '-'), 715, 325)

        engine_root.draw(btn_mini[0], 825, 325)
        engine_root.draw(engine_root.load_text(font_60, '+'), 890, 325)

        engine_root.draw(btn_mini[0], 650, 400)
        engine_root.draw(engine_root.load_text(font_60, f'{engine_root.walmen_language.get_localize('en-us')}'), 700, 400)

        engine_root.draw(btn_mini[0], 825, 400)
        engine_root.draw(engine_root.load_text(font_60, f'{engine_root.walmen_language.get_localize('ru-ru')}'), 875, 400)

        engine_root.draw(btn[0], 100, 500)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('controls')}'), engine_root.walmen_technology.adaptive_text(100, 300, font_size[1], engine_root.walmen_language.get_localize('controls')), 535)

        if walmen_mouse_pressed == (False, False, False):
            if walmen_mouseX >= 895/walmen_adapt_X and walmen_mouseX <= 1195/walmen_adapt_X:
                if walmen_mouseY >=515/walmen_adapt_y and walmen_mouseY <= 635/walmen_adapt_y:
                    engine_root.draw(btn[1], 895, 515)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(895, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 550)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=150/walmen_adapt_y and walmen_mouseY <=210/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 650, 150)
                    engine_root.draw(engine_root.load_text(font_40, f'{engine_root.walmen_language.get_localize('on')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(650, 150, font_size[0], engine_root.walmen_language.get_localize('on')), 160)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=150/walmen_adapt_y and walmen_mouseY <=210/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 825, 150)
                    engine_root.draw(engine_root.load_text(font_40, f'{engine_root.walmen_language.get_localize('off')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(825, 150, font_size[0], engine_root.walmen_language.get_localize('off')), 160)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=250/walmen_adapt_y and walmen_mouseY <=310/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 650, 250)
                    engine_root.draw(engine_root.load_text(font_60, '-', (255,255,0)), 715, 250)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=250/walmen_adapt_y and walmen_mouseY <=310/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 825, 250)
                    engine_root.draw(engine_root.load_text(font_60, '+', (255,255,0)), 890, 250)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=325/walmen_adapt_y and walmen_mouseY <=385/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 650, 325)
                    engine_root.draw(engine_root.load_text(font_60, '-', (255,255,0)), 715, 325)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=325/walmen_adapt_y and walmen_mouseY <=385/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 825, 325)
                    engine_root.draw(engine_root.load_text(font_60, '+', (255,255,0)), 890, 325)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=400/walmen_adapt_y and walmen_mouseY <=460/walmen_adapt_y:
                    engine_root.draw(btn_mini[1], 650, 400)
                    engine_root.draw(engine_root.load_text(font_60, f'{engine_root.walmen_language.get_localize('en-us')}', (255,255,0)), 700, 400)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=400/walmen_adapt_y and walmen_mouseY <=460/walmen_adapt_y:
                    engine_root.draw(btn_mini[0], 825, 400)
                    engine_root.draw(engine_root.load_text(font_60, f'{engine_root.walmen_language.get_localize('ru-ru')}', (255,255,0)), 875, 400)
            if walmen_mouseX >=100/walmen_adapt_X and walmen_mouseX<=400/walmen_adapt_X:
                if walmen_mouseY >=500/walmen_adapt_y and walmen_mouseY <=620/walmen_adapt_y:
                    engine_root.draw(btn[1], 100, 500)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('controls')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(100, 300, font_size[1], engine_root.walmen_language.get_localize('controls')), 535)

        if walmen_mouse_pressed == (True, False, False):
            if walmen_mouseX >= 895/walmen_adapt_X and walmen_mouseX <= 1195/walmen_adapt_X:
                if walmen_mouseY >=515/walmen_adapt_y and walmen_mouseY <= 635/walmen_adapt_y:
                    switch_scene(menu)
                    run=False
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=150/walmen_adapt_y and walmen_mouseY <=210/walmen_adapt_y:
                    engine_root.turn_fullscreen(mode=True)
                    engine_root.display_reinit()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=150/walmen_adapt_y and walmen_mouseY <=210/walmen_adapt_y:
                    engine_root.turn_fullscreen(mode=False)
                    engine_root.display_reinit()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=250/walmen_adapt_y and walmen_mouseY <=310/walmen_adapt_y:
                    engine_root.volume_down()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=250/walmen_adapt_y and walmen_mouseY <=310/walmen_adapt_y:
                    engine_root.volume_up()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=325/walmen_adapt_y and walmen_mouseY <=385/walmen_adapt_y:
                    engine_root.speak_down()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=325/walmen_adapt_y and walmen_mouseY <=385/walmen_adapt_y:
                    engine_root.speak_up()
                    engine_root.walmen_time.sleep(0.1)
            if walmen_mouseX >=650/walmen_adapt_X and walmen_mouseX<=800/walmen_adapt_X:
                if walmen_mouseY >=400/walmen_adapt_y and walmen_mouseY <=460/walmen_adapt_y:
                    engine_root.change_lang('eng')
                    engine_root.walmen_time.sleep(0.5)
            if walmen_mouseX >=825/walmen_adapt_X and walmen_mouseX<=975/walmen_adapt_X:
                if walmen_mouseY >=400/walmen_adapt_y and walmen_mouseY <=460/walmen_adapt_y:
                    engine_root.change_lang('rus')
                    engine_root.walmen_time.sleep(0.5)
            if walmen_mouseX >=100/walmen_adapt_X and walmen_mouseX<=400/walmen_adapt_X:
                if walmen_mouseY >=500/walmen_adapt_y and walmen_mouseY <=620/walmen_adapt_y:
                    switch_scene(controls)
                    run = False

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_screen()

def controls():
    engine_root.walmen_time.sleep(0.1)

    font_size = [45, 50, 60,30]

    font_45 = engine_root.load_font('game/assets/font/determination.otf', font_size[0])
    font_50 = engine_root.load_font('game/assets/font/determination.otf', font_size[1])
    font_60 = engine_root.load_font('game/assets/font/determination.otf', font_size[2])
    run = True
    while run:
        standart_iteria()

        walmen_mouseX, walmen_mouseY = engine_root.walmen_const.mouse.get_pos()
        walmen_mouse_pressed = engine_root.walmen_const.mouse.get_pressed()
        SurfX, SurfY = engine_root.current_size_window[0]/100, engine_root.current_size_window[1]/100
        walmen_adapt_X = (engine_root.width_native/100)/SurfX
        walmen_adapt_y = (engine_root.height_native/100)/SurfY

        key_up = engine_root.walmen_const.key.name(engine_root.walmen_config.key_up)
        key_down = engine_root.walmen_const.key.name(engine_root.walmen_config.key_down)
        key_left = engine_root.walmen_const.key.name(engine_root.walmen_config.key_left)
        key_right = engine_root.walmen_const.key.name(engine_root.walmen_config.key_right)
        key_abilities = engine_root.walmen_const.key.name(engine_root.walmen_config.key_abilities)
        key_attack = engine_root.walmen_const.key.name(engine_root.walmen_config.key_attack)

        engine_root.draw(engine_root.load_text(font_60, f'{engine_root.walmen_language.get_localize('controls')}'), 100, 40)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('up')} - {key_up}'), 100, 140)
        engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('abilities')} - {key_abilities}'), 600, 140)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('down')} - {key_down}'), 100, 240)
        engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('attack')} - {key_attack}'), 600, 240)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('left')} - {key_left}'), 100, 340)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('right')} - {key_right}'), 100, 440)

        engine_root.draw(btn[0], 895, 515)
        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}'), engine_root.walmen_technology.adaptive_text(895, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 550)
        
        
        if walmen_mouse_pressed == (False, False, False):
            if walmen_mouseX >= 895/walmen_adapt_X and walmen_mouseX <= 1195/walmen_adapt_X:
                if walmen_mouseY >=515/walmen_adapt_y and walmen_mouseY <= 635/walmen_adapt_y:
                    engine_root.draw(btn[1], 895, 515)
                    engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('exit')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(895, 300, font_size[1], engine_root.walmen_language.get_localize('exit')), 550)

        if walmen_mouse_pressed == (True, False, False):
            if walmen_mouseX >= 895/walmen_adapt_X and walmen_mouseX <= 1195/walmen_adapt_X:
                if walmen_mouseY >=515/walmen_adapt_y and walmen_mouseY <= 635/walmen_adapt_y:
                    switch_scene(menu)
                    run=False

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_screen()

def pause():
    engine_root.walmen_audio.stop()
    engine_root.walmen_audio.load(f'game/assets/sound/panelka.ogg')
    engine_root.walmen_audio.play(-1)

    font_50 = engine_root.load_font('game/assets/font/determination.otf', 50)
    font_45 = engine_root.load_font('game/assets/font/determination.otf', 40)

    run = True
    while run:
        standart_iteria()

        walmen_mouseX, walmen_mouseY = engine_root.walmen_const.mouse.get_pos()
        walmen_mouse_pressed = engine_root.walmen_const.mouse.get_pressed()
        SurfX, SurfY = engine_root.current_size_window[0]/100, engine_root.current_size_window[1]/100
        walmen_adapt_X = (engine_root.width_native/100)/SurfX
        walmen_adapt_y = (engine_root.height_native/100)/SurfY

        engine_root.draw(engine_root.load_text(font_50, f'{engine_root.walmen_language.get_localize('pause')}'), 575, 40)

        engine_root.draw(btn[0], 200, 200)
        engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('continue')}', (255,255,255)), engine_root.walmen_technology.adaptive_text(200, 300, 40, engine_root.walmen_language.get_localize('continue')), 235)

        engine_root.draw(btn[0], 760, 200)
        engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('main menu')}', (255,255,255)), engine_root.walmen_technology.adaptive_text(760, 300, 40, engine_root.walmen_language.get_localize('main menu')), 235)

        if walmen_mouse_pressed == (False, False, False):
            if walmen_mouseX >= 200/walmen_adapt_X and walmen_mouseX <= 500/walmen_adapt_X:
                if walmen_mouseY >=200/walmen_adapt_y and walmen_mouseY <= 320/walmen_adapt_y:
                    engine_root.draw(btn[1], 200, 200)
                    engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('continue')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(200, 300, 40, engine_root.walmen_language.get_localize('continue')), 235)
            if walmen_mouseX >= 760/walmen_adapt_X and walmen_mouseX <= 1060/walmen_adapt_X:
                if walmen_mouseY >=200/walmen_adapt_y and walmen_mouseY <= 320/walmen_adapt_y:
                    engine_root.draw(btn[1], 760, 200)
                    engine_root.draw(engine_root.load_text(font_45, f'{engine_root.walmen_language.get_localize('main menu')}', (255,255,0)), engine_root.walmen_technology.adaptive_text(760, 300, 40, engine_root.walmen_language.get_localize('main menu')), 235)

        if walmen_mouse_pressed == (True, False, False):
            if walmen_mouseX >= 200/walmen_adapt_X and walmen_mouseX <= 500/walmen_adapt_X:
                if walmen_mouseY >=200/walmen_adapt_y and walmen_mouseY <= 320/walmen_adapt_y:
                    switch_scene(quick_scene)
                    run=False
            if walmen_mouseX >= 760/walmen_adapt_X and walmen_mouseX <= 1060/walmen_adapt_X:
                if walmen_mouseY >=200/walmen_adapt_y and walmen_mouseY <= 320/walmen_adapt_y:
                    switch_scene(menu)
                    run=False

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_screen()

def start_game():
    global animation_text, in_game, quick_scene, next_scene, anonymous_voites

    engine_root.walmen_audio.stop()
    engine_root.update_screen()

    for i in range(5000):
        engine_root.walmen_time.sleep(0.001)
        standart_iteria()

    engine_root.walmen_audio.load(f'game/assets/sound/day, no Mira.ogg')
    engine_root.walmen_audio.play(-1)

    anonymous_voites = engine_root.walmen_language.get_localize('anonymous_voites')

    animation_text = 1
    in_game = 1
    next_scene = None

    dialog_font = engine_root.load_font('game/assets/font/determination.otf', 40)

    run = True
    while run:
        iteria = standart_iteria()

        if iteria == 'pause':
            quick_scene = start_game
            engine_root.walmen_time.sleep(0.1)
            switch_scene(pause)
            run=False
        elif iteria == 'next_scene':
            switch_scene(next_scene)
            run = False

        if animation_text == 1:

            dialog_window_object = engine_root.walmen_technology.dialog_window_animation(engine_root, standart_iteria, dialog_font, 130, 37, 400, 300, anonymous_voites[0], dialog_window, dialog_icon[0], 0.06, 'game/assets/sound/anonymous.wav')
            if dialog_window_object == True:
                animation_text = 0
                next_scene = map_prologue
                continue
            elif dialog_window_object == 'pause':
                quick_scene = start_game
                engine_root.walmen_time.sleep(0.1)
                switch_scene(pause)
                run=False
        elif animation_text == 0:
            engine_root.walmen_technology.self_dialog_window(engine_root, dialog_window, dialog_icon[0], dialog_font, anonymous_voites[0])

            if engine_root.walmen_const.mixer.music.get_pos()/1000 >= 35.000:
                engine_root.walmen_audio.play(-1)

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_teck_screen()

def map_prologue():
    global quick_scene, next_scene

    wabani_right = [engine_root.load_image('game/assets/images/wabani/right/animation/1.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/right/animation/2.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/right/animation/3.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/right/animation/4.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/right/animation/5.png', 256,256)]
    
    wabani_up = [engine_root.load_image('game/assets/images/wabani/up/animation/1.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/up/animation/2.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/up/animation/3.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/up/animation/4.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/up/animation/5.png', 256,256)]
    
    wabani_left = [engine_root.load_image('game/assets/images/wabani/left/animation/1.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/left/animation/2.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/left/animation/3.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/left/animation/4.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/left/animation/5.png', 256,256)]
    
    wabani_down = [engine_root.load_image('game/assets/images/wabani/down/animation/1.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/down/animation/2.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/down/animation/3.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/down/animation/4.png', 256,256),
              engine_root.load_image('game/assets/images/wabani/down/animation/5.png', 256,256)]
    
    wabani = wabani_down
    
    wabani_anim_number = 0
    anim_fps = 0
    scene_camera_x = 0
    scene_camera_y = 0
    wabani_speed = 5
    x_wabani = 385
    y_wabani = 475

    next_scene = None

    run=True
    while run:

        iteria = standart_iteria()
        if iteria == 'pause':
            quick_scene = start_game
            engine_root.walmen_time.sleep(0.1)
            switch_scene(pause)
            run=False
        elif iteria == 'up':
            wabani = wabani_up
        elif iteria == 'down':
            wabani = wabani_down
        elif iteria == 'left':
            wabani = wabani_left
        elif iteria == 'right':
            wabani = wabani_right
        elif iteria == 'used':
            if x_wabani >= 245 and x_wabani <=550:
                if y_wabani >= 1285 and y_wabani <= 1500:
                    switch_scene(hello_dialog)
                    run = False

        wabani_keys=engine_root.walmen_const.key.get_pressed()
        if wabani_keys[engine_root.walmen_config.key_up]:
            if y_wabani <= 40 or y_wabani <= 1015 and x_wabani >=800:
                y_wabani +=wabani_speed
            else:
                y_wabani -=wabani_speed
        elif wabani_keys[engine_root.walmen_config.key_down]:
            if y_wabani >= 1510:
                y_wabani -=wabani_speed
            else:
                y_wabani +=wabani_speed
        elif wabani_keys[engine_root.walmen_config.key_left]:
            if x_wabani <= -45:
                pass
            else:
                x_wabani -=wabani_speed           
        elif wabani_keys[engine_root.walmen_config.key_right]:
            if x_wabani >=800 and y_wabani <=950 or x_wabani >= 1600:
                pass
            else:
                x_wabani +=wabani_speed

        if wabani_keys[engine_root.walmen_config.key_up] and wabani_keys[engine_root.walmen_config.key_right]:    
            if x_wabani >=800 and y_wabani <=950 or x_wabani >= 1600:
                pass
            else:
                x_wabani +=wabani_speed/2
                y_wabani -=wabani_speed/2
        elif wabani_keys[engine_root.walmen_config.key_up] and wabani_keys[engine_root.walmen_config.key_left]:
            if x_wabani <= -45:
                pass
            else:
                x_wabani -=wabani_speed/2
                y_wabani -=wabani_speed/2
        elif wabani_keys[engine_root.walmen_config.key_down] and wabani_keys[engine_root.walmen_config.key_right]:
            if x_wabani >=800 and y_wabani <=950 or x_wabani >= 1600:
                pass
            else:
                x_wabani +=wabani_speed/2
                y_wabani +=wabani_speed/2
        elif wabani_keys[engine_root.walmen_config.key_down] and wabani_keys[engine_root.walmen_config.key_left]:
            if x_wabani <= -45:
                pass
            else:
                x_wabani -=wabani_speed/2
                y_wabani +=wabani_speed/2

        if anim_fps != 60:
            anim_fps +=1*60/4
        else:
            if wabani_anim_number != 4:
                wabani_anim_number +=1
            else:
                wabani_anim_number = 0

            anim_fps = 0

        if x_wabani - scene_camera_x != 0:
            scene_camera_x += (x_wabani - (engine_root.walmen_config.width_native/2 - 128) - scene_camera_x)/wabani_speed

        if y_wabani - scene_camera_y != 0:
            scene_camera_y += (y_wabani - (engine_root.walmen_config.height_native/2 - 128) - scene_camera_y)/wabani_speed

        engine_root.draw(map, 0-scene_camera_x, 0-scene_camera_y)

        engine_root.draw(wabani[wabani_anim_number], x_wabani-scene_camera_x, y_wabani-scene_camera_y)

        if engine_root.walmen_const.mixer.music.get_pos()/1000 >= 35.000:
            engine_root.walmen_audio.play(-1)

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS: {int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)

        if run != False:
            engine_root.update_screen()

def hello_dialog():
    global animation_text, in_game, quick_scene, next_scene

    wabani_voites = engine_root.walmen_language.get_localize('wabani_voites')

    animation_text = 1
    in_game = 1
    next_scene = None

    dialog_font = engine_root.load_font('game/assets/font/determination.otf', 40)

    run = True
    while run:
        iteria = standart_iteria()

        if iteria == 'pause':
            quick_scene = start_game
            engine_root.walmen_time.sleep(0.1)
            switch_scene(pause)
            run=False
        elif iteria == 'next_scene':
            switch_scene(next_scene)
            run = False

        if animation_text == 1:
            dialog_window_object = engine_root.walmen_technology.dialog_window_animation(engine_root, standart_iteria, dialog_font, 130, 37, 400, 300, wabani_voites[0], dialog_window, dialog_icon[1], 0.06, 'game/assets/sound/silent.wav')
            if dialog_window_object == True:
                animation_text = 0
                engine_root.update_screen()
                next_scene = monolog_anona
                continue
            elif dialog_window_object == 'pause':
                quick_scene = start_game
                engine_root.walmen_time.sleep(0.1)
                switch_scene(pause)
                run=False
        elif animation_text == 0:
            engine_root.walmen_technology.self_dialog_window(engine_root, dialog_window, dialog_icon[1], dialog_font, wabani_voites[0])

            if engine_root.walmen_const.mixer.music.get_pos()/1000 >= 35.000:
                engine_root.walmen_audio.play(-1)

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)
        engine_root.update_teck_screen()

def monolog_anona():
    global quick_scene, next_scene

    run = True
    animation_text = 1
    next_scene = None

    dialog_mass = 0

    engine_root.update_screen()

    engine_root.walmen_time.sleep(0.05)

    dialog_font = engine_root.load_font('game/assets/font/determination.otf', 40)

    engine_root.walmen_audio.play(-1, start=35.5)

    while run:
        iteria = standart_iteria()

        if iteria == 'pause':
            quick_scene = start_game
            engine_root.walmen_time.sleep(0.1)
            switch_scene(pause)
            run=False
        elif iteria == 'next_scene':
            if dialog_mass == False:
                switch_scene(next_scene)
                run = False
            elif dialog_mass == 0:
                dialog_mass = 1
                animation_text = 1
                continue
        elif iteria == 'used':
            if dialog_mass == 3:
                dialog_mass = 1
                animation_text = 1
                continue
            else:
                pass

        if animation_text == 1 and dialog_mass == 0:

            dialog_window_object = engine_root.walmen_technology.dialog_window_animation(engine_root, standart_iteria, dialog_font, 130, 37, 400, 300, anonymous_voites[1], dialog_window, dialog_icon[0], 0.06, 'game/assets/sound/anonymous.wav')
            if dialog_window_object == True:
                animation_text = 0
                dialog_mass = 3
            elif dialog_window_object == 'pause':
                quick_scene = start_game
                engine_root.walmen_time.sleep(0.1)
                switch_scene(pause)
                run=False
        elif animation_text == 0 and dialog_mass == 0:
            engine_root.walmen_technology.self_dialog_window(engine_root, dialog_window, dialog_icon[0], dialog_font, anonymous_voites[1])
        else:
            pass

        if animation_text == 1 and dialog_mass == 1:
            engine_root.update_screen()
            dialog_window_object = engine_root.walmen_technology.dialog_window_animation(engine_root, standart_iteria, dialog_font, 130, 37, 400, 300, anonymous_voites[2], dialog_window, dialog_icon[0], 0.06, 'game/assets/sound/anonymous.wav')
            if dialog_window_object == True:
                animation_text = 0
                dialog_mass = False
                next_scene = game_preview
                continue
            elif dialog_window_object == 'pause':
                quick_scene = start_game
                engine_root.walmen_time.sleep(0.1)
                switch_scene(pause)
                run=False
        elif animation_text == 0 and dialog_mass == False:
            engine_root.walmen_technology.self_dialog_window(engine_root, dialog_window, dialog_icon[0], dialog_font, anonymous_voites[2])
        else:
            pass

        if engine_root.walmen_const.mixer.music.get_pos()/1000 >= 13.8:
            engine_root.walmen_audio.play(-1, start=36)

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)

        engine_root.update_teck_screen()

def game_preview():
    global quick_scene, next_scene

    run = True
    next_scene = None

    engine_root.update_screen()

    engine_root.walmen_audio.play(start=49)

    game_captions = engine_root.video_load(f'game/assets/video/captions.mp4', True)

    engine_root.virtual_surface = engine_root.walmen_const.Surface((game_captions.current_size))

    while run:
        iteria = standart_iteria()

        if iteria == 'end_music':
            engine_root.moding_virtual_screen(mod='default')
            switch_scene(menu)
            run = False

        game_captions.draw(engine_root.virtual_surface, (0,0))

        if engine_root.walmen_config.debug_show_fps == True:
            fps_view = engine_root.load_text(fps_font, f'FPS:{int(engine_root.fps_timer.get_fps())}', (255,255,0))
            engine_root.draw(border_fps, 0, 0)
            engine_root.draw(fps_view, 0, 0)

        engine_root.update_screen()

switch_scene(menu)
while current_scene is not None:
    current_scene()