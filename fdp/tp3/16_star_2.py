import pygame


screen = pygame.display.set_mode((400, 400))
x = 10
y = 10
width = 100
height = 100
a = [25, 75]
b = [50, 10]
c = [75, 75]
d = [16.7, 25]
e = [87.5, 25]
f = [25, 75]


def draw_star():
    pygame.draw.lines(screen, (255,255,0), False,  (a, b, c, d, e, f), 2)

running = True
clock = pygame.time.Clock()

while running:

    events = pygame.event.get()

    if pygame.mouse.get_pressed()[0]:
        b = pygame.mouse.get_pos()
        a[0], a[1] = b[0] / 2, b[1] * 7.5
        c[0], c[1] = b[0] * 1.5, b[1] * 7.5
        d[0], d[1] = b[0] / 3, b[1] * 2.5
        e[0], e[1] = b[0] * 1.75, b[1] * 2.5
        f[0], f[1] = b[0] / 2, b[1] * 7.5

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        

    # screen.fill((0,0,0))
    draw_star()
    pygame.display.update()
    clock.tick(60)
