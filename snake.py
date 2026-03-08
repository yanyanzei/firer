import pygame
import random
import time

pygame.init()

width, high = 1000, 800
screen = pygame.display.set_mode((width, high))
pygame.display.set_caption("贪吃蛇")
clock = pygame.time.Clock()

red = (255, 0, 0)
green = (0, 255, 0)
body_long = 20
bx = body_long
by = 0

snake = [(width // 2, high // 2), (width // 2 - body_long, high // 2), (width // 2 - 2 * body_long, high // 2)]

def apple():

    while True:
        apple_x = random.randint(0, (width - body_long) // body_long) * body_long
        apple_y = random.randint(0, (high - body_long) // body_long) * body_long
        apple_down = (apple_x, apple_y)
        if apple_down not in snake:
            return apple_down

apple0 = apple()
running = True
game_over = False
score = 0
pygame.font.init()
font = pygame.font.Font(None, 80)
score_font = pygame.font.Font(None, 40)
text = font.render("Game Over", True, (255, 255, 255))
text_rect = text.get_rect(center=(width // 2, high // 2))

while running:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    new_head_x, new_head_y = snake[0][0] + bx, snake[0][1] + by


    if new_head_x < 0:
        new_head_x = width - body_long
    elif new_head_x > width:
        new_head_x = 0
    elif new_head_y < 0:
        new_head_y = high - body_long
    elif new_head_y > high:
        new_head_y = 0

    new_head = (new_head_x, new_head_y)

    snake.insert(0,new_head)

    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        score += 999
    if key[pygame.K_F1]:
        apple0 = apple()

    if key[pygame.K_UP] and by == 0:
        by = -body_long
        bx = 0
    elif key[pygame.K_DOWN] and by == 0:
        by = body_long
        bx = 0
    elif key[pygame.K_LEFT] and bx == 0:
        bx = -body_long
        by = 0
    elif key[pygame.K_RIGHT] and bx == 0:
        bx = body_long
        by = 0

    if new_head == apple0:
        apple0 = apple()
        score += 10
    else:
        snake.pop()
    if new_head in snake[1:]:
        game_over = True
        running = False
    screen.fill((0, 0, 0))

    for i in range(len(snake)):
        pygame.draw.rect(screen, green, (snake[i][0], snake[i][1],  body_long, body_long))
        pygame.draw.rect(screen, (0, 0, 0), (snake[0][0], snake[0][0], body_long, body_long), 2)
    pygame.draw.rect(screen, red, (apple0[0], apple0[1], body_long, body_long))
    score_text = score_font.render(f"score:{score}", True, (255, 255, 255))
    score_text_rect = score_text.get_rect(center=(width // 2, 10))
    screen.blit(score_text, score_text_rect)

    if game_over:
        screen.blit(text, text_rect)
        time.sleep(3)
    pygame.display.flip()
pygame.quit()
