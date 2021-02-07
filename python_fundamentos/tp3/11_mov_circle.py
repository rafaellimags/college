import pygame

screen = pygame.display.set_mode((400, 400))

x = 200
limit = False


def draw_circle():
    pygame.draw.circle(screen, (0, 0, 255), (x, 200), 100, 1)


clock = pygame.time.Clock()
running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if x == 300:
        limit = True

    if x == 100:
        limit = False

    if not limit:
        x += 1

    if limit:
        x -= 1

    screen.fill((0, 0, 0))
    draw_circle()
    pygame.display.update()
    clock.tick(60)
