import pygame
import psutil

largura_tela = 800
altura_tela = 600
preto = (0,0,0)
branco = (255,255,255)
azul = (0,0,255)
vermelho = (255,0,0)
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Uso de memória")
pygame.display.init()


pygame.font.init()
font = pygame.font.Font(None, 22)

s_mem = pygame.surface.Surface((largura_tela, 70))
s_proc = pygame.surface.Surface((largura_tela, 70))
s_strg = pygame.surface.Surface((largura_tela, 70))
s_net = pygame.surface.Surface((largura_tela, 70))

ip = psutil.net_if_addrs()['Wi-Fi'][1].address
text_ip = "IP: " + ip
text_ip = font.render(text_ip, 1, branco)
s_net.blit(text_ip, (20, 0))
tela.blit(s_net, (0, 340))

    


def mostra_uso_memoria():
    mem = psutil.virtual_memory()
    larg = largura_tela - 2*20
    pygame.draw.rect(s_mem, azul, (20, 30, larg, 70))
    larg = larg*mem.percent/100
    pygame.draw.rect(s_mem, vermelho, (20, 30, larg, 70))
    total = round(mem.total/(1024*1024*1024),2)
    texto_barra = "Uso de Memória (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    s_mem.blit(text, (20, 0))
    tela.blit(s_mem, (0, 30))


def show_cpu_usage():
    cpu = psutil.cpu_percent(interval=0)
    larg = largura_tela - 2 * 20
    pygame.draw.rect(s_proc, azul, (20, 30, larg, 70))
    larg = larg * cpu / 100
    pygame.draw.rect(s_proc, vermelho, (20, 30, larg, 70))
    text = font.render("Uso de CPU:", 1, branco)
    s_proc.blit(text, (20, 0))
    tela.blit(s_proc, (0, 130))

def show_storage_usage():
    disco = psutil.disk_usage('.')
    larg = largura_tela - 2*20
    pygame.draw.rect(s_strg, azul, (20, 30, larg, 70))
    larg = larg*disco.percent/100
    pygame.draw.rect(s_strg, vermelho, (20, 30, larg, 70))
    total = round(disco.total/(1024*1024*1024), 2)
    texto_barra = "Uso de Disco: (Total: " + str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    s_strg.blit(text, (20, 0))
    tela.blit(s_strg, (0, 230))

clock = pygame.time.Clock()
cont = 60
terminou = False
while not terminou:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    if cont == 60:
        mostra_uso_memoria()
        show_cpu_usage()
        show_storage_usage()
        cont = 0

    pygame.display.update()
    
    clock.tick(60)

    cont = cont + 1
pygame.display.quit()
