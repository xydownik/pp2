import pygame
import button
from text import InputBox
from map import world
pygame.init()

SCENE_Q1 = 1
SCENE_Q2 = 2
SCENE_Q3 = 3
SCENE_Q4 = 4
SCENE_Q5 = 5
SCENE_GAME = 0
SCENE_MENU = 6

W,H = 800,800
font = pygame.font.Font(None, 64)
clock = pygame.time.Clock()
cell = 40
ww,wh = W//cell, H//cell
water = pygame.transform.scale(pygame.image.load('resources\water.png'),(70,120))
glass = pygame.transform.scale(pygame.image.load('resources\glass.png'),(320,320))
bg =  pygame.transform.scale(pygame.image.load('resources\\bg.jpg'),(800,800))
blocks = pygame.transform.scale(pygame.image.load('resources\metal.png'),(40,40))


i1 = pygame.transform.scale(pygame.image.load('resources\image1.png'),(800,500))
i2 = pygame.transform.scale(pygame.image.load('resources\image2.png'),(800,500))
i3 = pygame.transform.scale(pygame.image.load('resources\image3.png'),(800,500))
i4 = pygame.transform.scale(pygame.image.load('resources\image4.png'),(800,500))
i5 = pygame.transform.scale(pygame.image.load('resources\image5.png'),(800,500))

active = False
pipes = []
def pipe():
    for i in range(1,8):
        pip = pygame.transform.scale(pygame.image.load(f'resources\pipe{i}.png'),(120,120))
        pipes.append(pip)
    return  pipes
    
class Object(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.Frame = 0
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center = (x, y))
        
    def update(self):
        self.Frame += 0.11
        if self.Frame > 10:
            self.Frame -= 10

        Personnel = ['1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png','8.png','9.png','10.png']
        self.image = pygame.transform.scale(pygame.image.load('resources\\'+ Personnel[int(self.Frame)]).convert_alpha(), (200,80))

input_box1 = InputBox(200, 600, 200, 80)
input_box2 = InputBox(200, 600, 200, 80)
input_box3 = InputBox(200, 600, 200, 80)
input_box4 = InputBox(200, 600, 200, 80)
input_box5 = InputBox(200, 600, 200, 80)
in_boxes = [input_box1,input_box2,input_box3,input_box4,input_box5]
answers = ['CONTRADICTION', 'MATPLOTLIB','CRYPTOGRAPHY','GAME OF THRONES','COPERNICUS']
images = [i1,i2,i3,i4,i5]
def menu(window):
    music = pygame.mixer.music.load('resources\music2.mp3')

# установка громкости музыки
    pygame.mixer.music.set_volume(0.5)

# проигрывание музыки
    pygame.mixer.music.play(-1)

#game variables
    game_paused = False
    menu_state = "main"

#define fonts
    font = pygame.font.SysFont("arialblack", 70)

#define colours
    TEXT_COL = (255, 0, 0)

#load button images
    play_img = pygame.image.load("resources\play.png").convert_alpha()
    rules_img = pygame.image.load("resources\game_rules.png").convert_alpha()
    quit_img = pygame.image.load("resources\quit.png").convert_alpha()
    back_img = pygame.image.load('resources\\back.png').convert_alpha()
    rule_list_img=pygame.image.load("resources\ere.png").convert_alpha()

#create button instances
    resume_button = button.Button(270, 125, play_img, 1)
    rules_button = button.Button(265, 250, rules_img, 1.03)
    quit_button = button.Button(270, 375, quit_img, 1)
    rule_button = button.Button(50, 5,rule_list_img, 1)
    back_button = button.Button(535, 350, back_img, 1)


    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        window.blit(img, (x, y))
#game loop
    run = True

    while run:
        background_image = pygame.image.load('resources\\backk.png')
        window.blit(background_image, (0, 0))


  #check if game is paused
        if game_paused == True:
    #check menu state
            if menu_state == "main":
      # draw pause window buttons
                if resume_button.draw(window):
                    menu_state = "play"
                if rules_button.draw(window):
                    menu_state = "rules"
                if quit_button.draw(window):
                    quit()
    
                
    #check if the options menu is open
            if menu_state == "rules":
      
      #draw the different options buttons
                if rule_button.draw(window):
   
                    print("любое слово")
                back = (pygame.image.load('resources\\backk.png'))
                rule=pygame.image.load('resources\ere.png')
                window.blit(back, (0, 0))
                window.blit(rule, (30, 100))
  
                if back_button.draw(window):
                    menu_state = "main"
      
            if menu_state == "play":
                if resume_button.draw(window):
                    print("play start")
     
                    return SCENE_GAME 
      
        else:
            draw_text("DEADPOOL", font, TEXT_COL, 240, 350)

  #event handler
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_paused = True
            if event.type == pygame.QUIT:
                quit()
            
            
        pygame.display.update()

def q1(window,i):
    # global points
    # points = 0
    FPS = 30
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    
                    return SCENE_GAME
            
            
            in_boxes[i].handle_event(event, answers[i])
            in_boxes[i].update()
            window.fill((255,255, 255)) 
            window.blit(images[i],(0,0))
            in_boxes[i].draw(window) 
            
        # points+= in_boxes[i].point   
        pygame.display.update()

# points = input_box1.point+input_box2.point

points = 0
for i in in_boxes:
    points +=i.point
def game(window):
    FPS = 60
    clock   = pygame.time.Clock()
    player = Object(600, 450, 'resources\\1.png')  
    play = True
    while play:

            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:   
                        play = False 
                        return SCENE_MENU
            
            #bg             
            window.blit(bg,(0,0))
            
            #player
            player.update()
            window.blit(player.image, player.rect) 
    
            #pool
            window.blit(water,(445,640))
            s = pygame.Surface((320,320))
            s.set_alpha(50)
            s.fill(pygame.Color('blue'))
            window.blit(s, (240,240))
            window.blit(glass,(240,240))

            #pipes
            pipes = pipe()   
            pipe3 = window.blit(pipes[3],(420,640))
            pipe0 = window.blit(pipes[0],(460,40))
            pipe4 = window.blit(pipes[4],(350,40))
            pipe1 = window.blit(pipes[1],(40,460))
            pipe2 = window.blit(pipes[2],(40,220))
            pipe7 = window.blit(pygame.transform.rotate(pipes[1],90),(260,40))
            pipe5 = window.blit(pipes[5],(640,420))
            pipe6 = window.blit(pipes[6],(640,300))
            pos = pygame.mouse.get_pos()
            #questions
            if pipe0.collidepoint(pos) or pipe4.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    return SCENE_Q1
            elif pipe7.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    return SCENE_Q2
            elif pipe2.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    return SCENE_Q3
            elif pipe1.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    return SCENE_Q4
            elif pipe3.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    return SCENE_Q5
            
            #map
            for i in range(len(world)):
                for j in range(len(world[i])):
                    x,y = j*cell,i*cell
            
                    if world[i][j] == 'B':
                        window.blit(blocks, (x,y))
            surf = font.render(str(points), True, pygame.Color('white'))
            window.blit(surf,(740,0))
            pygame.display.update()

def main():
    window = pygame.display.set_mode((800, 800))
    
        
    
    scene = SCENE_MENU
    while True:
        if scene == SCENE_Q1:
            scene = q1(window,0)
        elif scene == SCENE_Q2:
            scene = q1(window,1)
        elif scene == SCENE_Q3:
            scene = q1(window,2)
        elif scene == SCENE_Q4:
            scene = q1(window,3)
        elif scene == SCENE_Q5:
            scene = q1(window,4)
        elif scene == SCENE_GAME:
            scene = game(window)
               
        elif scene == SCENE_MENU:
            scene = menu(window)
            
        
main()