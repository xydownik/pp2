import pygame

pygame.init()

sc = pygame.display.set_mode((800,800))
sc.fill((255,255,255))
clock = pygame.time.Clock()

pygame.draw.circle(sc, 'red', (400,400), 25)

speed = 25
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pass
            elif event.key == pygame.K_DOWN:
                pass
            elif event.key == pygame.K_LEFT:
                pass
            elif event.key == pygame.K_RIGHT:
                pass
            
    
    pygame.display.update()
    clock.tick(20)