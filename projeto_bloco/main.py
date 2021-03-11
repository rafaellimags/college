import platform
import pygame
import psutil
import time
import os
from ui.view import Frame, Fill
from lib.utils import sizeof_fmt


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
IP = psutil.net_if_addrs()['Wi-Fi'][1].address

surface_i = pygame.surface.Surface((largura_tela, 600))

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
fill = Fill((0, 200, 0))
FILL_COLOR = fill.get_color()
FRAME_COLOR = FRAME.get_color()
FRAME_FILLED = FRAME.get_filled()
FRAME_SIZE = FRAME.get_size()
FRAME_DENSITY = FRAME.get_density()


def network(position, show_all, net_stat):
    s_net = pygame.surface.Surface((800, 600))
    netio = psutil.net_io_counters(pernic=False, nowrap=True)
    bytes_sent = str(netio.bytes_sent)
    bytes_recvd = str(netio.bytes_recv)
    pckts_sent = str(netio.packets_sent)
    pckts_recvd = str(netio.packets_recv)
    err_in = str(netio.errin)
    err_out = str(netio.errout)
    nw_data = [IP, bytes_sent, bytes_recvd,
               pckts_sent, pckts_recvd,
               err_in, err_out]

    title_status = "Estatísticas da Rede"
    legend = ["IP", "Bytes enviados", "Bytes Recebidos", "Pacotes enviados",
              "Pacotes recebidos", "Erros recebidos", "Erros enviados"]

    y = 48
    l = 0
    for data in nw_data:
        text_data = font.render(f"{legend[l]}: {data}", 1, branco)
        if net_stat:
            title = font.render(title_status, 4, branco)
            s_net.blit(title, (320, 0))
            tela.blit(s_net, (0, 0))
            s_net.blit(text_data, (24, y))
        else:
            s_net.blit(font.render(f"IP: {IP}", 1, branco), (0, y))
            tela.blit(s_net, position)
            break

        y = y + 24
        l += 1

    s_net.fill((0, 0, 0))


def mostra_uso_memoria(position, show_all):
    s_mem = pygame.surface.Surface((largura_tela, 600))
    svmem = psutil.virtual_memory()
    larg = largura_tela - 2*22
    pygame.draw.lines(s_mem, FRAME_COLOR, FRAME_FILLED,
                      FRAME_SIZE, FRAME_DENSITY)
    larg_percent = larg*svmem.percent/100
    pygame.draw.rect(s_mem, FILL_COLOR, (24, 34, larg_percent, 31))
    used = round(svmem.used/(1024**3), 2)
    total = round(svmem.total/(1024**3), 2)
    texto_barra = "Uso total da memória" + \
        "{:>46}".format(str(used) + " / " + str(total)) + " GB"
    text = font.render(texto_barra, 1, branco)
    s_mem.blit(text, (20, 0))
    tela.blit(s_mem, position)

    if not show_all:
        s_mem.fill((0, 0, 0))
        free_fill_color = (0, 200, 0)
        free_mem = round(svmem.free/(1024**3), 2)
        total_mem = round(svmem.total/(1024**3), 2)
        free_percent = free_mem / total_mem
        larg_free = larg * free_percent
        if free_percent < 0.12:
            free_fill_color = (255, 0, 0)

        pygame.draw.lines(s_mem, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.rect(s_mem, free_fill_color, (24, 34, larg_free, 31))

        text_free = round(svmem.free/(1024**3), 2)
        texto_barra = "Memória livre" + "{:>53}".format(str(text_free)) + " GB"
        text = font.render(texto_barra, 1, branco)
        s_mem.blit(text, (20, 0))
        tela.blit(s_mem, (0, 120))

    s_mem.fill((0, 0, 0))


def show_cpu_usage(position, show_all):
    s_proc0 = pygame.surface.Surface((largura_tela, 70))
    s_proc1 = pygame.surface.Surface((largura_tela, 70))
    s_proc2 = pygame.surface.Surface((largura_tela, 70))
    s_proc3 = pygame.surface.Surface((largura_tela, 70))
    s_proc4 = pygame.surface.Surface((largura_tela, 70))
    s_proc_info = pygame.surface.Surface((largura_tela, 180))
    if show_all:
        cpu_total = psutil.cpu_percent(interval=0, percpu=False)
        s_proc0.fill((0, 0, 0))
        larg = largura_tela - 2 * 22
        pygame.draw.lines(s_proc0, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        larg = larg * cpu_total / 100
        pygame.draw.rect(s_proc0, FILL_COLOR, (24, 34, larg, 31))
        text = font.render(
            "Uso da CPU" + "{:>58}".format(str(cpu_total)) + "%", 1, branco)
        s_proc0.blit(text, (20, 0))
        tela.blit(s_proc0, position)
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
        s_proc_info.fill((0, 0, 0))
        larg = largura_tela - 2 * 22
        pygame.draw.lines(s_proc1, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc2, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc3, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        pygame.draw.lines(s_proc4, FRAME_COLOR, FRAME_FILLED,
                          FRAME_SIZE, FRAME_DENSITY)
        larg1 = larg * cpu[0] / 100
        larg2 = larg * cpu[1] / 100
        larg3 = larg * cpu[2] / 100
        larg4 = larg * cpu[3] / 100
        pygame.draw.rect(s_proc1, FILL_COLOR, (24, 34, larg1, 31))
        pygame.draw.rect(s_proc2, FILL_COLOR, (24, 34, larg2, 31))
        pygame.draw.rect(s_proc3, FILL_COLOR, (24, 34, larg3, 31))
        pygame.draw.rect(s_proc4, FILL_COLOR, (24, 34, larg4, 31))
        pygame.draw.line(tela, (80, 80, 80), (20, 400), (768, 400), width=1)
        text1 = font.render(
            "Núcleo 1 " + "{:>58}".format(str(cpu[0])) + "%", 1, branco)
        text2 = font.render(
            "Núcleo 2 " + "{:>58}".format(str(cpu[1])) + "%", 1, branco)
        text3 = font.render(
            "Núcleo 3 " + "{:>58}".format(str(cpu[2])) + "%", 1, branco)
        text4 = font.render(
            "Núcleo 4 " + "{:>58}".format(str(cpu[3])) + "%", 1, branco)
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
    s_strg = pygame.surface.Surface((largura_tela, 600))
    disco = psutil.disk_usage('.')
    s_strg.fill((0, 0, 0))
    larg = largura_tela - 2*22
    pygame.draw.lines(s_strg, FRAME_COLOR, FRAME_FILLED,
                      FRAME_SIZE, FRAME_DENSITY)
    larg = larg*disco.percent/100
    pygame.draw.rect(s_strg, FILL_COLOR, (24, 34, larg, 31))
    total = round(disco.total/(1024*1024*1024), 2)
    usado = round(disco.used/(1024*1024*1024), 2)
    texto_barra = "Uso total do disco: " + \
        "{:>46}".format(str(usado) + " / " + str(total)) + " GB"
    text = font.render(texto_barra, 1, branco)
    s_strg.blit(text, (20, 0))
    tela.blit(s_strg, position)

    disk_part = psutil.disk_partitions(all=False)[0]._asdict()
    io_counters = psutil.disk_io_counters()._asdict()

    y_pos = 0

    # Render disk text info
    if not show_all:
        for key_p, value_p in disk_part.items():
            info = font.render(f"{key_p}: {value_p}", 1, branco)
            surface_i.blit(info, (24, y_pos))
            tela.blit(surface_i, (0, 120))
            y_pos += 22

        y_pos = -8

        for key_c, value_c in io_counters.items():
            if key_c == "read_time" or  key_c == "write_time":                
                info = font.render(f"{key_c}: {value_c / 1000}sec", 1, branco)
            elif key_c == "read_bytes" or key_c == "write_bytes":
                info = font.render(f"{key_c}: {sizeof_fmt(value_c)}", 1, branco)
            else:
                info = font.render(f"{key_c}: {value_c}", 1, branco)
            surface_i.blit(info, (224, y_pos))
            tela.blit(surface_i, (0, 120))
            y_pos += 22

    surface_i.fill((0,0,0))
    


def show_process_info(pos, show_all):
    # surface = pygame.surface.Surface((largura_tela, 600))
    p = psutil.Process(psutil.Process().pid)

    process = {
        "Name" : p.name()[:9],
        "Threads" : p.num_threads(),
        "Creation" : time.ctime(p.create_time()),
        "Sys time" : p.cpu_times().system,
        "Usr time" : p.cpu_times().user,
        "Mem Usage" : p.memory_percent(),
        "CPU Usage" : p.cpu_percent(),
        "VMS" : p.memory_info().vms / 1024 / 1024,
        "Exe" : p.exe()[-13:]
    }

    y_pos = 0

    for item in process:
        info = font.render(f"{item}: {process[item]}", 1, branco)
        surface_i.blit(info, (24, y_pos))
        tela.blit(surface_i, pos)
        y_pos += 22

    surface_i.fill((0,0,0))


fn_lst = [
    mostra_uso_memoria,
    show_cpu_usage,
    show_storage_usage,
    network,
    show_process_info,
]

clock = pygame.time.Clock()
cont = 60
navigation = -1
terminou = False
show_all = True
show_init = True
right = False
left = False
position = ((0, 30), (0, 120), (0, 210), (24, 320), (0, 320))

# Navigation keys
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

            if navigation > 3:
                navigation = 3

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            show_all = True
            cont = 60
            left, right, show_init = False, False, False

    if show_all or show_init:
        if cont == 60:
            net_stat = False
            fn_lst[0](position[0], show_all)
            fn_lst[1](position[1], show_all)
            fn_lst[2](position[2], show_all)
            fn_lst[3](position[3], show_all, net_stat)
            fn_lst[4](position[4], show_all)
            cont = 0

        cont = cont + 1

    if right:
        if cont == 60:
            tela.fill((0, 0, 0))
            if fn_lst[navigation] == network:
                net_stat = True
                fn_lst[navigation](position[navigation], show_all, net_stat)
            else:
                fn_lst[navigation](position[0], show_all)

            cont = 0

        cont = cont + 1

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
