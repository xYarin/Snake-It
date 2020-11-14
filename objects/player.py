"""
Object Oriented Player Object -
Written to implement the player in Snake It game
This code is open source and free to use
"""

import pygame


class Player:
    def __init__(self, image, x, y):    
        """__init__ constructor function for Player class

        Args:
            image (str.png): the player image to display on screen
            x (int): starting x position of player
            y (int): starting y position of player
        """
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vel = 20
        self.isRight = False

    def move(self, win):
        """move handles movement for player object

        Args:
            win (pygame.display): the window to move the player
        """
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (self.x < 1920 - 200):
            if not self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
            self.x += self.vel
            self.isRight = True

        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (self.x > 0):
            if self.isRight:
                self.image = pygame.transform.flip(self.image, True, False)
            self.x -= self.vel
            self.isRight = False  

        win.blit(self.image,(self.x, self.y))


            
        
