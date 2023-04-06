import pygame
import random

def main():
    
    pygame.init()
  
    sc = pygame.display.set_mode((400,500))
    pygame.display.set_caption("Snake")
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    
    start = (0,100)
    end = (400,100)

    #Инструменты кода
    apple = (random.randint(1, sc.get_width() / 10 - 1) * 10, random.randint(10, sc.get_height() / 10 - 1) * 10)
    isapple = True
    score = 0
    speed = 1
    level = ['easy','normal','hard','very hard', 'impossible', 'demon', 'death']
    score_font = pygame.font.SysFont('lunchtime Double So',32)

    new_dir = 'left'
    dir = 'left'

    player = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]]

    clock = pygame.time.Clock()

    check = True

    while check:
        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                check = False
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    new_dir = 'up'
                if event.key == pygame.K_DOWN:
                    new_dir = 'down'
                if event.key == pygame.K_LEFT:
                    new_dir = 'left'
                if event.key == pygame.K_RIGHT:
                    new_dir = 'right'
            
        
        if dir != 'up' and new_dir == 'down':
            dir = 'down'
        if dir != 'down' and new_dir == 'up':
            dir = 'up'
        if dir != 'left' and new_dir == 'right':
            dir = 'right'
        if dir != 'right' and new_dir == 'left':
            dir = 'left'
        
        
        if dir == 'up':
            player[1] -= 10
        if dir == 'down':
            player[1] += 10 
        if dir == 'left':
            player[0] -= 10 
        if dir == 'right':
            player[0] += 10  
        
        
        while isapple:
            apple = (random.randint(1,sc.get_width() / 10 - 1) * 10, random.randint(10, sc.get_height() / 10 - 1) * 10)
            if apple not in snake:
                isapple = False
                
        snake.insert(0, list(player))
              
        
        if player[0] == apple[0] and player[1] == apple[1]:
            score += 1
            isapple = True
            speed = score // 4 + 1
        else:
            snake.pop()
        
        sc.fill(white) 
        
        pygame.draw.line(sc, black, start, end, 1)
        
        if ((player[0] < -5 or player[0] > sc.get_width() - 5) or (player[1] < 100 or player[1] > sc.get_height() - 5)):
            break
        
        print(snake[1:])
        print(player)
       
        if player in snake[1:]:
            break
       
        for pos in snake:
            pygame.draw.rect(sc, black, pygame.Rect(pos[0], pos[1], 10, 10))


        pygame.draw.rect(sc, red, pygame.Rect(apple[0],apple[1],10,10))
        
      
        sc.blit(score_font.render(f'Score: {score}' , True, black) , (20,38))
       
        if speed <= 7:
            sc.blit(score_font.render(f'Speed: {level [speed - 1]}', True, black), (20,58))
        else:
            sc.blit(score_font.render(f'Speed: death', True, black), (20,58))
        
        pygame.display.update()
       
        clock.tick(10 + speed * 2)
    
    while check:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                check = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main()
                if event.key == pygame.K_c:
                    check = False
        sc.fill(white)
        
        sc.blit(score_font.render('R-->restart OR C-->close ' , True, black), (35,200))

        pygame.display.update()
main()
pygame.quit()