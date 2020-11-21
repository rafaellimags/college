import pygame

screen = pygame.display.set_mode((400, 400))

x = 200
y = 200
limitX = False
limitY = False
movX = True
movY = False


def draw_circle():
    pygame.draw.circle(screen, (255, 255, 0), (x, y), 100, 1)


clock = pygame.time.Clock()
running = True

while running:

    if x == 300:
        limitX = True

    if x == 100:
        limitX = False

    if y == 300:
        limitY = True

    if y == 100:
        limitY = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                limitX = True
                movY = False
                movX = True
            elif event.key == pygame.K_s:
                limitY = False
                movX = False
                movY = True
            elif event.key == pygame.K_d:
                limitX = False
                movY = False
                movX = True
            elif event.key == pygame.K_w:
                limitY = True
                movX = False
                movY = True

    if movX and not limitX:
        x += 1

    if movX and limitX:
        x -= 1

    if movY and not limitY:
        y += 1

    if movY and limitY:
        y -= 1

    screen.fill((0, 0, 0))
    draw_circle()
    pygame.display.update()
    clock.tick(60)
