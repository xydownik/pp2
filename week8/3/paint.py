import pygame
    
pygame.init()

sc = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)

color = red
lpos = (0,0)
mouse = False
sc.fill(white)
pygame.display.update()
radius = 5

clock = pygame.time.Clock()
check = True

#functions
def sterka():
    rect_pos = pygame.mouse.get_pos()
    w = 30
    h = 30
    pygame.draw.rect(sc, white, (rect_pos, (w, h)))

def krug():
    circle_pos = pygame.mouse.get_pos()
    r = 30
    pygame.draw.circle(sc, color, circle_pos, r)

def quadrat():
    rect_pos = pygame.mouse.get_pos()
    w = 50
    h = 50
    pygame.draw.rect(sc, color, (rect_pos, (w, h)))

def liner(surface, color, start, end, radius=1) :
    X = end[0] - start[0]
    Y = end[1] - start[1]
    dist = max(abs(X), abs(Y))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * X)
        y = int(start[1] + float(i) / dist * Y)
        pygame.draw.circle(surface, color, (x, y), radius)

while check:
    event = pygame.event.wait()
    
    if event.type == pygame.QUIT:
        check = False
        pygame.quit()
        
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_r:
            color = red
            radius = 5
        elif event.key == pygame.K_b:
            color = blue
            radius = 5
        elif event.key == pygame.K_g:
            color = green
            radius = 5
            
        if event.key == pygame.K_e:
            sterka()
        
        if event.key == pygame.K_w:
            color = white
            radius = 20
        
        if event.key == pygame.K_s:
            quadrat()
        
        if event.key == pygame.K_c:
            krug()
            
    if event.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(sc, color, event.pos, 5)
        mouse = True
        
    if event.type == pygame.MOUSEBUTTONUP:
        mouse = False
    
    
    if event.type == pygame.MOUSEMOTION:
        if mouse:
            pygame.draw.circle(sc,color,event.pos,radius)
            liner(sc,color,event.pos,lpos,radius)
        lpos = event.pos
        
    pygame.display.update()
   
    clock.tick(60)