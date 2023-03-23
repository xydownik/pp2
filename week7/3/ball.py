# import pygame

# pygame.init()

# sc = pygame.display.set_mode((800,800))
# sc.fill((255,255,255))
# clock = pygame.time.Clock()

# ball = pygame.draw.circle(sc, 'red', (400,400), 25)
# speed = 25
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
        
#         if event.type==pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 pass
#             elif event.key == pygame.K_DOWN:
#                 pass
#             elif event.key == pygame.K_LEFT:
#                 pass
#             elif event.key == pygame.K_RIGHT:
#                 pass
            
    
#     pygame.display.update()
#     clock.tick(60)


import pygame
pygame.init()
  
sc = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption("Moving rectangle")
  
# object current co-ordinates 
x = 400
y = 400
  
# dimensions of the object 
radius = 25
  
# velocity / speed of movement
vel = 20
  
# Indicates pygame is running
run = True
  
# infinite loop 
while run:
    pygame.time.delay(10)
      
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
              
            run = False
   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>0:
          
        x -= vel
          
    if keys[pygame.K_RIGHT] and x<800-radius*2:
          
        x += vel
         
    if keys[pygame.K_UP] and y>0:
          
        y -= vel
           
    if keys[pygame.K_DOWN] and y<800-radius*2:
        y += vel
         
    
    sc.fill((255, 255, 255))
      
    pygame.draw.circle(sc, 'red', (x, y), radius)
      
    pygame.display.update() 

pygame.quit()
clock.tick(20)