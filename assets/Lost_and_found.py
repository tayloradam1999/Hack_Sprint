import pygame
from pygame.locals import *
import os
import sys

# create window vars
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('name of our game')

# create assests
DOG = pygame.image.load(os.path.join('assets', Interceptor-Walk(Left).gif))

# create window function
def create_window():
    WIN.blit(DOG, (100, 300))
    pygame.display.update()

# create main function for collisions
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        # window will go here
    pygame.quit()
    sys.exit(0)
if __name__ == "__main__":
    main()
