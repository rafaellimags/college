import pygame
import psutil
import time

largura_tela = 800
altura_tela = 600
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()


class Frame:

    def __init__(self, color=(0, 0, 0), filled=False, size=None, density=0):
        self.__color = color
        self.__filled = filled
        self.__size = size
        self.__density = density

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_filled(self, filled):
        self.__filled = filled

    def get_filled(self):
        return self.__filled

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_density(self, density):
        self.__density = density

    def get_density(self):
        return self.__density


FRAME = Frame(
    (255, 255, 255),
    False,
    ((20, 30), (780, 30), (780, 68), (20, 68), (20, 30)),
    1
)

FRAME_INFO = Frame(
    (255, 255, 255),
    False,
    ((20, 320), (780, 320), (780, 580), (20, 580), (20, 320)),
    1
)


INFO_SIZE = FRAME_INFO.get_size()
INFO_BORDER_COLOR = FRAME_INFO.get_color()
INFO_DESITY = FRAME_INFO.get_density()
INFO_FILL = FRAME_INFO.get_filled()

print(INFO_SIZE)
print(INFO_BORDER_COLOR)
print(INFO_DESITY)
print(INFO_FILL)


class Fill(object):

    def __init__(self, color=(0, 0, 0), size=None):
        self.__color = color
        self.__size = size

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size


fill = Fill((0, 255, 0))

FILL_COLOR = fill.get_color()

FRAME_COLOR = FRAME.get_color()
FRAME_FILLED = FRAME.get_filled()
FRAME_SIZE = FRAME.get_size()
FRAME_DENSITY = FRAME.get_density()

pygame.font.init()
font = pygame.font.Font('SpaceMono-Regular.ttf', 18)

s_mem = pygame.surface.Surface((largura_tela, 70))
s_proc = pygame.surface.Surface((largura_tela, 70))
s_strg = pygame.surface.Surface((largura_tela, 70))
s_net = pygame.surface.Surface((largura_tela, 70))
s_info = pygame.surface.Surface((largura_tela, 280))


def network(position):
    ip = psutil.net_if_addrs()['Wi-Fi'][1].address
    s_net.fill((0, 0, 0))
    text_ip = "IP: " + ip
    text_ip = font.render(text_ip, 1, branco)
    s_net.blit(text_ip, (20, 0))
    tela.blit(s_net, (0, 280))


def mostra_uso_memoria(position):
    mem = psutil.virtual_memory()
    s_mem.fill((0, 0, 0))
    larg = largura_tela - 2*22
    pygame.draw.lines(s_mem, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
    larg = larg*mem.percent/100
    pygame.draw.rect(s_mem, FILL_COLOR, (24, 34, larg, 31))
    total = round(mem.used/(1024*1024*1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    s_mem.blit(text, (20, 0))
    tela.blit(s_mem, position)


def show_cpu_usage(position):
    cpu = psutil.cpu_percent(interval=0)
    s_proc.fill((0, 0, 0))
    larg = largura_tela - 2 * 22
    pygame.draw.lines(s_proc, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
    larg = larg * cpu / 100
    pygame.draw.rect(s_proc, FILL_COLOR, (24, 34, larg, 31))
    text = font.render("Uso de CPU: " + str(cpu) + "%", 1, branco)
    s_proc.blit(text, (20, 0))
    tela.blit(s_proc, position)


def show_storage_usage(position):
    disco = psutil.disk_usage('.')
    s_strg.fill((0, 0, 0))
    larg = largura_tela - 2*22
    pygame.draw.lines(s_strg, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
    larg = larg*disco.percent/100
    pygame.draw.rect(s_strg, FILL_COLOR, (24, 34, larg, 31))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso total do disco: " + str(total) + "GB"
    text = font.render(texto_barra, 1, branco)
    s_strg.blit(text, (20, 0))
    tela.blit(s_strg, position)


def aditional_info(position):
    s_info.fill((0, 0, 0))
    pygame.draw.lines(s_info, INFO_BORDER_COLOR, INFO_FILL, ((20, 0), (780, 0), (780, 278), (20, 278), (20, 0)), INFO_DESITY)
    tela.blit(s_info, position)


fn_lst = [
    mostra_uso_memoria,
    show_cpu_usage,
    show_storage_usage,
    # network,
    aditional_info
]

clock = pygame.time.Clock()
cont = 60
navigation = -1
terminou = False
show_all = False
show_init = True
right = False
left = False
position = ((0, 30), (0, 120), (0, 210), (0, 300))


while not terminou:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
            show_all = False
            show_init = False
            cont = 60
            navigation -= 1
            if navigation < 0:
                navigation = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
            show_all = False
            show_init = False
            cont = 60

            navigation += 1

            if navigation > 2:
                navigation = 2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            show_all = True
            cont = 60
            left, right, show_init=False, False, False

    if show_all or show_init:
        if cont == 60:
            fn_lst[0](position[0])
            fn_lst[1](position[1])
            fn_lst[2](position[2])
            # fn_lst[3](position[3])
            fn_lst[3](position[3])
            cont = 0

        cont = cont + 1

    if right:
        if cont == 60:
            tela.fill((0, 0, 0))
            fn_lst[navigation](position[0])
            cont = 0

        cont = cont + 1

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
