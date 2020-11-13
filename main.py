import pygame
import os
from player import Player
from language import Language
from database import Database
from db_config import Config
config = Config()

db = Database(config.get_host(), config.get_db_name(), config.get_collection())
collection = db.collection

x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()

def start_play():
    CLOCK = pygame.time.Clock()
    FPS = 60
    game_win = pygame.display.set_mode((1920, 1080))
    game_background = pygame.image.load("assets/backgrounds/game_background.jpg")
    player = Player("assets/player/snake.png", 700, 700)
    language = Language()
    
    images_to_blit = [[game_background, (0, 0)]]

    
    running = True    
    while running:
        CLOCK.tick(FPS)
        current_fps = CLOCK.get_fps()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        

        for image in images_to_blit:
            game_win.blit(image[0], (image[1][0], image[1][1]))
           
        language.move(game_win)
        player.move(game_win)
        pygame.display.update()

start_play()