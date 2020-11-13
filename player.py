import pygame


class Player():
    def __init__(self, image, x, y):    
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.vel = 20
        self.isRight = False
    def move(self, win):
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


#self.image = pygame.transform.flip(self.image, True, False)
            
        
