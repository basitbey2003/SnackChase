import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnackChase")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()

import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SnackChase")

# Player settings
player_color = (0, 255, 0)
player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 3

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)
    pygame.display.flip()

pygame.quit()
sys.exit()

# Player settings
player_color = (0, 255, 0)
player_radius = 20
player_x = WIDTH // 2
player_y = HEIGHT // 2
player_speed = 3

# Inside the game loop (after event loop)
keys = pygame.key.get_pressed()
if keys[pygame.K_LEFT]: player_x -= player_speed
if keys[pygame.K_RIGHT]: player_x += player_speed
if keys[pygame.K_UP]: player_y -= player_speed
if keys[pygame.K_DOWN]: player_y += player_speed

# Draw player
pygame.draw.circle(screen, player_color, (player_x, player_y), player_radius)

import random
snack_color = (255, 0, 0)
snack_radius = 10
snack_x = random.randint(50, WIDTH - 50)
snack_y = random.randint(50, HEIGHT - 50)
# Check collision
distance = ((player_x - snack_x)**2 + (player_y - snack_y)**2)**0.5
if distance < player_radius + snack_radius:
    snack_x = random.randint(50, WIDTH - 50)
    snack_y = random.randint(50, HEIGHT - 50)

# Draw snack
pygame.draw.circle(screen, snack_color, (snack_x, snack_y), snack_radius)



