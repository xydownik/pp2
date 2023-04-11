import pygame
import math
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

def circle():
    circle_pos = pygame.mouse.get_pos()
    r = 30
    pygame.draw.circle(sc, color, circle_pos, r)

def square():
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
def equil_tri():
    tri_pos = pygame.mouse.get_pos()
    a = 50
    r = a/math.sqrt(3)
    b = a/math.sqrt(12)
    x = tri_pos[0]
    y = tri_pos[1]                                # r  = a/sqrt(3) --> theory of right tri
    A = ((x- a/2),(y + b))         # b = sqrt(r^2-(s/2)^2) = a/sqrt(12)
    B = (x, (y-r))                    # just gave coordinates of points according to its center which is given by mouse
    C = ((x+a/2), (y + b))
    pygame.draw.polygon(sc, color,(A,B,C))
    
def right_tri():
    a = 50
    b = 25
    tri_pos = pygame.mouse.get_pos()
    x = tri_pos[0]
    y = tri_pos[1]
    A = tri_pos
    B = (x, (y-b))
    C = ((x+a), y)
    pygame.draw.polygon(sc, color, (A,B,C))

def rhombus():
    r_pos = pygame.mouse.get_pos()
    x = r_pos[0]
    y = r_pos[1]
    a = 15
    b = 30
    A = (x, y+b)
    B =(x-a, y)
    C = (x, y-b)
    D = (x+a, y)
    pygame.draw.polygon(sc,color,(A, B, C, D))
while check:
    event = pygame.event.wait()
    
    if event.type == pygame.QUIT:
        check = False
        pygame.quit()
        
    
    if event.type == pygame.KEYDOWN:
        
        if event.key == pygame.K_1:
            color = red
            radius = 5
        elif event.key == pygame.K_2:
            color = blue
            radius = 5
        elif event.key == pygame.K_3:
            color = green
            radius = 5
            
        if event.key == pygame.K_0:
            sterka()
        
        if event.key == pygame.K_w:
            color = white
            radius = 20
        
        if event.key == pygame.K_s:
            square()
        
        if event.key == pygame.K_c:
            circle()
            
        if event.key == pygame.K_e:
            equil_tri()
            
        if event.key == pygame.K_r:
            right_tri()
        
        if event.key == pygame.K_m:
            rhombus()   
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