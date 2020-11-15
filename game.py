import pygame
import os, time
import schedule
from threading import Thread
from objects.player import Player
from objects.language import Language
from database.database import Database
from database.db_config import Config
from texts.inputbox import InputBox
from texts.text import Text


x = 0
y = 30

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

def set_languages(languages):
    sec = 5
    for lang in languages:
        start_time = time.time()
        while start_time + 5 >= time.time():
            pass
        schedule.every(sec).seconds.do(lang.set_on_screen)


def start_play():
    CLOCK = pygame.time.Clock()
    FPS = 30
    score = 0
    textinput = InputBox(20, 20, 200, 50, '', True)
    textinput2 = InputBox(500, 500, 200, 50 , '', False)
    game_win = pygame.display.set_mode((1920, 1080))
    game_background = pygame.image.load("assets/backgrounds/game_background.jpg")
    player = Player("assets/player/snake.png", 700, 700)
    language1 = Language()
    language2 = Language()
    language3 = Language()
    language4 = Language()
    language5 = Language()
    current_lang_to_blit_index = 0
    time_counter = 0
    time_to_blit = 80
    images_to_blit = [[game_background, (0, 0)]]
    #languages = [language1, language2, language3, language4, language5]
    languages = [language1]
    input_boxes = [textinput, textinput2]



    """
    Hey, lately I've been working on a little game which his main idea is images falling from the sky,
    and you have to catch them with moving right and left.
    I am struggeling now to get the objects to fall from the sky each xxx seconds, without getting the code lagging
    with threads. Can anyone suggest an idea to implement this?
    """


    running = True    
    while running:
        CLOCK.tick(FPS)
        schedule.run_pending()
        current_fps = CLOCK.get_fps()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            for box in input_boxes:
                box.handle_event(event)
        

        for box in input_boxes:
            box.update()

        for image in images_to_blit:
            game_win.blit(image[0], (image[1][0], image[1][1]))
        for aaaaaaabox in input_boxes:
            box.draw(game_win)
        player.move(game_win)
        if time_counter % time_to_blit == 0:
            if languages[current_lang_to_blit_index].isOnScreen == False:
                languages[current_lang_to_blit_index].isOnScreen = True
                #if current_lang_to_blit_index == len(languages):
                #current_lang_to_blit_index = 0
            #    else:
            #         current_lang_to_blit_index += 1

        time_counter += 1
        for lang in languages:
            if lang.isOnScreen == True:
                lang.move(game_win, player)
        pygame.display.update()

if __name__ == "__main__":
    start_play()






