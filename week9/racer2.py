import pygame, sys

from pygame.locals import *
import time,random
 
pygame.init()

FPS = 60
clock = pygame.time.Clock()
 
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 600
HEIGHT = 600
speed = 5
score = 0
coins = 0


class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-10), 0)  
   
      def move(self):
        global score
        self.rect.move_ip(0,speed)
        if (self.rect.top > HEIGHT):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 10), 0)
 

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  
class Coin(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 560), random.randint(-100, 0))
        self.weight = 1
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        global coins
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 560), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            coins += self.weight
            self.rect.top = 0
            self.rect.center = (random.randint(40,560), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,560), 0)

        self.rect.move_ip(0, speed)
        
        
class Coin2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("coin.png"), (84,84))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 560), random.randint(-100, 0))
        self.weight = 3
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        global coins
        if self.rect.top > HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 560), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            coins += self.weight
            self.rect.top = 0
            self.rect.center = (random.randint(40,560), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,560), 0)

        self.rect.move_ip(0, speed)
 

font = pygame.font.SysFont("Verdana", 60)
font2 = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, RED)
scoring = font.render("Score",True,RED)

bg = pygame.image.load("road.png")
 
sc= pygame.display.set_mode((WIDTH,HEIGHT))
sc.fill(WHITE)
pygame.display.set_caption("Game")


    
P1 = Player()
E1 = Enemy()

player = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player.add(P1)
coins_group = pygame.sprite.Group()
sprites = pygame.sprite.Group()

enemies.add(E1)
sprites.add(P1)
sprites.add(E1)
 
velocity = pygame.USEREVENT + 1
pygame.time.set_timer(velocity, 1000)

for i in range(2):
    C1 = Coin()
    coins_group.add(C1)
    sprites.add(C1)
    
for i in range(1):
    C2 = Coin2()
    coins_group.add(C2)
    sprites.add(C2)
coins2 = 10
while True:
        
    for event in pygame.event.get():
        if event.type == velocity:
            if coins >=coins2:          # if current num of coins exceed coins2 = 10 then speed increases to 1.5
                speed += 1.5
                coins2+=10          # and the next time speed increases when coins will exceed 20
                   
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    sc.blit(bg, (0,0))
    scores = font2.render(str(score), True, WHITE)
    coins_view = font2.render(str(coins),True,WHITE)
    sc.blit(scores, (10,10))
    sc.blit(coins_view,(535,10))
    
    for i in sprites:
        sc.blit(i.image, i.rect)
        i.move()
 
    if pygame.sprite.spritecollideany(P1, enemies):
        
          pygame.mixer.Sound('crash.wav').play()
          time.sleep(0.5)
          
          sc.fill(BLACK)
          sc.blit(game_over, (100,250))
          
          pygame.display.update()
          for i in sprites:
                i.kill() 
          time.sleep(3)
          pygame.quit()
          sys.exit()    
              
    pygame.display.update()
    clock.tick(FPS)