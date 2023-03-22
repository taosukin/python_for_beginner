import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇")

# Set up the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up the font
font = pygame.font.SysFont(None, 30)

# Set up the clock
clock = pygame.time.Clock()

# Set up the snake
snake_block_size = 10
snake_speed = 15
snake_list = [[window_width // 2, window_height // 2]]
snake_length = 1

# Set up the food
food_block_size = 10
food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0

# Set up the score
score = 0


def draw_snake(snake_block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_window, green, [x[0], x[1], snake_block_size, snake_block_size])


def draw_food(food_block_size, food_x, food_y):
    pygame.draw.rect(game_window, red, [food_x, food_y, food_block_size, food_block_size])


def display_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    game_window.blit(score_text, [0, 0])


# Main game loop
game_over = False
x_change = 0
y_change = snake_block_size
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_block_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_block_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_block_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_block_size
            elif event.key == pygame.K_SPACE:
                pause = True
                while pause:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pause = False
    snake_head = [snake_list[-1][0] + x_change, snake_list[-1][1] + y_change]
    if snake_head[0] >= window_width or snake_head[0] < 0 or snake_head[1] >= window_height or snake_head[1] < 0:
        game_over = True
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    for x in snake_list[:-1]:
        if x == snake_head:
            game_over = True
    draw_snake(snake_block_size, snake_list)
    draw_food(food_block_size, food_x, food_y)
    pygame.display.update()
    if snake_head[0] == food_x and snake_head[1] == food_y:
        food_x = round(random.randrange(0, window_width - food_block_size) / 10.0) * 10.0
        food_y = round(random.randrange(0, window_height - food_block_size) / 10.0) * 10.0
        snake_length += 1
        score += 10
    display_score(score)
    clock.tick(snake_speed)
pygame.quit()
quit()
