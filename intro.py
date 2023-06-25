# Pygame

import pygame
import sys

pygame.init()

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,100,100)
GREEN = (100,255,100)
BLUE = (100,100,255)


# Create window
size = (800,500)
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

# Initial position of the rectangle
coord_x = 400
coord_y = 200

speed_x = 3
speed_y = 3

while True:


    ### --- EVENTS --- 
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit(1)


    ### --- LOGIC --- 
    if coord_x > 720 or coord_x < 0:
        speed_x *= -1

    if coord_y > 320 or coord_y < 0:
        speed_y *= -1

    coord_x += speed_x
    coord_y += speed_y




    ### --- SCREEN BACKGROUND ---
    screen.fill(WHITE)
    
    ### --- DRAWING ---
    pygame.draw.line(screen, GREEN, [10,100],[150,200], 10)
    #pygame.draw.rect(screen, BLACK, (0,250,800,250))
    pygame.draw.circle(screen, RED, (100,150), 20)
    pygame.draw.rect(screen, RED, (coord_x,coord_y,80,80))

    for x in range(100, 700, 100):
        pygame.draw.rect(screen, BLUE, (x,350,50,50))




    ### --- UPDATE ---
    pygame.display.flip()
    clock.tick(60) # 60Hz = 60FPS