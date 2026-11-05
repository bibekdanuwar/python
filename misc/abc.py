import pygame
import random

pygame.init()

# Window
WIDTH = 900
HEIGHT = 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Runner")

# Colors
WHITE = (255, 255, 255)
BLACK = (30, 30, 30)
GREEN = (0, 180, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Ground
GROUND_Y = 250

# Dino
dino_width = 40
dino_height = 50
dino_x = 80
dino_y = GROUND_Y - dino_height

velocity_y = 0
gravity = 0.8
jump_power = -14
is_jumping = False

# Obstacles
obstacles = []

# Score
score = 0
font = pygame.font.SysFont(None, 36)

speed = 7

running = True
game_over = False

while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if not game_over:
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_SPACE, pygame.K_UP]:
                    if not is_jumping:
                        velocity_y = jump_power
                        is_jumping = True

        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    obstacles.clear()
                    score = 0
                    speed = 7
                    game_over = False
                    dino_y = GROUND_Y - dino_height
                    velocity_y = 0

    if not game_over:
        # Jump physics
        velocity_y += gravity
        dino_y += velocity_y

        if dino_y >= GROUND_Y - dino_height:
            dino_y = GROUND_Y - dino_height
            velocity_y = 0
            is_jumping = False

        # Spawn obstacles
        if random.randint(1, 70) == 1:
            obstacle_width = random.randint(20, 35)
            obstacle_height = random.randint(40, 60)

            obstacles.append(
                pygame.Rect(
                    WIDTH,
                    GROUND_Y - obstacle_height,
                    obstacle_width,
                    obstacle_height,
                )
            )

        # Move obstacles
        for obstacle in obstacles[:]:
            obstacle.x -= speed

            if obstacle.right < 0:
                obstacles.remove(obstacle)
                score += 1

        # Increase difficulty
        speed = 7 + score // 10

        # Collision
        dino_rect = pygame.Rect(
            dino_x,
            dino_y,
            dino_width,
            dino_height,
        )

        for obstacle in obstacles:
            if dino_rect.colliderect(obstacle):
                game_over = True

    # Draw
    screen.fill(WHITE)

    # Ground
    pygame.draw.line(
        screen,
        BLACK,
        (0, GROUND_Y),
        (WIDTH, GROUND_Y),
        2
    )

    # Dino
    pygame.draw.rect(
        screen,
        BLACK,
        (dino_x, dino_y, dino_width, dino_height)
    )

    # Eye
    pygame.draw.circle(
        screen,
        WHITE,
        (dino_x + 30, int(dino_y + 12)),
        3
    )

    # Obstacles
    for obstacle in obstacles:
        pygame.draw.rect(screen, GREEN, obstacle)

    # Score
    score_text = font.render(
        f"Score: {score}",
        True,
        BLACK
    )
    screen.blit(score_text, (20, 20))

    if game_over:
        text = font.render(
            "GAME OVER - Press R",
            True,
            BLACK
        )
        screen.blit(
            text,
            (WIDTH // 2 - 150, HEIGHT // 2)
        )

    pygame.display.update()

pygame.quit()