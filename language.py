import pygame
from random import randint, choice

class Language():
    def __init__(self):
        self.languages_images = ["assets/languages/c.png", "assets/languages/c#.png",
                            "assets/languages/c++.png", "assets/languages/elixir.png", 
                            "assets/languages/go.png", "assets/languages/java.png",
                            "assets/languages/js.png", "assets/languages/php.png", 
                            "assets/languages/ruby.png", "assets/languages/rust.png"]
        self.image = pygame.image.load(choice(self.languages_images))
        self.x = randint(0, 1100)
        self.y = 0

    def move(self, win):
        self.y += 5
        if self.y > 1080:
            del self

        else:
            win.blit(self.image , (self.x, self.y))
