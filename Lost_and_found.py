import pygame, os

# create window vars
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('name of our game')
WHITE = (255, 255, 255)
# create assests
DOG = pygame.image.load(os.path.join('assets', 'left_dog.gif'))

# create window function
def create_window():
    WIN.fill(WHITE)
    WIN.blit(DOG, (100, 300))
    pygame.display.update()

# create main function for collisions
def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        create_window()
    pygame.quit()
    
if __name__ == "__main__":
    main()
