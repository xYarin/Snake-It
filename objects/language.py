"""
Object Oriented Language Object -
Written to create languages objects to fall from the sky for Snake It game
This code is open source and free to use
"""

import pygame
from math import sqrt
from random import randint, choice
from time import sleep

class Language:
    def __init__(self):
        """__init__ constructor function of Language class"""
        self.languages_images = ["assets/languages/c.png", "assets/languages/c#.png",
                            "assets/languages/c++.png", "assets/languages/elixir.png", 
                            "assets/languages/go.png", "assets/languages/java.png",
                            "assets/languages/js.png", "assets/languages/php.png", 
                            "assets/languages/ruby.png", "assets/languages/rust.png"]
        self.image = pygame.image.load(choice(self.languages_images))
        self.x = randint(0, 1700)
        self.y = 0
        self.isOnScreen = False

    def move(self, win, player):
        """move move the language image down

        Args:
            win (pygame.display): the window to move the langauge on
        """
        self.y += 20
        if (self.y > 1080) or (self.x in range(player.x - 120, player.x + 100) and self.y in range (player.y - 30, player.y + 500)):
            self.isOnScreen = False
            self.y = 0
            self.x = randint(0, 1700)
            self.image = pygame.image.load(choice(self.languages_images))

        self.draw(win)
        pygame.display.update()

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
    
    def set_on_screen(self):
        self.isOnScreen = True