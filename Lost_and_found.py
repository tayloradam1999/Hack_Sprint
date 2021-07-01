import pygame, os

# create window variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('name of our game')
WHITE = (255, 255, 255)
# create assests
DOG_HEIGHT, DOG_WIDTH = 55, 40
# use join so different operating systems can load
DOG = pygame.image.load(os.path.join('assets', 'left_dog.gif'))
# DOG2 = pygame.image.load(os.path.join('assets', 'left_dog.gif'))
dog_right = pygame.transform.flip(pygame.transform.scale(DOG, (DOG_HEIGHT, DOG_WIDTH)), True, False)
# create consistency for CPU access
FPS = 60
# velocity is 5 pixels per key press
VEL = 5 

# create window function
def create_window(dog):
    # assets appear in order from top down.
    WIN.fill(WHITE)
    # use blit to put images on the screen
    WIN.blit(dog_right, (dog.x, dog.y))
    # this constantly updates the window.
    pygame.display.update()

#create movement with keyboard keys
def dog_movement(keys_pressed, dog):
    if keys_pressed[pygame.K_LEFT] and dog.x - VEL > 0:
        dog.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and dog.x + VEL + dog.width < WIDTH:
       dog.x += VEL
    if keys_pressed[pygame.K_UP] and dog.y - VEL > 0:
       dog.y -= VEL
    if keys_pressed[pygame.K_DOWN] and dog.y + VEL + dog.height < HEIGHT:
       dog.y += VEL

# create main function for collisions
# add clock to implement the FPS
# add key handling capablitites
def main():
    dog = pygame.Rect(100, 300, DOG_WIDTH, DOG_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        dog_movement(keys_pressed, dog)
        create_window(dog)
    pygame.quit()
    
if __name__ == "__main__":
    main()
