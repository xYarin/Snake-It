from texts.inputbox import InputBox
import pygame
import pygame.cursors
import os
from objects.button import Button
from texts.text import Text
from game import start_play
import asyncio
x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()
pygame.font.init()


def run_menu():
    """run_menu starts the menu
    """
    CLOCK = pygame.time.Clock()
    FPS = 60
    white = (255, 255, 255) 
    green = (0, 255, 0) 
    blue = (0, 0, 128) 
    logged_in = False
    started_playing = False
    # assigning values to X and Y variable 
    
    menu_win = pygame.display.set_mode((1920, 1080))
    pygame.display.set_caption("Main Menu")
    game_background = pygame.image.load("assets/backgrounds/game_background.jpg")
    # create a font object. 
    # 1st parameter is the font file 
    # which is present in pygame. 
    # 2nd parameter is size of the font 
    
    
    # create a text suface object, 
    # on which text is drawn on it. 
    text = Text(960, 400, "arial", 62) 
    text.set_text("Snake It!", underline=True, bold=True)
    play_button = Button((104, 209, 98), 850, 500, 200, 100, "Play!", 46)
    login_button = Button((38, 90, 181), 400, 650, 200, 100, "Login", 42)
    signup_button = Button((97, 44, 176), 1325, 650, 200, 100, "Sign Up", 42)
    # set the center of the rectangular object. 

    images_to_blit = [[game_background, (0, 0)]]
    #input_boxes = [textinput, textinput2]
    
    # create the display surface object 
    # of specific dimension..e(X, Y). 
    
    # set the pygame window name 
    
    
    
    running = True    
    while running:
        #text.draw(menu_win) 
        CLOCK.tick(FPS)
        current_fps = CLOCK.get_fps()
        events = pygame.event.get()
        for event in events:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.isOver(pos) and logged_in == False:
                    print("Button clicked!")
                    running = False
                    start_play()
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
                running = False
        #     for box in input_boxes:
        #         box.handle_event(event)
        

        # for box in input_boxes:
        #     box.update()

        # for image in images_to_blit:
        #     menu_win.blit(image[0], (image[1][0], image[1][1]))
        menu_win.blit(game_background, (0, 0))
        text.draw(menu_win)
        if logged_in == False:
            play_button.draw(menu_win, outline=(0, 0, 0))
        else:
            login_button.draw(menu_win, (0, 0, 0))
            signup_button.draw(menu_win, (0, 0, 0))
        # for box in input_boxes:
        #     box.draw(menu_win)
        pygame.display.update()

if __name__ == '__main__':
    run_menu()