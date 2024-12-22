import sys
import os
import pygame
import Funcao

# Funções auxiliares
def desenhar_botao(screen, x, y, largura, altura, texto, cor, cor_hover):
    Posicao_Mouse = pygame.mouse.get_pos()
    Clique_Mouse = pygame.mouse.get_pressed()
    
    fonte_botao = pygame.font.SysFont('Arial', 20)
    texto_botao = fonte_botao.render(texto, True, (0, 0, 0))
    
    if x < Posicao_Mouse[0] < x + largura and y < Posicao_Mouse[1] < y + altura:
        pygame.draw.rect(screen, cor_hover, (x, y, largura, altura), border_radius=10)
        
        if Clique_Mouse[0]:  # Clique esquerdo
            return True
    else:
        pygame.draw.rect(screen, cor, (x, y, largura, altura), border_radius=10)

    screen.blit(texto_botao, (x + 10, y + 5))
    return False

def titulo(screen, titulo, cor_titulo):
    fonte = pygame.font.SysFont('Arial', 30)
    texto = fonte.render(titulo, True, cor_titulo)
    screen.blit(texto, (10, 10))

# Inicializando Pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MusicFlow")
icone = pygame.image.load('./LocalPlayerPy/icone/MusicFlow.ico') 
pygame.display.set_icon(icone)

# Tela
info_tela = pygame.display.Info()
SCREEN_WIDTH = int(info_tela.current_w / 2)
SCREEN_HEIGHT = int(info_tela.current_h / 1.5)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Variável para controlar as telas
tela_atual = "principal"

# Cores
COR_GRAY = (200, 200, 200)
COR_WHITE = (255, 255, 255)
COR_BLUE = (0, 0, 255)
COR_RED = (255, 0, 0)
COR_YELLOW = (255, 255, 0)
COR_CYAN = (0, 255, 255)

# Loop principal
while True:
    screen.fill(COR_GRAY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            if SCREEN_HEIGHT < 450:
                SCREEN_HEIGHT = 450
            if SCREEN_WIDTH < 300:
                SCREEN_WIDTH = 300
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    
    # Verificando qual tela exibir
    if tela_atual == "principal":
        # Tela principal
        titulo(screen, "Tela Principal", COR_WHITE)
        if desenhar_botao(screen, 60, 60, 200, 60, "Ir para Outra Tela", COR_WHITE, COR_BLUE):
            tela_atual = "outra_tela"
        
    elif tela_atual == "outra_tela":
        # Outra tela
        screen.fill(Funcao.cor('white'))
        titulo(screen, "Outra Tela", COR_YELLOW)
        if desenhar_botao(screen, 60, 60, 200, 60, "Voltar", COR_RED, COR_GRAY):
            tela_atual = "principal"
    
    pygame.display.flip()
    clock.tick(10)
