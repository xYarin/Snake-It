""" 
Object Oriented Text Object - 
This code is open source and free to use
"""

import pygame
pygame.init()
pygame.font.init()

class Text:
    def __init__(self, x, y, font, size, color=(0, 0, 0)):
        """__init__ constructor function for Text class

        Args:
            x (int): x position on screen
            y (int): y position on screen
            font (str): font of text
            size (int): size of text
            color (rgb tuple, optional): color of text. Defaults to (0, 0, 0).
        """
        self.x = x
        self.color = color
        self.y = y
        self.font = pygame.font.SysFont(font, size)

    def set_text(self, text, underline = False, bold = True):
        """set_text set text caption

        Args:
            text (str): string of text
            underline (bool, optional): sets the text underline if true. Defaults to False.
            bold (bool, optional): set the text bold if true. Defaults to True.
        """
        self.underline = underline
        self.bold = bold
        if self.underline:
            self.font.set_underline(True)
        if self.bold:
            self.font.set_bold(True)
        self.text = self.font.render(text, True, self.color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (self.x, self.y)
        
    
    def draw(self, win):
        """draw blit the text on screen

        Args:
            win (pygame.display): pygame window to display the text on
        """
        win.blit(self.text, self.text_rect)