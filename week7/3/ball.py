import pygame
pygame.init()
  
sc = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

pygame.display.set_caption("Moving circle")
  
x = 400
y = 400
  
radius = 25
  
vel = 20
  
run = True
  
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