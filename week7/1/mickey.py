import pygame, datetime

pygame.init()

W, H = 800, 800
sc = pygame.display.set_mode((W, H))
font = pygame.font.SysFont('Verdana', 50)
clock = pygame.time.Clock()
w = W//2
h = H//2

mickey = pygame.image.load("main-clock.png")
leftHand = pygame.image.load("left-hand.png")
rightHand = pygame.image.load("right-hand.png")
mickeyRect = mickey.get_rect(center = (w,h))
sc.blit(mickey, (w, h))

def blitRotateCenter(sc, image, center, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = center).center)
    sc.blit(rotated_image, new_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    sc.blit(mickey, mickeyRect)
    t = datetime.datetime.now()
    minute, second = t.minute, t.second
   
    time_render = font.render(f'{t:%H:%M:%S}', True, pygame.Color('green'), pygame.Color('red'))
    sc.blit(time_render,(0,0))
    
    langle = (74.5- t.second)*6 
    rangle = (440 - (t.minute*6))+langle/60
    blitRotateCenter(sc, leftHand, (w,h), langle) 
    blitRotateCenter(sc, rightHand, (w,h), rangle)
    pygame.display.flip()
    clock.tick