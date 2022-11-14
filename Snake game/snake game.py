import pygame
import sys
import time
import colours
from random import randint
segment_size = 20

window_height = 400
window_weight = 720
window_dimensions = window_weight, window_height

Img_body = pygame.transform.scale(pygame.image.load('body.jpg'), (segment_size, segment_size))
Img_head = pygame.transform.scale(pygame.image.load('head.jpg'), (segment_size, segment_size))
Img_food = pygame.transform.scale(pygame.image.load('covid.png'), (segment_size, segment_size))

pygame.init()
pygame.display.set_caption("Snake game")

screen = pygame.display.set_mode(window_dimensions)
clock = pygame.time.Clock()


def draw_object(snake_positions, food_position):
    for position in snake_positions:
        screen.blit(Img_body, pygame.Rect(position[0], position[1], segment_size, segment_size))

    screen.blit(Img_head, pygame.Rect(snake_positions[0][0], snake_positions[0][1], segment_size, segment_size))
    screen.blit(Img_food, pygame.Rect(food_position[0], food_position[1], segment_size, segment_size))


def set_new_position(snake_positions):
    while True:
        x_position = randint(0, 36) * segment_size
        y_position = randint(1, 20) * segment_size
        food_position = (x_position, y_position)

        if food_position not in snake_positions:
            return food_position


def move_snake(snake_positions, direction):
    head_x_positions, head_y_positions = snake_positions[0]

    if direction == "Left":
        new_head_positions = (head_x_positions - segment_size, head_y_positions)
    elif direction == "Right":
        new_head_positions = (head_x_positions + segment_size, head_y_positions)
    elif direction == "Down":
        new_head_positions = (head_x_positions, head_y_positions + segment_size)
    elif direction == "Up":
        new_head_positions = (head_x_positions, head_y_positions - segment_size)

    snake_positions.insert(0, new_head_positions)
    del snake_positions[-1]


def on_key_press(event, current_direction):
    new_direction = "Right"
    if event.key == pygame.K_RIGHT:
        new_direction = "Right"
    if event.key == pygame.K_LEFT:
        new_direction = "Left"
    if event.key == pygame.K_UP:
        new_direction = "Up"
    if event.key == pygame.K_DOWN:
        new_direction = "Down"

    all_direction = ("Up", "Down", "Left", "Right")
    opposites = ({"Up", "Down"}, {"Left", "Right"})
    if new_direction in all_direction and {new_direction, current_direction} not in opposites:
        return new_direction
    return current_direction


def check_collisions(snake_positions):
    head_x_positions, head_y_positions = snake_positions[0]
    return (
           head_x_positions in (0, window_weight)
           or head_y_positions in (0, window_height)
           or (head_x_positions, head_y_positions) in snake_positions[1:]
    )


def check_food_collisions(snake_positions, food_positions):
    if snake_positions[0] == food_positions:
        snake_positions.append(snake_positions[-1])
        return True


def game_over():
    font = pygame.font.Font(None, 40)
    text = font.render('Game over!', True, colours.quit_colour)
    position = text.get_rect()
    position.midtop = (360,150)
    screen.blit(text, position)

    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    sys.exit()


def show_score(score):
    font = pygame.font.Font(None, 28)
    text = font.render(f"Score:{score}", True, colours.text_colour)
    screen.blit(text, (10, 10))


def play_game():
    snake_positions = [(100, 100), (80, 100), (60, 100)]
    food_positions = set_new_position(snake_positions)

    score = 0
    current_direction = "Right"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                current_direction = on_key_press(event, current_direction)

        screen.fill(colours.background_colour)

        show_score(score)

        move_snake(snake_positions, current_direction)

        draw_object(snake_positions, food_positions)

        pygame.display.update()

        if check_collisions(snake_positions):
            game_over()

        if check_food_collisions(snake_positions, food_positions):
            food_positions = set_new_position(snake_positions)
            score += 1

        clock.tick(10)


play_game()

