import pygame
import sys
import random
import time

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnackChase")

# Fonts
font = pygame.font.Font(None, 36)

# Player settings
player_color = (0, 255, 0)  # Green
player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 3

# Snack settings
snack_color = (255, 0, 0)  # Red
snack_radius = 10
snack_x = random.randint(50, WIDTH - 50)
snack_y = random.randint(50, HEIGHT - 50)

# Enemy settings
enemy_color = (0, 0, 255)  # Blue
enemy_radius = 20
enemy_x = random.randint(50, WIDTH - 50)
enemy_y = random.randint(50, HEIGHT - 50)
enemy_speed = 1

# Score and timer
score = 0
start_time = time.time()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep player on screen
    player_x = max(player_radius, min(WIDTH - player_radius, player_x))
    player_y = max(player_radius, min(HEIGHT - player_radius, player_y))

    # Move enemy toward player
    if enemy_x < player_x:
        enemy_x += enemy_speed
    if enemy_x > player_x:
        enemy_x -= enemy_speed
    if enemy_y < player_y:
        enemy_y += enemy_speed
    if enemy_y > player_y:
        enemy_y -= enemy_speed

    # Check collision with snack
    distance_snack = ((player_x - snack_x) ** 2 + (player_y - snack_y) ** 2) ** 0.5
    if distance_snack < player_radius + snack_radius:
        score += 1
        snack_x = random.randint(50, WIDTH - 50)
        snack_y = random.randint(50, HEIGHT - 50)

    # Check collision with enemy
    distance_enemy = ((player_x - enemy_x) ** 2 + (player_y - enemy_y) ** 2) ** 0.5
    if distance_enemy < player_radius + enemy_radius:
        running = False  

    # Drawing
    screen.fill((0, 0, 0))  # Black background
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)
    pygame.draw.circle(screen, snack_color, (snack_x, snack_y), snack_radius)
    pygame.draw.circle(screen, enemy_color, (enemy_x, enemy_y), enemy_radius)

    # Draw score
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    # Draw timer
    elapsed_time = int(time.time() - start_time)
    time_text = font.render(f"Time: {elapsed_time}s", True, (255, 255, 255))
    screen.blit(time_text, (10, 50)

    # Update screen
    pygame.display.flip()
    pygame.time.Clock().tick(60)  # Limit to 60 FPS

# Quit game
pygame.quit()
sys.exit()
