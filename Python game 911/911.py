import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Load and scale images
try:
    background = pygame.image.load("911.webp")
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    plane_img = pygame.image.load("plane.webp")
    plane_img = pygame.transform.scale(plane_img, (100, 50))
    tower_img = pygame.image.load("tower.jpeg")
    tower_img = pygame.transform.scale(tower_img, (100, 300))
    bang_img = pygame.image.load("bang.jpeg")
    bang_img = pygame.transform.scale(bang_img, (120, 120))
except pygame.error as e:
    print(f"Error loading images: {e}")
    sys.exit()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("9/11 History Project")

# Tower and plane positions
tower1_pos = [200, 300]
tower2_pos = [500, 300]
plane1_pos = [0, 100]  # Controlled by arrow keys
plane2_pos = [WIDTH - 100, 200]  # Controlled by WASD

# Fonts
font = pygame.font.SysFont("Arial", 24)

# Game clock
clock = pygame.time.Clock()

# Game variables
tower1_falling = False
tower2_falling = False
fall_speed = 2

bang1_shown = False
bang2_shown = False
bang_timer1 = 0
bang_timer2 = 0

# Speed for plane movement
plane_speed = 5

# Main loop
running = True
while running:
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control planes
    keys = pygame.key.get_pressed()
    # Plane 1 (Arrow keys)
    if keys[pygame.K_UP]:
        plane1_pos[1] -= plane_speed
    if keys[pygame.K_DOWN]:
        plane1_pos[1] += plane_speed
    if keys[pygame.K_LEFT]:
        plane1_pos[0] -= plane_speed
    if keys[pygame.K_RIGHT]:
        plane1_pos[0] += plane_speed

    # Plane 2 (WASD)
    if keys[pygame.K_w]:
        plane2_pos[1] -= plane_speed
    if keys[pygame.K_s]:
        plane2_pos[1] += plane_speed
    if keys[pygame.K_a]:
        plane2_pos[0] -= plane_speed
    if keys[pygame.K_d]:
        plane2_pos[0] += plane_speed

    # Collision detection
    if not tower1_falling and not bang1_shown and plane1_pos[0] + 100 >= tower1_pos[0] and plane1_pos[1] < tower1_pos[1] + 300:
        bang1_shown = True
        bang_timer1 = pygame.time.get_ticks()
    if not tower2_falling and not bang2_shown and plane2_pos[0] <= tower2_pos[0] + 100 and plane2_pos[1] < tower2_pos[1] + 300:
        bang2_shown = True
        bang_timer2 = pygame.time.get_ticks()

    # Handle "bang" image timing (display for 2 seconds)
    current_time = pygame.time.get_ticks()
    if bang1_shown and current_time - bang_timer1 > 2000:  # Show for 2 seconds
        bang1_shown = False
        tower1_falling = True  # Tower 1 starts falling after bang disappears
    if bang2_shown and current_time - bang_timer2 > 2000:
        bang2_shown = False
        tower2_falling = True  # Tower 2 starts falling after bang disappears

    # Make towers fall
    if tower1_falling and tower1_pos[1] < HEIGHT:
        tower1_pos[1] += fall_speed
    if tower2_falling and tower2_pos[1] < HEIGHT:
        tower2_pos[1] += fall_speed

    # Draw towers
    if not bang1_shown:
        screen.blit(tower_img, tower1_pos)
    if not bang2_shown:
        screen.blit(tower_img, tower2_pos)

    # Draw planes
    if not bang1_shown:
        screen.blit(plane_img, plane1_pos)
    if not bang2_shown:
        screen.blit(plane_img, plane2_pos)

    # Draw "bang" images at the crash points
    if bang1_shown:
        bang_x1 = tower1_pos[0] - 10
        bang_y1 = tower1_pos[1] - 120  # Adjust for correct position
        screen.blit(bang_img, (bang_x1, bang_y1))
    if bang2_shown:
        bang_x2 = tower2_pos[0] - 10
        bang_y2 = tower2_pos[1] - 120  # Adjust for correct position
        screen.blit(bang_img, (bang_x2, bang_y2))

    # Display text
    if tower1_falling or tower2_falling:
        text = font.render(
            "This simulation represents the tragic events of 9/11.", True, BLACK
        )
        screen.blit(text, (50, 50))

    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
