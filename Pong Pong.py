'''
Code Written By Stickman

a pygame-ce 2.5.8 python 3.14.4 game

All the descriptions are written in code
And I also added an example for some functions like screen.blit or pygamedraw.rect to help for understanding
arguments shall given to these functions (It will help :=)

github page= https://github.com/manstick

THE SOURCE CODE OF THE GAME

'''
#imports
import sys
import subprocess

try:
    import pygame
    print("pygame-ce is already built in starting program...")
except ImportError:
    print("pygame-ce couldn't founded installing..")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygame-ce"])
        import pygame_ce
        print("pygame-ce successfully installed")
    except Exception as e:
        print(f"Something Bad Happened While Downloading {e}")
        sys.exit(1)
    '''If your python doesn't have a pygame library it downloads it '''

import numpy as np
import time
import sys
import random
import pygame

# startups
pygame.init()

player1_score = 0
player2_score = 0
ai_score = 0

paused = False
control = False
debug = False
game_active = True
game_over = False
running = False
ai = False
in_difficulty_menu = False
v_pressed = False


fps = 120
fps_stat=0
clock = pygame.time.Clock()
last_time_activate = pygame.time.get_ticks()

# screen
'''Screen resolution is a value that can be changed'''

screen_w, screen_h = 800,640
screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption("Pong Pong")

#click
p_click = 0
click_debug = 0
click = 0
v_click = False
click_back = 0
#icon

img = pygame.image.load('icon.jpg')
pygame.display.set_icon(img)

#pi

pi = 3.141592653589793238462643383
'''pi for numpy dont change it '''

# fonts

'''fonts (('Type of the font if you want the normal font leave it empty'), size of the font here)'''
verysmallfont = pygame.font.SysFont('',25)
smallfont = pygame.font.SysFont('', 35)
bigfont = pygame.font.SysFont('', 70)
numberfont = pygame.font.SysFont('', 60)

# difficulty
'''For solo mode'''
difficulty_delay = 500
ai_target_y = 250

# players Setup
player1_x, player1_y = 45, screen_h // 2 + 80
player1_width, player1_height = 15, 80
player1_speed = 5

player2_x, player2_y = screen_w - 55, screen_h // 2 + 80
player2_width, player2_height = 15, 80
player2_speed = 5
ai_speed = 4

# ball
x, y = screen_w // 2, screen_h //2
radius = 10
speed_x = 2.5
speed_y = 2.5

saved_speed_x = 0
saved_speed_y = 0
# colors

'''colour= (r,g,b) red-green-blue values'''

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (128, 128, 128)

# texts

'''('Text Here'), condition (True or False) , color '''

text_start = smallfont.render('Two Players', True, white)
text_quit = smallfont.render('Quit', True, white)
text_ping_pong = bigfont.render('Pong Pong', True, white)
text_stickman = smallfont.render('Made By Stickman', True, white)
text_ai = smallfont.render('One Player', True, white)

text_easy = smallfont.render('Easy', True, white)
text_normal = smallfont.render('Normal', True, white)
text_hard = smallfont.render('Hard', True, white)
text_control = smallfont.render('Control', True,white)
text_fps = smallfont.render(f'Fps = {fps}',True, white)
text_volume_on = smallfont.render('Volume On', True,white)
text_volume_off = smallfont.render('Volume Off', True,white)
text_paused = smallfont.render('Paused', True, white)
pause_symbol = smallfont.render('| |',True,white)
# buttons

'''(x,y cordinates --- width,height of the cubes)'''

start_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 - 50, 140, 40)
ai_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 + 10, 140, 40)
quit_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 + 70, 140, 40)

easy_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 - 50, 140, 40)
normal_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 + 10, 140, 40)
hard_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h // 2 + 70, 140, 40)

fps_btn_rect = pygame.Rect(screen_w// 2 - 350, screen_h // 2 + 250, 120, 40)

control_btn_rect = pygame.Rect(screen_w //2 + 250, screen_h // 2 - 20, 100, 40)
pause_btn_rect = pygame.Rect(screen_w // 2 -20 , screen_h + 20, 20,20 )

wide_back_btn = 140
back_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h - 70, wide_back_btn, 40)
text_back = smallfont.render('Back', True, white)

winner_text_str = ""

#Functions
def reset_game():
    '''120 fps mode'''
    global ai_score, player1_score, player2_score, player1_y, player2_y
    global x, y, speed_x, speed_y, player1_height, player2_height, fps, paused,debug,fps_mode
    debug = False
    paused = False
    fps = 120
    fps_mode = 120
    ai_score = 0
    player1_score = 0
    player2_score = 0
    player1_y = 250
    player2_y = 250
    x = screen_w / 2
    y = screen_h / 2
    speed_x = 2.5
    speed_y = 2.5
    player1_height = 80
    player2_height = 80

def reset_game_60():
    '''60 fps mode'''
    global ai_score, player1_score, player2_score, player1_y, player2_y
    global x, y, speed_x, speed_y, player1_height, player2_height, fps, paused,debug,fps_mode
    debug = False
    paused = False
    fps = 60
    fps_mode = 60
    #saver value
    ai_score = 0
    player1_score = 0
    player2_score = 0
    player1_y = 250
    player2_y = 250
    x = screen_w / 2
    y = screen_h / 2
    speed_x = 5
    speed_y = 5
    player1_height = 80
    player2_height = 80
    
#Button pos functions
def changing_back_btn():
    global text_back, wide_back_btn, back_btn_rect
    text_back = smallfont.render('Return to Main Menu', True, white)
    wide_back_btn = 350
    back_btn_rect = pygame.Rect(screen_w // 2 -175, screen_h - 70, wide_back_btn, 40)
    
def back_btn_org():
    global text_back, wide_back_btn, back_btn_rect
    wide_back_btn = 140
    back_btn_rect = pygame.Rect(screen_w // 2 - 70, screen_h - 70, wide_back_btn, 40)
    text_back = smallfont.render('Back', True, white)
    
def make_click_sound():
    """
    These sounds are just got created in real time by frequences
    but unless you are a mathemathic prof dont mess with
    ai did those sounds
    
    """
    sample_rate = 44100
    duration = 0.05  
    t = np.linspace(0, duration, int(sample_rate * duration), False)


    wave = np.sin(2 * np.pi * 800 * t) * np.exp(-t * 80)
    audio = (wave * 32767).astype(np.int16)

    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)


def make_bounce_sound():
    """Bouncing sound"""
    sample_rate = 44100
    duration = 0.15 
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    freq = 300 * np.exp(-t * 15) + 100
    wave = np.sin(2 * np.pi * freq * t) * np.exp(-t * 12)
    audio = (wave * 32780).astype(np.int16)

    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()


click_sound = make_click_sound()
bounce_sound = make_bounce_sound()

'''
to use it 
click_sound.play()
bounce_sound.play()
'''

# loops
reset_game()
while game_active:
    clock.tick(fps)
    mouse_pos = pygame.mouse.get_pos()
    # main menu
    if not running and not game_over and not in_difficulty_menu and not control:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if start_btn_rect.collidepoint(mouse_pos):
                    running = True
                    ai = False
                    control = False
                    click_sound.play()
                    if fps == 60:
                        reset_game_60()
                    elif fps == 120:
                        reset_game()
                if control_btn_rect.collidepoint(mouse_pos):
                    control = True
                    click_sound.play()
                if ai_btn_rect.collidepoint(mouse_pos):
                    in_difficulty_menu = True
                    click_sound.play()
                if quit_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    game_active = False
                if fps_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    click+=1
                    if not click % 2 == 0:
                        fps_stat=1
                        fps=60
                        speed_x = 5
                        speed_y = 5
                        player1_speed = 10
                        player2_speed = 10
                        ai_speed *=2
                    elif click % 2 ==0:
                        fps_stat=0
                        fps=120
                        speed_x= 2.5
                        speed_y = 2.5
                        player1_speed = 5
                        player2_speed = 5
                        ai_speed = 0
                        '''changing the speed of ai is only neccesary at 60 fps and the value is going to
                        change at dificulty screen'''
                        
                    text_fps = smallfont.render(f'Fps = {fps}',True, white)
                    
        screen.fill((30, 30, 30))
        '''r,g,b again'''
        
        '''field, color, target_button, border_radius'''
        pygame.draw.rect(screen, gray, start_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, ai_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, quit_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, fps_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, control_btn_rect, border_radius=8)
        
        '''text, text.get_rect (center=target_button.center)'''
        screen.blit(text_start, text_start.get_rect(center=start_btn_rect.center))
        screen.blit(text_ai, text_ai.get_rect(center=ai_btn_rect.center))
        screen.blit(text_quit, text_quit.get_rect(center=quit_btn_rect.center))
        screen.blit(text_ping_pong, text_ping_pong.get_rect(center=(screen_w // 2, 80)))
        screen.blit(text_stickman, text_stickman.get_rect(center=(screen_w // 2, 600)))
        screen.blit(text_fps, text_fps.get_rect(center=(screen_w // 2 - 290, screen_h // 2 + 270)))
        screen.blit(text_control, text_control.get_rect(center = (screen_w //2 + 300, screen_h // 2)))
    
    # control menu
    elif control:
        # buttons for this menu

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    control = False

        screen.fill((30, 30, 30))
        
        # title
        title_ctrl = bigfont.render("Control", True, white)
        screen.blit(title_ctrl, title_ctrl.get_rect(center=(screen_w // 2, 60)))

        # player 1 (red one)
        pygame.draw.rect(screen, red, (100, 160, 15, 60))
        p1_title = smallfont.render("Player 1 (Red):", True, red)
        p1_up = verysmallfont.render("W -> Move Up", True, white)
        p1_down = verysmallfont.render("S -> Move Down", True, white)
        screen.blit(p1_title, (130, 160))
        screen.blit(p1_up, (130, 195))
        screen.blit(p1_down, (130, 220))

        # player 2 / ai (blue oen)
        pygame.draw.rect(screen, blue, (480, 160, 15, 60))
        p2_title = smallfont.render("Player 2 / AI (Blue):", True, blue)
        p2_up = verysmallfont.render("UP Arrow -> Move Up", True, white)
        p2_down = verysmallfont.render("DOWN Arrow -> Move Down", True, white)
        screen.blit(p2_title, (510, 160))
        screen.blit(p2_up, (510, 195))
        screen.blit(p2_down, (510, 220))

        # keys
        gen_title = smallfont.render("Keybinds:", True, gray)
        p_key = verysmallfont.render("P -> pause / unpause", True, white)
        k_key = verysmallfont.render("K -> return to main menu", True, white)
        v_key = verysmallfont.render("V -> mute / sound on", True, white)
        d_key = verysmallfont.render("D -> debug mode / cheats", True, white)

        screen.blit(gen_title, (screen_w // 2 - 100, 300))
        screen.blit(p_key, (screen_w // 2 - 120, 340))
        screen.blit(k_key, (screen_w // 2 - 120, 370))
        screen.blit(v_key, (screen_w // 2 - 120, 400))
        screen.blit(d_key, (screen_w // 2 - 120, 430))


        # back buton
        pygame.draw.rect(screen, gray, back_btn_rect, border_radius=8)
        screen.blit(text_back, text_back.get_rect(center=back_btn_rect.center))
        
    # difficulty for solo mode
        '''
        Difficulty system works with delaying time, harder = less delay, easier = more delay
        the pos of the blue is trying to equalize his y pos with balls y pos but delay prevents it
        '''
    elif in_difficulty_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if easy_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    paused = False
                    difficulty_delay = 500
                    ai_speed = 3
                    if fps == 60:
                        reset_game_60()
                    elif fps == 120:
                        reset_game()
                        
                elif normal_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    paused = False
                    difficulty_delay = 250
                    ai_speed = 4.5
                    if fps == 60:
                        reset_game_60()
                    elif fps == 120:
                        reset_game()
                        
                elif hard_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    paused = False
                    difficulty_delay = 150
                    ai_speed = 6
                    if fps == 60:
                        reset_game_60()
                    elif fps == 120:
                        reset_game()

                if easy_btn_rect.collidepoint(mouse_pos) or normal_btn_rect.collidepoint(mouse_pos) or hard_btn_rect.collidepoint(mouse_pos):
                    ai = True
                    running = True
                    in_difficulty_menu = False

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, gray, easy_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, normal_btn_rect, border_radius=8)
        pygame.draw.rect(screen, gray, hard_btn_rect, border_radius=8)

        screen.blit(text_easy, text_easy.get_rect(center=easy_btn_rect.center))
        screen.blit(text_normal, text_normal.get_rect(center=normal_btn_rect.center))
        screen.blit(text_hard, text_hard.get_rect(center=hard_btn_rect.center))

    # game over screen
    elif game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
            if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                game_over = False
                running = False
                ai = False
                if fps==60:
                    reset_game_60()
                else:
                    reset_game()
                    
        screen.fill((20, 20, 20))
        text_winner = bigfont.render(winner_text_str, True, white)
        text_restart_info = smallfont.render('Click to go back to the main menu', True, gray)

        screen.blit(text_winner, text_winner.get_rect(center=(screen_w // 2, screen_h // 2 - 30)))
        screen.blit(text_restart_info, text_restart_info.get_rect(center=(screen_w // 2, screen_h // 2 + 50)))

    # game
    else:
        
        time_now = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_active = False
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                   debug = not debug
                if event.key == pygame.K_p:
                    fps=0
                    debug = False
                    if fps_mode == 120:
                        fps = 120
                    elif fps_mode == 60:
                        fps=60
                    paused = not paused
                    saved_speed_x = speed_x
                    saved_speed_y = speed_y
                if back_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    control = False
                    
        keys = pygame.key.get_pressed()
        #pause screen
        if paused:
            changing_back_btn()
            screen.blit(text_paused, text_paused.get_rect(center=(screen_w // 2, screen_h // 2)))
            pygame.display.flip()
            pygame.draw.rect(screen, gray, back_btn_rect, border_radius=8)
            screen.blit(text_back, text_back.get_rect(center=back_btn_rect.center))
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if back_btn_rect.collidepoint(mouse_pos):
                    click_sound.play()
                    control = False 
                    game = False
                    pause = False
                    game_active = True
                    running=False
                    ai=False
                    back_btn_org()
            elif click_back != 1:
                continue
        
        if keys[pygame.K_w]:
            player1_y -= player1_speed
        if keys[pygame.K_s]:
            player1_y += player1_speed
        # ai movement
        if ai:
            if time_now - last_time_activate >= difficulty_delay:
                ai_target_y = y - (player2_height / 2)
                last_time_activate = time_now

            if abs(player2_y - ai_target_y) > 3:
                if player2_y < ai_target_y:
                    player2_y += ai_speed
                elif player2_y > ai_target_y:
                    player2_y -= ai_speed
        else:
            if keys[pygame.K_UP]:
                player2_y -= player2_speed
            if keys[pygame.K_DOWN]:
                player2_y += player2_speed
                

        
            
        # min max y cheking
        player1_y = max(0, min(screen_h - player1_height, player1_y))
        player2_y = max(0, min(screen_h - player2_height, player2_y))

        # ball
        x += speed_x
        y += speed_y

        if y - radius <= 0 or y + radius >= screen_h:
            speed_y *= -1          

        # scoring system
        if x >= screen_w - 2:
            player1_score += 1
            x, y = screen_w / 2, screen_h / 2
            if fps==60:
                speed_x = -5
                speed_y = 5
                pygame.time.delay(200)
                '''I added these code because when someone gets a score the ball was restarting the game
                with 120 fps modes speed and this lookstoo slow for 60 fps'''
            else:
                speed_x = -2.5
                speed_y = 2.5
                pygame.time.delay(200)

        if x <= 2:
            if ai:
                ai_score += 1
                x, y = screen_w / 2, screen_h / 2
                if fps==60:
                    speed_x = 5
                    speed_y = 5
                    pygame.time.delay(200)
                else:   
                    speed_x = 2.5
                    speed_y = 2.5
                    pygame.time.delay(200)
            else:
                player2_score += 1
                x, y = screen_w / 2, screen_h / 2
                if fps==60:
                    speed_x = 5
                    speed_y = 5
                    pygame.time.delay(200)
                else:   
                    speed_x = 2.5
                    speed_y = 2.5
                    pygame.time.delay(200)

        # drawing charachters
        screen.fill((30, 30, 30))
        p2_score_display = ai_score if ai else player2_score
        text_score1 = numberfont.render(f'{player1_score}', True, red)
        text_score2 = numberfont.render(f'{p2_score_display}', True, blue)
        
        screen.blit(pause_symbol, pause_symbol.get_rect(center=(screen_w// 2 -10,10)))
        screen.blit(text_score1, text_score1.get_rect(center=(screen_w // 4, 40)))
        screen.blit(text_score2, text_score2.get_rect(center=(3 * screen_w // 4, 40)))
        
        '''pygame.draw.(shape) (target field, color, (x,y, width , height or radius for ball))'''
        
        player_1 = pygame.draw.rect(screen, red, (player1_x, player1_y, player1_width, player1_height))
        player_2 = pygame.draw.rect(screen, blue, (player2_x, player2_y, player2_width, player2_height))
        ball = pygame.draw.circle(screen, white, (int(x), int(y)), radius)

        # ball collisions
        if ball.colliderect(player_1):
            bounce_sound.play()
            speed_x = abs(speed_x) + 0.3
            x = player_1.right + radius
        if ball.colliderect(player_2):
            bounce_sound.play()
            speed_x = -(abs(speed_x) + 0.3)
            x = player_2.left - radius

        #ends
        if player1_score == 10:
            if ai:
                winner_text_str = "You Won!"
            else:
                winner_text_str = "Player 1 Won!"
            game_over = True
            running = False
            player1_score = 0
            ai_score = 0
            player2_score = 0
            
        elif (ai and ai_score == 10) or (not ai and player2_score == 10):
            winner_text_str = "AI Won!" if ai else "Player 2 Won!"
            game_over = True
            running = False
            player1_score = 0
            ai_score = 0
            player2_score = 0
            
        # debug screen and cheats
        if debug:
            text_activate_d= verysmallfont.render("Debug mode activated close 'd' on your keyboard to close",True,white)
            
            '''To add a value first enter the value name and then write the value into {} e.g == Example = {example}'''
            
            text_debug = verysmallfont.render(f'Fps = {fps}, Ball Speed={speed_y},{speed_x} , Player 1-2 speed={player1_speed},{player2_speed},paused={paused},ss={saved_speed_y,saved_speed_x}',True, white)
            click_debug+=1
            if not click_debug % 2==0:
                pass
            else:
                screen.blit(text_debug, (10, 10))
                screen.blit(text_activate_d, (30, 620))
                
            '''Added these debug to not use print because it slowdown the code.
            Cheats are for testing for using cheats first press d enter
            debug mode and then you can use the cheats
            
            Cheats are only for red player I was too lazy to codde the other cheats to blue and it is not necesarry
            
            n = Adds a + to player 1 score
            m = makes the ball faster (too much fast)
            t = makes the y value same as ball value so that means the player 1 follows the ball by 
            h = increasing players height to 640 (max size of the screen height)
            f = dont (random fps value )
            
            Non Debug Keys
            
            v = Sound on off
            k = return main menu
            '''
            
            if keys[pygame.K_n]:
                player1_score+=1
                pygame.time.delay(200)
            if keys[pygame.K_m]:
                if speed_x < 0:
                    speed_x -= 1
                else:
                    speed_x += 1
            if keys[pygame.K_t]:
                player1_y = y - 50
            if keys[pygame.K_h]:
                player1_height = screen_h
                player2_height = screen_h
            if keys[pygame.K_f]:
                fps =random.randint(1,120)
            if keys[pygame.K_l]:
                fps = 10000000000000

        '''Non Debug Keys'''
        if keys[pygame.K_k]:
            running=False
            ai=False
            game_active=True
            if fps == 60:
                reset_game_60()
            else:
                reset_game()
        if keys[pygame.K_v]:
            if not v_pressed:
                '''volume off'''
                v_click = True
                volume = 0.0 if v_click else 1.0
                click_sound.set_volume(volume)
                bounce_sound.set_volume(volume)
                screen.blit(text_volume_off, text_volume_off.get_rect(center=(screen_w // 2, screen_h // 2)))
                v_pressed = True  
            else:
                '''volume on'''
                v_click = False
                volume = 1.0
                click_sound.set_volume(volume)
                bounce_sound.set_volume(volume)
                screen.blit(text_volume_on, text_volume_on.get_rect(center=(screen_w // 2, screen_h // 2)))
                v_pressed = False
            pygame.display.flip()
            pygame.time.delay(200)
                    
    pygame.display.flip()
pygame.quit()
sys.exit()


#Code end

'''

⠀⠀⠀⠀⠀⢀⡠....⠤⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠊⠁⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀
⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⠀⠀⠀
⠀⠀⡇⢠⣦⡄⠀⠀⠀⠀⠀⠀⣠⣤⠀⡇⠀⠀
⠀⠀⢡⠀⠉⠀⠘⠢⠀⠤⠂⠀⠈⠉⢰⠀⠀⠀
⠀⠀⠀⠣⡄⠀⠀⠀⠀⠀⠀⠀⢀⡐⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠁⠒⠤⣤⡤⠔⠂⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠊⢸⠘⢦⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠔⠁⠀⢸⠀⠀⠙⢄⡀⠀⠀⠀⠀
⠀⠀⠀⡠⠋⠀⠀⠀⢸⠀⠀⠀⠀⠑⢄⡀⠀⠀
⠀⢀⠎⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠑⢄⠀
⠐⠁⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠑
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀
         ⢸⠀         
         |
         |         
         |           
         ⢸⠀⠀          
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡼⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠜⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠈⢄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠊⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀⠀
⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀
⠀⠀⡰⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀'''