import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.Frame = 0
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        
    def update(self):
        self.Frame += 0.11
        if self.Frame > 10:
            self.Frame -= 10

        Personnel = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png','8.png','9.png','10.png']
        self.image = pygame.transform.scale(pygame.image.load('resources\\'+ Personnel[int(self.Frame)]).convert_alpha(), (200,80))
class Battery(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.Frame = 0 
        self.time = True
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(topleft= (x,y))
    def update(self):
        self.Frame+=0.0009
        if self.Frame>6:
            self.time = False
        Bat = ['1b.png','2b.png','3b.png','4b.png','5b.png','6b.png']
        self.image = pygame.transform.scale(pygame.image.load('resources\\'+Bat[int(self.Frame)]).convert_alpha(),(120,70))