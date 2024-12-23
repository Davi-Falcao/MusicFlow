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
    Redmensionavel = pygame.RESIZABLE if redimensionavel else 0
    screen = pygame.display.set_mode((largura, altura), Redmensionavel)


Funcao_Listar_Diretorio = Funcao.listar_conteudo(pasta_Musica)[0]
pasta_selecionada = ''



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

    screen.fill(Funcao.cor('grey'))

    if tela_principal == 'principal':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        if Funcao.desenhar_botao(screen, 20, 100, texto="Pastas", cor='white', cor_hover='blue'):    
            tela_principal = 'pasta'    
        if Funcao.desenhar_botao(screen, 20, 170, texto="Music", cor='white', cor_hover='blue'):
            tela_principal = 'musica'
    
    elif tela_principal == 'pasta':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        y_pos = 100  # Posição inicial no eixo Y
        for pasta in Funcao_Listar_Diretorio:
            if Funcao.desenhar_botao(screen, 20, y_pos, texto=pasta, cor='white', cor_hover='blue'):
                pasta_selecionada = pasta
                tela_principal = 'Playlist'
            y_pos += 70  # Ajuste o espaçamento entre os botões
    
    elif tela_principal == 'musica':    
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
    
    elif tela_principal == 'Playlist':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
                tela_principal = 'principal'
        if pasta_selecionada:
            Funcao_Listar_Musica = Funcao.listar_conteudo(f'{pasta_Musica}\\{pasta_selecionada}')[1]
            y_pos = 100
            for musica in Funcao_Listar_Musica:
                if Funcao.desenhar_botao(screen, 20, y_pos, texto=musica, cor='white', cor_hover='blue'):
                    tela_principal = 'musica'
                    Funcao.tocar_musica((f'{pasta_Musica}\\{pasta_selecionada}\\{musica}'))
                y_pos += 70          
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
    clock.tick(13)