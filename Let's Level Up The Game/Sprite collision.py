import pygame
import random

# Starting the mixer
pygame.mixer.init()

surf_color = (0, 142, 204)
color = (0, 0, 0)

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(surf_color)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y += speed * speed / 10

    def moveBack(self, speed):
        self.rect.y -= speed * speed / 10

# Initialize Pygame
pygame.init()

# Set up screen and background
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("Sprite Collision")
bg = pygame.image.load("download.jpeg")
bg = pygame.transform.scale(bg, (500, 400))

# Sprite groups
all_sprites_list = pygame.sprite.Group()

# Player sprite
sp1 = Sprite(color, 20, 30)
sp1.rect.x = random.randint(0, 480)
sp1.rect.y = random.randint(0, 370)
all_sprites_list.add(sp1)

# Enemy sprite
sp2 = Sprite((255, 0, 0), 20, 30)
sp2.rect.x = random.randint(0, 480)
sp2.rect.y = random.randint(0, 370)
all_sprites_list.add(sp2)

# Variables for enemy movement
enemy_speed = 2
enemy_directions = [(enemy_speed, 0), (-enemy_speed, 0), (0, enemy_speed), (0, -enemy_speed)]
current_direction = random.choice(enemy_directions)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_DOWN]:
        sp1.moveForward(5)
    if keys[pygame.K_UP]:
        sp1.moveBack(5)

    # Enemy movement
    sp2.rect.x += current_direction[0]
    sp2.rect.y += current_direction[1]

    # Change direction if the enemy hits screen boundaries
    if sp2.rect.x <= 0 or sp2.rect.x >= 480:
        current_direction = random.choice(enemy_directions)
    if sp2.rect.y <= 0 or sp2.rect.y >= 370:
        current_direction = random.choice(enemy_directions)

    # Collision detection
    if sp1.rect.colliderect(sp2.rect):
        text = "You win!"
        font = pygame.font.SysFont("Times New Roman", 72)
        text_surface = font.render(text, True, (158, 16, 16))
        screen.blit(text_surface, (250 - text_surface.get_width() // 2, 200 - text_surface.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(2000)  # Pause for 2 seconds before exiting
        running = False

    # Update screen
    screen.blit(bg, (0, 0))
    all_sprites_list.draw(screen)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(60)

pygame.quit()
