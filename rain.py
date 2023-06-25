import pygame
import sys
import random

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

coord_list = []
for i in range(60):
    x = random.randint(0,800)
    y = random.randint(0,500)
    coord_list.append( [x,y] )

while True:

    ### --- EVENTS --- 
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            sys.exit(1)

    ### --- LOGIC --




    ### --- DRAWING ---
    screen.fill(BLACK)
    

    for coord in coord_list:
        pygame.draw.circle(screen, BLUE, coord, 2)
        coord[1] += 3 # fall speed of the rain

        if coord[1] > 500:
            coord[1] = 0

    ### --- UPDATE ---
    pygame.display.flip()
    clock.tick(60) # 60Hz = 60FPS