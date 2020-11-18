import pygame

screen = pygame.display.set_mode((400, 400))
x = 10
y = 10
width = 100
height = 100


def draw_sqr():
    pygame.draw.rect(screen, (0,0,255), [x, y, width, height])

running = True
clock = pygame.time.Clock()

while running:

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                x -= 1
            elif event.key == pygame.K_s:
                y += 1
            elif event.key == pygame.K_d:
                x += 1
            elif event.key == pygame.K_w:
                y -= 1

    screen.fill((0,0,0))
    draw_sqr()
    pygame.display.update()
    clock.tick(60)
