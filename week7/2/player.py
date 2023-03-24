import pygame
import os
clock = pygame.time.Clock()
music = ['Pink Floyd - Comfortably Numb.mp3', 'Pink Floyd - The Gunners Dream.mp3', 'Oasis_-_Married_With_Children.mp3']
buttons = ['pause.png', 'play.jpg', 'next.png', 'back.png']
covers = ['thewall.jpg', 'finalcut.jpg', 'def_maybe.jpg']
pygame.mixer.init()
sc = pygame.display.set_mode((1310, 900))
sc.fill((255,255,255))
done = False
i = 0
def start(i):
    sc.blit(pygame.transform.scale(pygame.image.load(covers[i]),(500,500)), (395, 5))
    pygame.mixer.music.load(music[i])
    pygame.mixer.music.play()
start(i)

sc.blit(pygame.transform.scale(pygame.image.load(buttons[0]), (300,300)), (475, 525))
sc.blit(pygame.transform.scale(pygame.image.load(buttons[3]),(300,300)), (50, 525))
sc.blit(pygame.transform.scale(pygame.image.load(buttons[2]),(300,300)), (900, 525))
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
                sc.blit(pygame.transform.scale(pygame.image.load(buttons[1]),(300,300)), (475, 525))
            else:
                pygame.mixer.music.unpause()
                paused = False 
                sc.blit(pygame.transform.scale(pygame.image.load(buttons[0]),(300,300)), (475, 525))
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if i==2: i=0
            else: i+=1
            sc.blit(pygame.transform.scale(pygame.image.load(covers[i]),(500,500)), (395, 5))
            start(i)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if i==0: i=2
            else: i-=1
            sc.blit(pygame.transform.scale(pygame.image.load(covers[i]),(500,500)), (395, 5))
            start(i)
        if left:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if 475 <=mouse_pos[0]<= 835 and 525 <= mouse_pos[1]<= 885:
                    if(paused == False):
                        pygame.mixer.music.pause()
                        paused = True
                        sc.blit(pygame.image.load(buttons[1]), (475, 525))
                    else:
                        pygame.mixer.music.unpause()
                        paused = False 
                        sc.blit(pygame.image.load(buttons[0]), (475, 525))
                if 50 <= mouse_pos[0] <= 410 and 525 <= mouse_pos[1] <= 885:
                    if i==0: i=2
                    else: i-=1
                    sc.blit(pygame.transform.scale(pygame.image.load(covers[i]),(500,500)), (395, 5))
                    start(i)
                if 900 <= mouse_pos[0] <= 1260 and 525 <= mouse_pos[1] <= 885:
                    if i==2: i=0
                    else: i+=1
                    sc.blit(pygame.transform.scale(pygame.image.load(covers[i]),(500,500)), (395, 5))
                    start(i)
    pygame.display.flip()
    clock.tick(55)
pygame.quit()
