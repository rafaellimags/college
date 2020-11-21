import pygame

screen = pygame.display.set_mode((400, 400))

def draw_circle():
    pygame.draw.circle(screen, (0,0,255), (200,200),100,1)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_circle()
    pygame.display.update()

