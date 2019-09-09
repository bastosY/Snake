import pygame
from pygame.locals import *
import random

def collision(element):
    
    for body in range(1, len(element)):
        if(element[0] == element[body]):
            return 1
       
        
def capture_apple(element1, element2):
    x = (element2[0], element2[1])
    if(element1[0][0] == element2[0] and element1[0][1] == element2[1]):
        return 1

def randomPos():
    return (random.randint(50,590) // 10 * 10, random.randint(50,590) // 10 * 10)

def main():

    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    my_direction = 3

    pygame.init()
    screen = pygame.display.set_mode((600,600))
    pygame.display.set_caption('snake')
    exit = False
    clock = pygame.time.Clock()

    snake = [(200,200),(210,200),(220,200)]
    snake_init = [(200,200),(210,200),(220,200)]
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))
    
    apple = pygame.Surface((10,10))
    apple_pos = randomPos()
    apple.fill((255,0,0))

    score = 0
    scoreboard = pygame.Surface((600,50))
    scoreboard.fill((255,0,0))

    barrier = pygame.Surface((600,50))
    barrier.fill((255,0,0))

    sides = pygame.Surface((1,600))
    sides.fill((255,0,0))

    pygame.font.init()
    font = pygame.font.get_default_font()
    textScore = pygame.font.SysFont(font, 45)

    while exit == False:
        clock.tick(20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    exit = True
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP;   
                elif event.key == K_RIGHT:
                    my_direction = RIGHT
                elif event.key == K_DOWN:
                    my_direction = DOWN
                elif event.key == K_LEFT:
                    my_direction = LEFT
                elif event.key == K_SPACE:
                    snake.append((0,0))

       

        screen.fill((0,0,0))
        for pos in snake:
            screen.blit(snake_skin, pos)
        
        if(my_direction == UP):
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if(my_direction == RIGHT):
            snake[0] = (snake[0][0] + 10, snake[0][1])
        if(my_direction == DOWN):
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if(my_direction == LEFT):
            snake[0] = (snake[0][0] - 10, snake[0][1])

        if(collision(snake)):
            score = 0
            del(snake[3::])
           
        for i in range(len(snake) -1, 0, -1):
            snake[i] = (snake[i-1][0], snake[i-1][1])

       
        if(snake[0][1] < 50 or snake[0][1] > 590 or snake[0][0] < 0 or snake[0][0] > 590):
            snake[0] = (200, 200)
            score = 0
            del(snake[3::])
            
        if(capture_apple(snake, apple_pos)):
            snake.append((0,0))
            score = score + 1
            apple_pos = randomPos()

        scoreboard.fill((255,0,0))
        text = textScore.render('Score:'+str(score),1,(255,255,255))

        scoreboard.blit(text, (20,10))
        screen.blit(apple, apple_pos)
        screen.blit(scoreboard, (0,0))
        screen.blit(barrier, (0,599))
        screen.blit(sides, (599,0))
        screen.blit(sides, (0,0))
        pygame.display.update()

    pygame.quit()
main()