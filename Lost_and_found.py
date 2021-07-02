import pygame, os
pygame.font.init()
pygame.mixer.init()

# create window variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('name of our game')
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)
# create assests
DOG_HEIGHT, DOG_WIDTH = 55, 40
OWNER_HEIGHT, OWNER_WIDTH = 55, 40
MAX_BULLETS = 10
# use join so different operating systems can load
# BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('assets', ''))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('assets', 'gunshot.wav'))
DOG = pygame.image.load(os.path.join('assets', 'left_dog.gif'))
OWNER = pygame.image.load(os.path.join('assets', 'owner.gif'))
YARD = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'pixelated_yard.png')), (WIDTH, HEIGHT))
dog_right = pygame.transform.flip(pygame.transform.scale(DOG, (DOG_HEIGHT, DOG_WIDTH)), True, False)
owner_place = pygame.transform.scale(OWNER, (OWNER_HEIGHT, OWNER_WIDTH))
# create consistency for CPU access
FPS = 60
# velocity is 5 pixels per key press
VEL = 5 
# bullet velocity determins how fast the bullets move
BULLET_VEL = 9
# new event for bullet collision
DOG_HIT = pygame.USEREVENT + 1
OWNER_HIT = pygame.USEREVENT + 2

# create window function
def create_window(dog, owner, dog_bullets, owner_bullets, dog_health, owner_health):
    # assets appear in order from top down.
    WIN.blit(YARD, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    dog_health_text = HEALTH_FONT.render("Health: " + str(dog_health), 1, BLACK)
    owner_health_text = HEALTH_FONT.render("Health: " + str(owner_health), 1, BLACK)
    WIN.blit(dog_health_text, (WIDTH - dog_health_text.get_width() - 10, 10))
    WIN.blit(owner_health_text, (10, 10))
    WIN.blit(dog_right, (dog.x, dog.y))
    WIN.blit(owner_place, (owner.x, owner.y))
    for bullet in dog_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    for bullet in owner_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    # this constantly updates the window at the set FPS
    pygame.display.update()

def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH//2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

#create movement with arrow keys
def dog_movement(keys_pressed, dog, BORDER):
    if keys_pressed[pygame.K_a] and dog.x - VEL > 0: #LEFT
        dog.x -= VEL
    if keys_pressed[pygame.K_d] and dog.x + VEL + dog.width < BORDER.x: #RIGHT
       dog.x += VEL
    if keys_pressed[pygame.K_w] and dog.y - VEL > 0: #DOWN
       dog.y -= VEL
    if keys_pressed[pygame.K_s] and dog.y + VEL + dog.height < HEIGHT: #UP
       dog.y += VEL

#create movement with wsad
def owner_movement(keys_pressed, owner, BORDER):
    if keys_pressed[pygame.K_LEFT] and owner.x - VEL > BORDER.x + BORDER.width:
       owner.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and owner.x + VEL + owner.width < WIDTH:
       owner.x += VEL
    if keys_pressed[pygame.K_UP] and owner.y - VEL > 0:
       owner.y -= VEL
    if keys_pressed[pygame.K_DOWN] and owner.y + VEL + owner.height < HEIGHT - 15:
       owner.y += VEL

# handles bullet collision
def handle_bullets(dog_bullets, owner_bullets, dog, owner):
    for bullet in dog_bullets:
        bullet.x += BULLET_VEL
        if owner.colliderect(bullet):
            pygame.event.post(pygame.event.Event(OWNER_HIT))
            dog_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            dog_bullets.remove(bullet)

    for bullet in owner_bullets:
        bullet.x -= BULLET_VEL
        if dog.colliderect(bullet):
            pygame.event.post(pygame.event.Event(DOG_HIT))
            owner_bullets.remove(bullet)
        elif bullet.x < 0:
            owner_bullets.remove(bullet)

# create main function for collisions
# add clock to implement the FPS
# add key handling capablitites
def main():
    dog = pygame.Rect(100, 300, DOG_WIDTH, DOG_HEIGHT)
    owner = pygame.Rect(700, 300, OWNER_WIDTH, OWNER_HEIGHT)
    dog_health = 10
    owner_health = 10
    dog_bullets = []
    owner_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT and len(dog_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(dog.x + dog.width, dog.y + dog.height//2 - 2, 10, 5) 
                    dog_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_KP0 and len(owner_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(owner.x, owner.y + owner.height//2 - 2, 10, 5) 
                    owner_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == DOG_HIT:
                owner_health -= 1
                # BULLET_HIT_SOUND.play()
            if event.type == OWNER_HIT:
                dog_health -= 1
                # BULLET_HIT_SOUND.play()
        winner_text = ""
        if dog_health <= 0:
            winner_text = "Dog Wins!"
        if owner_health <= 0:
            winner_text = "Owner Wins!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        dog_movement(keys_pressed, dog, BORDER)
        owner_movement(keys_pressed, owner, BORDER)
        handle_bullets(dog_bullets, owner_bullets, dog, owner)
        create_window(dog, owner, dog_bullets, owner_bullets, dog_health, owner_health)
    main()
    
if __name__ == "__main__":
    main()
