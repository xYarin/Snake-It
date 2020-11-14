import pygame
import os
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

def start_play():
    CLOCK = pygame.time.Clock()
    FPS = 60
    textinput = InputBox(20, 20, 200, 50, '', True)
    textinput2 = InputBox(500, 500, 200, 50 , '', False)
    game_win = pygame.display.set_mode((1920, 1080))
    game_background = pygame.image.load("assets/backgrounds/game_background.jpg")
    player = Player("assets/player/snake.png", 700, 700)
    language = Language()
    
    images_to_blit = [[game_background, (0, 0)]]
    input_boxes = [textinput, textinput2]

    
    running = True    
    while running:
        CLOCK.tick(FPS)
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
        for box in input_boxes:
            box.draw(game_win)
        language.move(game_win)
        player.move(game_win)
        pygame.display.update()

#start_play()