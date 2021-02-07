import pygame
import random

screen = pygame.display.set_mode((400, 400))
x = round(random.randint(0, 350))
y = round(random.randint(0, 350))
width = 50
height = 50


def draw_sqr():
    pygame.draw.rect(screen, (255, 255, 0), [x, y, width, height])


running = True
clock = pygame.time.Clock()

while running:

    events = pygame.event.get()

    if pygame.mouse.get_pressed()[0]:
        pos = pygame.mouse.get_pos()
        x = pos[0] - 50
        y = pos[1] - 50

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = round(random.randint(0, 350))
                y = round(random.randint(0, 350))
                print(x, y)

    screen.fill((0, 0, 0))
    draw_sqr()
    pygame.display.update()
    clock.tick(60)
