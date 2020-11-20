from texts.inputbox import InputBox
import pygame
from pygame import mixer
import os
from database.database import Database
from database.db_config import Config
from objects.button import Button
from texts.text import Text
from game import start_play
import asyncio
x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
pygame.font.init()

config = Config()
db = Database(config.get_host(), config.get_db_name(), config.get_collection())
logged_in = False
def run_menu(user=None, logged_in=False):
    """run_menu starts the menu
    """
    mixer.music.load("assets/sounds/menu_music.mp3")
    mixer.music.play(-1)
    print(mixer.music.set_volume(0.3684))
    CLOCK = pygame.time.Clock()
    FPS = 60
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    started_playing = False
    # assigning values to X and Y variable 
    
    menu_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Main Menu")
    game_background = pygame.image.load("assets/game/game_background.jpg")
    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    
    
    # create a text suface object, 
    # on which text is drawn on it.
    if user is not None:
        user_text = Text(100, 100, "arial", 42)
        user_text.set_text(f"Welcome Back - {user['username']}")
    title_text = Text(830, 400, "arial", 62) 
    title_text.set_text("Snake It!", underline=True, bold=True)
    play_button = Button((104, 209, 98), 850, 500, 200, 100, "Play!", 46)
    login_button = Button((38, 90, 181), 400, 650, 200, 100, "Login", 42)
    signup_button = Button((97, 44, 176), 1325, 650, 200, 100, "Sign Up", 42)
    # set the center of the rectangular object. 

    images_to_blit = [[game_background, (0, 0)]]
    #input_boxes = [textinput, textinput2]
    
    # create the display surface object 
    # of specific dimension..e(X, Y). 
    
    # set the pygame window name 
    
    
    
    menu_run = True    
    while menu_run:
        title_text.draw(menu_win) 
        CLOCK.tick(FPS)
        current_fps = CLOCK.get_fps()
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos) and logged_in:
                    menu_run = False
                    start_play(user)
                    mixer.music.fadeout(1)
                    exit()
                if login_button.isOver(pos):
                    menu_run = False
                    open_login(logged_in)
                    exit()
            if event.type == pygame.MOUSEMOTION:
                #if play_button.isOver(pos) and logged_in:
                if play_button.isOver(pos):
                    play_button.color = (92, 176, 86)
                else:
                    play_button.color = (104, 209, 98)
                if login_button.isOver(pos) and not logged_in:
                    login_button.color = (17, 63, 143)
                else:
                    login_button.color = (38, 90, 181)
                if signup_button.isOver(pos) and not logged_in:
                    signup_button.color = (76, 29, 145)
                else:
                    signup_button.color = (97, 44, 176)
            if event.type == pygame.QUIT:
                menu_run = False

       
        menu_win.blit(game_background, (0, 0))
        title_text.draw(menu_win)
        if user is not None:
            user_text.draw(menu_win)
        if logged_in == True:
            play_button.draw(menu_win, outline=(0, 0, 0))
        else:
            login_button.draw(menu_win, (0, 0, 0))
            signup_button.draw(menu_win, (0, 0, 0))

        pygame.display.update()


def open_login(logged_in):
    clock = pygame.time.Clock()
    login_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Log In")
    game_background = pygame.image.load("assets/game/game_background.jpg")
    username_text = Text(500, 375, "freesansbold", 70)
    username_text.set_text("Username: ")
    password_text = Text(500, 525, "freesansbold", 70)
    password_text.set_text("Password: ", underline=True)
    username_input = InputBox(1000, 375, 200, 50)
    password_input = InputBox(1000, 525, 200, 50, password=True)
    login_button = Button((53, 189, 103), 800, 800, 250, 150, "Login", 66)
    texts_to_draw = [username_text, password_text]
    input_boxes = [username_input, password_input]
    login_run = True
    while login_run:
        clock.tick(60)
        login_win.blit(game_background, (0, 0))
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.isOver(pos):
                    print(f"username - {username_input.text}")
                    print(f"password - {password_input.actual_text}")
                    user = db.log_in(username_input.text, password_input.actual_text)
                    if not user:
                        logged_in = False
                    else:
                        logged_in = True
                        print("Logged in is {}".format(logged_in))
                        run_menu(user, logged_in)
                        exit() 
            if event.type == pygame.MOUSEMOTION:
                if login_button.isOver(pos):
                    login_button.color = (54, 150, 90)
                else:
                    login_button.color = (53, 189, 103)
            if event.type == pygame.QUIT:
                login_run = False
            for box in input_boxes:
                box.handle_event(event)
                #exit()
        for box in input_boxes:
            box.draw(login_win)
        for text in texts_to_draw:
            text.draw(login_win)

        login_button.draw(login_win, outline=True)
        pygame.display.update()

if __name__ == '__main__':
    run_menu()