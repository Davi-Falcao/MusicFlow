import sys
import os
import pygame
import Funcao

user_home_directory = os.path.expanduser("~")
pasta_Musica = f'{user_home_directory}\\Music\\'

# Inicializando Pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MusicFlow")
icone = pygame.image.load('.\\LocalPlayerPy\\icone\\MusicFlow.ico') 
pygame.display.set_icon(icone)

# Tela
info_tela = pygame.display.Info()
SCREEN_WIDTH = int(1920/ 2)
SCREEN_HEIGHT = int(1080 / 1.5)
MUSIC_SCREEN_WIDTH = 300
MUSIC_SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Variáveis
fonte = "Impact"
fonte_titulo = pygame.font.SysFont(fonte, 30)
tela_principal = 'principal'

# Função para ajustar o tamanho da tela
def ajustar_tamanho_tela(largura, altura, redimensionavel=True):
    global screen
    flags = pygame.RESIZABLE if redimensionavel else 0
    screen = pygame.display.set_mode((largura, altura), flags)

while True:
    # Ajustar o tamanho da tela com base na tela atual
    if tela_principal == 'musica':
        if screen.get_width() != MUSIC_SCREEN_WIDTH or screen.get_height() != MUSIC_SCREEN_HEIGHT:
            ajustar_tamanho_tela(MUSIC_SCREEN_WIDTH, MUSIC_SCREEN_HEIGHT, redimensionavel=False)
    elif tela_principal in ['principal', 'botao']:
        if screen.get_width() != SCREEN_WIDTH or screen.get_height() != SCREEN_HEIGHT:
            SCREEN_WIDTH = int(1920/ 2)
            SCREEN_HEIGHT = int(1080 / 1.5)
            ajustar_tamanho_tela(SCREEN_WIDTH, SCREEN_HEIGHT, redimensionavel=True)

    # Preencher o fundo
    screen.fill(Funcao.cor('grey'))

    if tela_principal == 'principal':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        if Funcao.desenhar_botao(screen, 20, 100, texto="Botao", cor='white', cor_hover='blue'):    
            tela_principal = 'botao'    
        if Funcao.desenhar_botao(screen, 20, 170, texto="Music", cor='white', cor_hover='blue'):
            tela_principal = 'musica'
    
    elif tela_principal == 'botao':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        if Funcao.desenhar_botao(screen, 20, 100, texto="Clique Aqui", cor='white', cor_hover='blue'):
            print('botão clicado')
    
    elif tela_principal == 'musica':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.VIDEORESIZE and tela_principal in ['principal', 'botao']:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            if SCREEN_HEIGHT < 450:
                SCREEN_HEIGHT = 450
            if SCREEN_WIDTH < 300:
                SCREEN_WIDTH = 300
            ajustar_tamanho_tela(SCREEN_WIDTH, SCREEN_HEIGHT, redimensionavel=True)

    pygame.display.flip()
    clock.tick(30)