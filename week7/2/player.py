import pygame
import os
uaqyt = pygame.time.Clock()
ander = ['Pink Floyd - Comfortably Numb.mp3', 'Pink Floyd - The Gunners Dream.mp3', 'Oasis_-_Married_With_Children.mp3']
pppn = ['pause.png', 'play.jpg', 'next.png', 'back.png']
photos = ['thewall.jpg', 'finalcut.jpg', 'def_maybe.jpg']
pygame.mixer.init()
screen = pygame.display.set_mode((1310, 900))
screen.fill((255,255,255))
done = False
i = 0
def start(i):
    screen.blit(pygame.transform.scale(pygame.image.load(photos[i]),(500,500)), (395, 5))
    pygame.mixer.music.load(ander[i])
    pygame.mixer.music.play()
start(i)

screen.blit(pygame.transform.scale(pygame.image.load(pppn[0]), (300,300)), (475, 525))
screen.blit(pygame.transform.scale(pygame.image.load(pppn[3]),(300,300)), (50, 525))
screen.blit(pygame.transform.scale(pygame.image.load(pppn[2]),(300,300)), (900, 525))
paused = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        mouse_pos = pygame.mouse.get_pos()
        left = pygame.mouse.get_pressed()
        
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if(paused == False):
                pygame.mixer.music.pause()
                paused = True
                screen.blit(pygame.transform.scale(pygame.image.load(pppn[1]),(300,300)), (475, 525))
            else:
                pygame.mixer.music.unpause()
                paused = False 
                screen.blit(pygame.transform.scale(pygame.image.load(pppn[0]),(300,300)), (475, 525))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if i==2: i=0
            else: i+=1
            screen.blit(pygame.transform.scale(pygame.image.load(photos[i]),(500,500)), (395, 5))
            start(i)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if i==0: i=2
            else: i-=1
            screen.blit(pygame.transform.scale(pygame.image.load(photos[i]),(500,500)), (395, 5))
            start(i)
        if left:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 475 <=mouse_pos[0]<= 835 and 525 <= mouse_pos[1]<= 885:
                    if(paused == False):
                        pygame.mixer.music.pause()
                        paused = True
                        screen.blit(pygame.image.load(pppn[1]), (475, 525))
                    else:
                        pygame.mixer.music.unpause()
                        paused = False 
                        screen.blit(pygame.image.load(pppn[0]), (475, 525))
                if 50 <= mouse_pos[0] <= 410 and 525 <= mouse_pos[1] <= 885:
                    if i==0: i=2
                    else: i-=1
                    screen.blit(pygame.transform.scale(pygame.image.load(photos[i]),(500,500)), (395, 5))
                    start(i)
                if 900 <= mouse_pos[0] <= 1260 and 525 <= mouse_pos[1] <= 885:
                    if i==2: i=0
                    else: i+=1
                    screen.blit(pygame.transform.scale(pygame.image.load(photos[i]),(500,500)), (395, 5))
                    start(i)
    pygame.display.flip()
    uaqyt.tick(55)
pygame.quit()
