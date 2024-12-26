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
SCREEN_WIDTH = int(1920 / 2)
SCREEN_HEIGHT = int(1080 / 1.5)
MUSIC_SCREEN_WIDTH = 300
MUSIC_SCREEN_HEIGHT = 450
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

# Variáveis
fonte = "Impact"
fonte_titulo = pygame.font.SysFont(fonte, 30)
tela_principal = 'principal'

# Variável para controlar o scroll
scroll_offset = 0
scroll_speed = 20  # Velocidade do scroll
scroll_limit = 0  # Limite do scroll para impedir sair da área visível

# Definindo uma área específica para o conteúdo rolável (ex: 300x400 px)
SCROLL_AREA_WIDTH = SCREEN_WIDTH
SCROLL_AREA_HEIGHT = SCREEN_HEIGHT - 150
scroll_area = pygame.Rect(50, 100, SCROLL_AREA_WIDTH, SCROLL_AREA_HEIGHT)

# Função para ajustar o tamanho da tela
def ajustar_tamanho_tela(largura, altura, redimensionavel=True):
    global screen
    Redmensionavel = pygame.RESIZABLE if redimensionavel else 0
    screen = pygame.display.set_mode((largura, altura), Redmensionavel)

Funcao_Listar_Diretorio = Funcao.listar_conteudo(pasta_Musica)[0]
pasta_selecionada = ''

# Função para calcular o limite de scroll
def calcular_scroll_limite(itens, item_altura, altura_area):
    total_altura = len(itens) * item_altura
    return min(0, altura_area - total_altura)

while True:
    screen.fill(Funcao.cor('grey'))

    if tela_principal == 'musica':
        if screen.get_width() != MUSIC_SCREEN_WIDTH or screen.get_height() != MUSIC_SCREEN_HEIGHT:
            ajustar_tamanho_tela(MUSIC_SCREEN_WIDTH, MUSIC_SCREEN_HEIGHT, redimensionavel=False)
    elif tela_principal in ['principal', 'botao']:
        if screen.get_width() != SCREEN_WIDTH or screen.get_height() != SCREEN_HEIGHT:
            SCREEN_WIDTH = int(1920 / 2)
            SCREEN_HEIGHT = int(1080 / 1.5)
            ajustar_tamanho_tela(SCREEN_WIDTH, SCREEN_HEIGHT, redimensionavel=True)

    if tela_principal == 'principal':
        # Desenhar os elementos fixos primeiro (que vão ficar na frente do conteúdo rolável)
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        if Funcao.desenhar_botao(screen, 20, 100, texto="Pastas", cor='white', cor_hover='blue'):
            tela_principal = 'pasta'    
        if Funcao.desenhar_botao(screen, 20, 170, texto="Music", cor='white', cor_hover='blue'):
            tela_principal = 'musica'

    elif tela_principal == 'pasta':
        # Desenhar o botão de voltar para a tela principal
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        
        # Calculando o limite do scroll
        scroll_limit = calcular_scroll_limite(Funcao_Listar_Diretorio, 70, SCROLL_AREA_HEIGHT)

        # Garantir que o scroll_offset não seja maior que 0 (para evitar espaço vazio no topo)
        scroll_offset = min(scroll_offset, 0)

        # Criar uma superfície para desenhar os itens de rolagem
        scroll_surface = pygame.Surface((SCROLL_AREA_WIDTH, SCROLL_AREA_HEIGHT))

        # Preencher a superfície com uma cor de fundo (opcional)
        scroll_surface.fill(Funcao.cor('lightgray'))

        # Aplicar o offset de scroll e desenhar os itens na superfície
        y_pos = scroll_offset  # Aplicando o offset de scroll

        for pasta in Funcao_Listar_Diretorio:
            if Funcao.desenhar_botao(scroll_surface, 20, y_pos, texto=pasta, cor='white', cor_hover='blue', offset_x=scroll_area.x, offset_y=scroll_area.y):
                pasta_selecionada = pasta
                tela_principal = 'Playlist'
            y_pos += 70  # Ajuste o espaçamento entre os botões

        # Desenhar a superfície dentro da área de rolagem
        screen.blit(scroll_surface, (scroll_area.x, scroll_area.y))

    elif tela_principal == 'musica':    
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
    
    elif tela_principal == 'Playlist':
        if Funcao.desenhar_botao(screen, 20, 30, texto="MusicFlow", cor='white', cor_hover='blue'):
            tela_principal = 'principal'
        if pasta_selecionada:
            Funcao_Listar_Musica = Funcao.listar_conteudo(f'{pasta_Musica}\\{pasta_selecionada}')[1]
            
            # Calculando o limite do scroll para músicas
            scroll_limit = calcular_scroll_limite(Funcao_Listar_Musica, 70, SCROLL_AREA_HEIGHT)

            # Garantir que o scroll_offset não seja maior que 0 (para evitar espaço vazio no topo)
            scroll_offset = min(scroll_offset, 0)

            # Criar uma superfície para desenhar os itens de rolagem
            scroll_surface = pygame.Surface((SCROLL_AREA_WIDTH, SCROLL_AREA_HEIGHT))

            # Preencher a superfície com uma cor de fundo (opcional)
            scroll_surface.fill(Funcao.cor('lightgray'))

            y_pos = scroll_offset  # Aplicando o offset de scroll

            for musica in Funcao_Listar_Musica:
                if Funcao.desenhar_botao(scroll_surface, 20, y_pos, texto=musica, cor='white', cor_hover='blue', offset_x=scroll_area.x, offset_y=scroll_area.y):
                    tela_principal = 'musica'
                    Funcao.tocar_musica(f'{pasta_Musica}\\{pasta_selecionada}\\{musica}')
                y_pos += 70  # Ajuste o espaçamento entre os botões

            # Desenhar a superfície dentro da área de rolagem
            screen.blit(scroll_surface, (scroll_area.x, scroll_area.y))

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

        if event.type == pygame.MOUSEWHEEL:  # Evento de rolagem do mouse
            scroll_offset += event.y * scroll_speed
            # Limitar o scroll entre 0 e o limite calculado
            scroll_offset = max(min(scroll_offset, 0), scroll_limit)

    pygame.display.flip()
    clock.tick(10)
