import pygame


screen = pygame.display.set_mode((400, 400))
x = 10
y = 10
width = 100
height = 100


def draw_star():
    pygame.draw.lines(screen, (255,255,0), False,  ((100, 300), (200, 20), (300, 300), (50, 100), (350, 100), (100, 300)), 2)

running = True
clock = pygame.time.Clock()

while running:

    events = pygame.event.get()    

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        

    screen.fill((0,0,0))
    draw_star()
    pygame.display.update()
    clock.tick(60)
