import pygame
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background = pygame.image.load("bg.jpeg")
pygame.display.set_caption("Bob's galaxy space alien shooter")

icon = pygame.image.load("logo.jpeg")
pygame.display.set_icon(icon)
playerimg = pygame.image.load("spaceship non enemy.jpeg")
Player_x = PLAYER_START_X
Player_y = PLAYER_START_Y
player_x_change = 0
enemyimg = []
enemy_x = []
enemy_y = []
enemyxchange = []
enemyychange = []
no_of_enemy = 6
for _i in range(no_of_enemy):
    enemyimg.append(pygame.image.load("spaceship.jpeg"))
    enemy_x.append(random.randit(0,SCREEN_WIDTH-64))
    enemy_y.append(random.randit(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyxchange.append(ENEMY_SPEED_X)
    enemyychange.append(ENEMY_SPEED_Y)
    











