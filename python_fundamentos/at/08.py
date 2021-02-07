import pygame
import random

# pygame.surface.Surface().lock

screen = pygame.display.set_mode((400, 400))
sqr_srfc = pygame.surface.Surface((50, 50))
pygame.font.init()
text = pygame.font.SysFont('Arial', 30)
BTN_COORD = (195, 130)
pos_list = []


def draw_circle():
    # screen.fill((0, 0, 0))
    text_surface = text.render('Clique', True, (0, 255, 0))
    screen.blit(text_surface, (160, 20))
    pygame.draw.circle(screen, (255, 255, 0), BTN_COORD, 50)


def draw_sqr():
    coord = [random.randint(0, 350), random.randint(0, 350)]
    pygame.draw.rect(sqr_srfc, (255, 255, 0), (0,0,50,50))
    pos_list.append(coord)
    for sqr in pos_list:
        screen.blit(sqr_srfc, sqr)

    if len(pos_list) > 1:
        for s in range(len(pos_list) -1):
            if pos_list[s][0] - pos_list[-1][0] <= 50 and pos_list[s][1] - pos_list[-1][1] <= 50:
                pos_list.remove(pos_list[s])
                pos_list.remove(pos_list[-1])


    # for x in range(len(pos_list)-1):
    #     if pos_list[x][0]+50 >= pos_list[-1][0] and pos_list[x][1]+50 >= pos_list[-1][1]:
    #         # pos_list.remove(x)
    #         screen.fill((0,0,0))
    #         pos_list.remove(pos_list[-1])
    #         break
    #     else:
    #         print(False)

    print(pos_list)


running = True
clock = pygame.time.Clock()

while running:

    is_clicked = False

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if mouse[0] in range(145, 245):
                if mouse[1] in range(80, 180):
                    is_clicked = True


    draw_circle()
    if is_clicked:
        draw_sqr()


    pygame.display.update()
    clock.tick(60)
