import pygame
from pygame import mixer
import os, time
from objects.player import Player, is_collided
from objects.language import Language
from objects.heart import Heart
from database.database import Database
from database.db_config import Config
from texts.inputbox import InputBox
from texts.text import Text

config = Config()
db = Database(config.get_host(), config.get_db_name(), config.get_collection())
x = 0
y = 30


os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
pygame.init()




def start_play(user):
    """start_play starts the game screen
    """
    mixer.music.load("assets/sounds/gameplay_music.mp3")
    print(mixer.music.get_busy())
    if not mixer.music.get_busy():
        #mixer.music.play(-1)
        pass
    CLOCK = pygame.time.Clock()
    FPS = 60
    textinput = InputBox(20, 20, 200, 50, '', True)
    textinput2 = InputBox(500, 500, 200, 50 , '', False)
    game_win = pygame.display.set_mode((1920, 1080))
    game_background = pygame.image.load("assets/game/game_background.jpg")   
    player = Player("assets/player/snake.png", 700, 700)
    language1 = Language()
    language2 = Language()
    language3 = Language()
    language4 = Language()
    language5 = Language()
    current_lang_to_blit_index = 0
    time_counter = 3
    first_image = True
    time_to_blit = 80
    failed = False
    images_to_blit = [[game_background, (0, 0)]]
    languages = [language1, language2, language3, language4, language5]
    input_boxes = [textinput, textinput2]
    best_score_text = Text(800, 200, "freesans", 40)
    score_text = Text(30, 25, "freesans", 30)
    score_text.set_text("Score: ")
    
        

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
        


        for image in images_to_blit:
            game_win.blit(image[0], (image[1][0], image[1][1]))

        player.move(game_win)
        if time_counter % time_to_blit == 0:
            if first_image:
                first_image = False
                time_counter = 0
            if languages[current_lang_to_blit_index].isOnScreen == False:
                languages[current_lang_to_blit_index].isOnScreen = True
                if current_lang_to_blit_index == len(languages) - 1:
                    current_lang_to_blit_index = 0
                    # for lang in languages:
                    #     lang.set_on_screen()
                else:
                    current_lang_to_blit_index += 1

        time_counter += 1
        for lang in languages:
            if lang.isOnScreen:
                if is_collided(player.x + 100, player.y, lang.x, lang.y):
                    lang.reset_place()
                    player.update_score()
                if not failed:
                    if lang.move(game_win, player, languages) == False:
                        failed = True
                        score_text.replace(550, 500, 160)
                        if db.update_bestscore(user, player.score):
                            best_score_text.set_text("new record!")
                        for lang in languages:
                            lang.isOnScreen = False
        
        for heart in player.hearts:
            heart.draw(game_win)
        
        best_score_text.draw(game_win)
        score_text.set_text(f"Score: {player.score}")
        score_text.draw(game_win)
        pygame.display.update()

if __name__ == "__main__":
    start_play(user="yarin")





