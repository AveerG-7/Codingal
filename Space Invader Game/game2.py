import math
import random
import pygame
from pygame import mixer
import time  # To handle the pause

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 500))

# Background
background = pygame.image.load('bg.jpg')

# Sound
mixer.music.load("bg music.mp3")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('logo.jpeg')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship non enemy.jpg')
playerX = 370
playerY = 380
playerX_change = 0

# Enemy settings function
def create_enemy(level):
    enemyImg = []
    enemyX = []
    enemyY = []
    enemyX_change = []
    enemyY_change = []
    num_of_enemies = 6 + level * 2  # Increase enemies with each level

    for i in range(num_of_enemies):
        enemyImg.append(pygame.image.load('spaceship.jpg'))
        enemyX.append(random.randint(0, 736))
        enemyY.append(random.randint(50, 150))
        enemyX_change.append(2 + level)  # Increase speed in higher levels
        enemyY_change.append(20)

    return enemyImg, enemyX, enemyY, enemyX_change, enemyY_change, num_of_enemies

# Initialize enemies for level 1
level = 1
enemyImg, enemyX, enemyY, enemyX_change, enemyY_change, num_of_enemies = create_enemy(level)

# Bullet
bulletImg = pygame.image.load('bull.jpg')
bulletX = 0
bulletY = 380
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
testY = 10

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    return False

# Pause the game for a few seconds
def level_up_pause(level):
    font = pygame.font.Font('freesansbold.ttf', 64)
    level_text = font.render(f"Level {level}", True, (255, 255, 255))
    screen.blit(level_text, (300, 200))
    pygame.display.update()
    time.sleep(3)  # Pause for 3 seconds

# Game Loop
running = True
while running:
    screen.fill((0, 0, 0))  # RGB = Red, Green, Blue
    screen.blit(background, (0, 0))  # Background Image

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletSound = mixer.Sound("laser shooting sound.mp3")
                    bulletSound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 2000  # Move enemies off-screen
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= 736:
            enemyX_change[i] *= -1  # Reverse direction
            enemyY[i] += enemyY_change[i]

        # Collision Detection
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosionSound = mixer.Sound("explosion sound.mp3")
            explosionSound.play()
            bulletY = 380
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Check for level up
    if score_value >= 10 * level:  # Level up after every 10 points
        level += 1
        enemyImg, enemyX, enemyY, enemyX_change, enemyY_change, num_of_enemies = create_enemy(level)
        level_up_pause(level)  # Pause for 3 seconds after leveling up

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 380
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
