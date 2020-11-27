import pygame
import psutil
import time

largura_tela = 800
altura_tela = 600
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()


pygame.font.init()
font = pygame.font.Font('SpaceMono-Regular.ttf', 18)

s_mem = pygame.surface.Surface((largura_tela, 70))
s_proc = pygame.surface.Surface((largura_tela, 70))
s_strg = pygame.surface.Surface((largura_tela, 70))
s_net = pygame.surface.Surface((largura_tela, 70))

ip = psutil.net_if_addrs()['Wi-Fi'][1].address
text_ip = "IP: " + ip
text_ip = font.render(text_ip, 1, branco)
s_net.blit(text_ip, (20, 0))
tela.blit(s_net, (0, 340))


def mostra_uso_memoria(position):
    mem = psutil.virtual_memory()
    s_mem.fill((0, 0, 0))
    larg = largura_tela - 2*20
    pygame.draw.rect(s_mem, azul, (20, 30, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(s_mem, vermelho, (20, 30, larg, 70))
    total = round(mem.used/(1024*1024*1024), 2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    s_mem.blit(text, (20, 0))
    tela.blit(s_mem, position)


def show_cpu_usage(position):
    cpu = psutil.cpu_percent(interval=0)
    s_proc.fill((0, 0, 0))
    larg = largura_tela - 2 * 20
    pygame.draw.rect(s_proc, azul, (20, 30, larg, 70))
    larg = larg * cpu / 100
    pygame.draw.rect(s_proc, vermelho, (20, 30, larg, 70))
    text = font.render("Uso de CPU: " + str(cpu) + "%", 1, branco)
    s_proc.blit(text, (20, 0))
    tela.blit(s_proc, position)


def show_storage_usage(position):
    disco = psutil.disk_usage('.')
    s_strg.fill((0, 0, 0))
    larg = largura_tela - 2*20
    pygame.draw.rect(s_strg, azul, (20, 30, larg, 70))
    larg = larg*disco.percent/100
    pygame.draw.rect(s_strg, vermelho, (20, 30, larg, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso total do disco: " + str(total) + "GB"
    text = font.render(texto_barra, 1, branco)
    s_strg.blit(text, (20, 0))
    tela.blit(s_strg, position)


fn_lst = [
    mostra_uso_memoria,
    show_cpu_usage,
    show_storage_usage
]

clock = pygame.time.Clock()
cont = 60
navigation = -1
terminou = False
space = False
right = False
left = False

while not terminou:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            left = True
            space = False
            cont = 60
            position = (0, 30)
            navigation -= 1
            if navigation < 0:
                navigation = 0

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            right = True
            space = False
            cont = 60
            position = (0, 30)

            navigation += 1

            if navigation > 2:
                navigation = 2

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            space = True
            cont = 60
            position = ((0, 30), (0, 120), (0, 210))
            left, right = False, False

    if space:
        if cont == 60:
            tela.fill((0, 0, 0))
            fn_lst[0](position[0])
            fn_lst[1](position[1])
            fn_lst[2](position[2])
            cont = 0

        cont = cont + 1

    if right:
        if cont == 60:
            tela.fill((0, 0, 0))
            fn_lst[navigation](position)
            cont = 0

        cont = cont + 1

    pygame.display.update()
    clock.tick(60)

pygame.display.quit()
