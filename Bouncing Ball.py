import pygame
from collections import namedtuple
from random import randint

Colour = namedtuple("Colour", ["red", "green", "blue"])

BACKGROUND_COLOUR = Colour(red=36, green=188, blue=118)
BALL_COLOUR = Colour(red=235, green=210, blue=65)

BALL_RADIUS = 30

pygame.init()

pygame.display.set_caption("Bouncing Ball")

clock = pygame.time.Clock()
screen = pygame.display.set_mode([640, 480])


def main():
    ball_position = [(screen.get_width() // 2), (screen.get_height() // 2)]
    ball_velocity = [randint(-5, 5), randint(-5, 5)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(BACKGROUND_COLOUR)
        pygame.draw.circle(screen, BALL_COLOUR, ball_position, BALL_RADIUS)
        pygame.display.update()

        if ball_position[0] - BALL_RADIUS < 0:
            ball_velocity[0] = -ball_velocity[0]
        elif ball_position[0] + BALL_RADIUS > screen.get_width():
            ball_velocity[0] = -ball_velocity[0]

            # Check for top and bottom collisions
        if ball_position[1] - BALL_RADIUS < 0:
            ball_velocity[1] = -ball_velocity[1]
        elif ball_position[1] + BALL_RADIUS > screen.get_height():
            ball_velocity[1] = -ball_velocity[1]

        ball_position[0] += ball_velocity[0]
        ball_position[1] += ball_velocity[1]

        clock.tick(60)


main()
