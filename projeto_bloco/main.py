import pygame
import psutil
import time
import platform
from ui.view import Frame, Fill

largura_tela = 800
altura_tela = 600
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
pygame.display.init()
pygame.font.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Monitor de Recursos")
font = pygame.font.Font('SpaceMono-Regular.ttf', 18)

# container borders
FRAME = Frame(
    (255, 255, 255),
    False,
    ((20, 30), (780, 30), (780, 68), (20, 68), (20, 30)),
    1
)

# resource information above each container
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

# rousource bar color
fill = Fill((0, 255, 0))
FILL_COLOR = fill.get_color()
FRAME_COLOR = FRAME.get_color()
FRAME_FILLED = FRAME.get_filled()
FRAME_SIZE = FRAME.get_size()
FRAME_DENSITY = FRAME.get_density()

s_mem = pygame.surface.Surface((largura_tela, 70))
s_proc = pygame.surface.Surface((largura_tela, 70))
s_proc1 = pygame.surface.Surface((largura_tela, 70))
s_proc2 = pygame.surface.Surface((largura_tela, 70))
s_proc3 = pygame.surface.Surface((largura_tela, 70))
s_proc4 = pygame.surface.Surface((largura_tela, 70))
s_proc_info = pygame.surface.Surface((largura_tela, 180))
s_strg = pygame.surface.Surface((largura_tela, 70))
s_net = pygame.surface.Surface((largura_tela, 70))
s_info = pygame.surface.Surface((largura_tela, 280))


def network(position, show_all):
    ip = psutil.net_if_addrs()['Wi-Fi'][1].address
    s_net.fill((0, 0, 0))
    text_ip = "IP: " + ip
    text_ip = font.render(text_ip, 1, branco)
    s_net.blit(text_ip, (20, 0))
    tela.blit(s_net, (0, 280))


def mostra_uso_memoria(position, show_all):
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


def show_cpu_usage(position, show_all):
    if show_all:
        cpu_total = psutil.cpu_percent(interval=0, percpu=False)
        s_proc.fill((0, 0, 0))
        larg = largura_tela - 2 * 22
        pygame.draw.lines(s_proc, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
        larg = larg * cpu_total / 100
        pygame.draw.rect(s_proc, FILL_COLOR, (24, 34, larg, 31))
        text = font.render("Uso " + "{:>59}".format(str(cpu_total)) + "%", 1, branco)
        s_proc.blit(text, (20, 0))
        tela.blit(s_proc, position)
    else:
        cpu = psutil.cpu_percent(interval=0, percpu=True)
        arch = platform.architecture()[0]
        proc = platform.processor()
        cores = psutil.cpu_count(logical=False)
        threads = psutil.cpu_count(logical=True)
        s_proc1.fill((0, 0, 0))
        s_proc2.fill((0, 0, 0))
        s_proc3.fill((0, 0, 0))
        s_proc4.fill((0, 0, 0))
        s_proc_info.fill((0,0,0))
        larg = largura_tela - 2 * 22
        pygame.draw.lines(s_proc1, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc2, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc3, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc4, FRAME_COLOR, FRAME_FILLED, FRAME_SIZE, FRAME_DENSITY)
        larg1 = larg * cpu[0] / 100
        larg2 = larg * cpu[1] / 100
        larg3 = larg * cpu[2] / 100
        larg4 = larg * cpu[3] / 100
        pygame.draw.rect(s_proc1, FILL_COLOR, (24, 34, larg1, 31))
        pygame.draw.rect(s_proc2, FILL_COLOR, (24, 34, larg2, 31))
        pygame.draw.rect(s_proc3, FILL_COLOR, (24, 34, larg3, 31))
        pygame.draw.rect(s_proc4, FILL_COLOR, (24, 34, larg4, 31))
        pygame.draw.line(tela, (80,80,80), (20, 400), (768, 400), width=1)
        text1 = font.render("Núcleo 1 " + "{:>59}".format(str(cpu[0])) + "%", 1, branco)
        text2 = font.render("Núcleo 2 " + "{:>59}".format(str(cpu[1])) + "%", 1, branco)
        text3 = font.render("Núcleo 3 " + "{:>59}".format(str(cpu[2])) + "%", 1, branco)
        text4 = font.render("Núcleo 4 " + "{:>59}".format(str(cpu[3])) + "%", 1, branco)
        text5 = font.render(f"Arquitetura {arch}", 1, branco)
        text6 = font.render(f"Arquitetura {proc}", 1, branco)
        text7 = font.render(f"Núcleos {cores}", 1, branco)
        text8 = font.render(f"Threads {threads}", 1, branco)

        s_proc1.blit(text1, (20, 0))
        tela.blit(s_proc1, (0, 30))

        s_proc2.blit(text2, (20, 0))
        tela.blit(s_proc2, (0, 120))

        s_proc3.blit(text3, (20, 0))
        tela.blit(s_proc3, (0, 210))

        s_proc4.blit(text4, (20, 0))
        tela.blit(s_proc4, (0, 300))

        s_proc_info.blit(text5, (20, 0))
        s_proc_info.blit(text6, (20, 20))
        s_proc_info.blit(text7, (20, 40))
        s_proc_info.blit(text8, (20, 60))
        tela.blit(s_proc_info, (0, 420))


def show_storage_usage(position, show_all):
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


def aditional_info(position, show_all):
    s_info.fill((0, 0, 0))
    pygame.draw.lines(s_info, INFO_BORDER_COLOR, INFO_FILL, ((20, 0), (780, 0), (780, 278), (20, 278), (20, 0)), INFO_DESITY)
    tela.blit(s_info, position)


fn_lst = [
    mostra_uso_memoria,
    show_cpu_usage,
    show_storage_usage,
    aditional_info
]

clock = pygame.time.Clock()
cont = 60
navigation = -1
terminou = False
show_all = True
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
            fn_lst[0](position[0], show_all)
            fn_lst[1](position[1], show_all)
            fn_lst[2](position[2], show_all)
            fn_lst[3](position[3], show_all)
            cont = 0

        cont = cont + 1

    if right:
        if cont == 60:
            tela.fill((0, 0, 0))
            fn_lst[navigation](position[0], show_all)
            cont = 0

        cont = cont + 1

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
