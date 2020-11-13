import pygame
from random import randint

class Language():
    def __init__(self, image, x, y):
        self.image = pygame.image.load(image)
        self.x = randint(0, 1100)
        self.y = 0
