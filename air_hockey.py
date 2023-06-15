import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 1920
HEIGHT = 1080
WINDOW_SIZE = (WIDTH, HEIGHT)
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Air Hockey")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define game variables
FPS = 60
player_score = 0
opponent_score = 0
winning_score = 7  # Score required to win the game

# Define paddle variables
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_SPEED = 5

player_1_paddle = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
player_2_paddle = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Define puck variables
PUCK_RADIUS = 10
PUCK_SPEED_X = 3
PUCK_SPEED_Y = 3

puck = pygame.Rect(WIDTH // 2 - PUCK_RADIUS // 2, HEIGHT // 2 - PUCK_RADIUS // 2, PUCK_RADIUS, PUCK_RADIUS)
puck_speed_x = PUCK_SPEED_X * random.choice((1, -1))
puck_speed_y = PUCK_SPEED_Y * random.choice((1, -1))

clock = pygame.time.Clock()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()

    # Player 1 controls
    if keys[pygame.K_w] and player_1_paddle.y > 0:
        player_1_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and player_1_paddle.y < HEIGHT - PADDLE_HEIGHT:
        player_1_paddle.y += PADDLE_SPEED
    if keys[pygame.K_a] and player_1_paddle.x > 0:
        player_1_paddle.x -= PADDLE_SPEED
    if keys[pygame.K_d] and player_1_paddle.x < WIDTH - PADDLE_HEIGHT:
        player_1_paddle.x += PADDLE_SPEED
   
   # Player 2 controls
    if keys[pygame.K_UP] and player_2_paddle.y > 0:
        player_2_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_DOWN] and player_2_paddle.y < HEIGHT - PADDLE_HEIGHT:
        player_2_paddle.y += PADDLE_SPEED
    if keys[pygame.K_LEFT] and player_2_paddle.x > 0:
        player_2_paddle.x -= PADDLE_SPEED
    if keys[pygame.K_RIGHT] and player_2_paddle.x < WIDTH - PADDLE_HEIGHT:
        player_2_paddle.x += PADDLE_SPEED
   
    # Move the puck
    puck.x += puck_speed_x
    puck.y += puck_speed_y

    # Collision detection with paddles
    if puck.colliderect(player_1_paddle):
        if player_1_paddle.x > puck.x:
            puck_speed_x = 3
        if player_1_paddle.x < puck.x:
            puck_speed_x = -3
        # puck_speed_x *= -1
    if puck.colliderect(player_2_paddle):
        if player_2_paddle.x > puck.x:
            puck_speed_x = 3
        if player_2_paddle.x < puck.x:
            puck_speed_x = -3
    # Collision detection with walls
    if puck.y > HEIGHT - PUCK_RADIUS or puck.y < 0:
        puck_speed_y *= -1

    # Scoring
    if puck.x > WIDTH:
        player_score += 1
        if player_score == winning_score:
            print("Congrats Player 1, you win!")
            running = False
        else:
            puck.center = (WIDTH // 2, HEIGHT // 2)
            puck_speed_x = PUCK_SPEED_X * random.choice((1, -1))
            puck_speed_y = PUCK_SPEED_Y * random.choice((1, -1))
    if puck.x < 0:
        opponent_score += 1
        if opponent_score == winning_score:
            print("Congrats Player 2, you win!")
            running = False
        else:
            puck.center = (WIDTH // 2, HEIGHT // 2)
            puck_speed_x = PUCK_SPEED_X * random.choice((1, -1))
            puck_speed_y = PUCK_SPEED_Y * random.choice((1, -1))

    # Draw the game elements
    window.fill(BLACK)
    pygame.draw.rect(window, RED, player_1_paddle)
    pygame.draw.rect(window, BLUE, player_2_paddle)
    pygame.draw.ellipse(window, WHITE, puck)
    pygame.draw.aaline(window, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

    # Draw the scores
    font = pygame.font.Font(None, 36)
    player_text = font.render(str(player_score), True, WHITE)
    opponent_text = font.render(str(opponent_score), True, WHITE)
    window.blit(player_text, (WIDTH // 2 - 30, 10))
    window.blit(opponent_text, (WIDTH // 2 + 20, 10))

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()