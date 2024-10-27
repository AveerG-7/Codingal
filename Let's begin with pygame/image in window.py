import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame window + image")
image = pygame.image.load("real-madrid-badge.png")
defualtimage = (200,200)
image = pygame.transform.scale(image,(defualtimage))
defpos = ((150,150))
running = True
while running:
    screen.fill((255,255,255))
    screen.blit(image,(defpos))
    for event in pygame.event.get():
  
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    pygame.display.flip()

