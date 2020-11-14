"""
Object Oriented Language Object -
Written to create languages objects to fall from the sky for Snake It game
This code is open source and free to use
"""

import pygame
from random import randint, choice

class Language:
    def __init__(self):
        """__init__ constructor function of Language class
        """
        self.languages_images = ["assets/languages/c.png", "assets/languages/c#.png",
                            "assets/languages/c++.png", "assets/languages/elixir.png", 
                            "assets/languages/go.png", "assets/languages/java.png",
                            "assets/languages/js.png", "assets/languages/php.png", 
                            "assets/languages/ruby.png", "assets/languages/rust.png"]
        self.image = pygame.image.load(choice(self.languages_images))
        self.x = randint(0, 1100)
        self.y = 0

    def move(self, win):
        """move move the language image down

        Args:
            win (pygame.display): the window to move the langauge on
        """
        self.y += 5
        if self.y > 1080:
            del self

        else:
            win.blit(self.image , (self.x, self.y))
