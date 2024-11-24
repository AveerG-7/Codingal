import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 50
ENEMY_SIZE = 50
NUM_ENEMIES = 7
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= 5
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_UP]: self.rect.y -= 5
        if keys[pygame.K_DOWN]: self.rect.y += 5
        self.rect.clamp_ip(screen.get_rect())

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((ENEMY_SIZE, ENEMY_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect(topleft=(random.randint(0, SCREEN_WIDTH - ENEMY_SIZE), 
                                                  random.randint(0, SCREEN_HEIGHT - ENEMY_SIZE)))

def main():
    player = Player()
    enemies = pygame.sprite.Group(Enemy() for _ in range(NUM_ENEMIES))
    all_sprites = pygame.sprite.Group(player, *enemies)

    score = 0
    font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        player.update()
        if pygame.sprite.spritecollide(player, enemies, True):
            score += 1
            enemies.add(Enemy())

        screen.fill(WHITE)
        all_sprites.draw(screen)
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()