from game.engine import global_var

from game.engine import config

engine_root = global_var.engine_root
engine_root.display_mod(mod=0)
engine_root.draw_engine_logo()

engine_root.walmen_time.sleep(2)

engine_root.display_reinit()

run = False

current_scene = None
effect_current_scene = None

fps_font = engine_root.load_font('game/startassets/font/determination.otf', 40)
border_fps = engine_root.load_image('game/startassets/images/black.webp', 150, 40)

def switch_scene(scene):
    global current_scene
    current_scene = scene

def logo():
    global effect_current_scene
    run = True

    intro_number = len(engine_root.walmen_os.listdir('game/startassets/intro'))
    
    for intro in engine_root.walmen_os.listdir('game/startassets/intro'):

        engine_root.walmen_time.sleep(1)

        video_logo = engine_root.video_load(f'game/startassets/intro/{intro}', False)

        video_logo.set_volume(50.0)

        engine_root.moding_virtual_screen(video_logo.current_size)

        while run:
            for event in engine_root.walmen_const.event.get():
                if event.type == engine_root.walmen_const.QUIT:
                    engine_root.exit()
                elif event.type == engine_root.walmen_const.VIDEORESIZE:
                    engine_root.set_resize_window(event.size)

            video_logo_pos = round(video_logo.get_pos(), 1)
            if video_logo_pos >= round(video_logo.duration, 1):
                break
            else:
                video_logo.draw(engine_root.virtual_surface, (0,0), force_draw=False)  
            
            if engine_root.walmen_config.debug_show_fps == True:
                fps_view = engine_root.load_text(fps_font, f'FPS: {int(engine_root.fps_timer.get_fps())}', (255,255,0))
                engine_root.draw(border_fps, 0, 0)
                engine_root.draw(fps_view, 0, 0)

            engine_root.update_teck_screen()
        intro_number -=1
        if intro_number != 0:
            continue
        else:
            from game.assets import script

switch_scene(logo)
while current_scene is not None:
    current_scene()
