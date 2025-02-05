import pygame
import os

pygame.init()
info_tela = pygame.display.Info()
SCREEN_WIDTH = int(info_tela.current_w / 2)
SCREEN_HEIGHT = int(info_tela.current_h / 1.5)
MUSIC_SCREEN_WIDTH = 330
MUSIC_SCREEN_HEIGHT = 480
user_home_directory = os.path.expanduser("~")
pasta_Musica = f'{user_home_directory}\\Music\\'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

fonte = "Impact"
fonte_titulo = pygame.font.SysFont(fonte, 30)

def desenhar_botao(screen, x, y, texto=None, cor='white', cor_hover='blue', imagem=None, offset_x=0, offset_y=0):
    posicao_mouse = pygame.mouse.get_pos()
    clique_mouse = pygame.mouse.get_pressed()

    # Ajustando a posição do mouse relativa à superfície
    posicao_mouse_relativa = (posicao_mouse[0] - offset_x, posicao_mouse[1] - offset_y)

    if imagem:
        imagem_surface = pygame.image.load(imagem)
        botao_rect = imagem_surface.get_rect(topleft=(x, y))
    else:
        text_surface = fonte_titulo.render(texto, True, (0, 0, 0))
        botao_rect = text_surface.get_rect(topleft=(x, y))

    # Ajustar o y_pos com o scroll_offset para verificar a colisão corretamente
    botao_rect.y += offset_y

    if botao_rect.collidepoint(posicao_mouse_relativa):
        pygame.draw.rect(screen, pygame.Color(cor_hover), botao_rect.inflate(20, 20), border_radius=10)
        if clique_mouse[0]:  # Botão esquerdo do mouse foi clicado
            return True
    else:
        pygame.draw.rect(screen, pygame.Color(cor), botao_rect.inflate(20, 20), border_radius=10)

    if imagem:
        screen.blit(imagem_surface, botao_rect)
    else:
        screen.blit(text_surface, botao_rect)

    return False

def cor(nome_cor):
    cor = pygame.Color(nome_cor)  
    return (cor.r, cor.g, cor.b)

def listar_conteudo(diretorio):
    conteudo = os.listdir(diretorio)
    pastas = [item for item in conteudo if os.path.isdir(os.path.join(diretorio, item))]
    musicas = [item for item in conteudo if item.endswith('.mp3') or item.endswith('.wav') or item.endswith('.mp4')]
    return pastas, musicas

def tocar_musica(musica):
    caminho_musica = os.path.join(pasta_Musica, musica)
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.play()
