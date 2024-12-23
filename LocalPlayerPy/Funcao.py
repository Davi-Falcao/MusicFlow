import pygame
import os

pygame.init()
info_tela = pygame.display.Info()
SCREEN_WIDTH = int(info_tela.current_w/2)
SCREEN_HEIGHT = int(info_tela.current_h/1.5)
user_home_directory = os.path.expanduser("~")
pasta_Musica = f'{user_home_directory}\\Music\\'
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

fonte = "Impact"
fonte_titulo = pygame.font.SysFont(fonte, 30)

def desenhar_botao(screen, x, y, texto, cor, cor_hover):
    # Obtemos a posição do mouse e o estado de clique
    posicao_mouse = pygame.mouse.get_pos()
    clique_mouse = pygame.mouse.get_pressed()

    # Renderizando o texto do botão
    text_surface = fonte_titulo.render(texto, True, (0, 0, 0))
    text_rect = text_surface.get_rect(topleft=(x, y))

    # Verificando se o mouse está sobre o botão
    if text_rect.collidepoint(posicao_mouse):
        pygame.draw.rect(screen, pygame.Color(cor_hover), text_rect.inflate(20, 20), border_radius=10)
        if clique_mouse[0]:  # Botão esquerdo do mouse foi clicado
            return True
    else:
        pygame.draw.rect(screen, pygame.Color(cor), text_rect.inflate(20, 20), border_radius=10)

    # Desenhando o texto do botão
    screen.blit(text_surface, text_rect)
    
    return False

def cor(nome_cor):
    cor = pygame.Color(nome_cor)  
    return (cor.r, cor.g, cor.b)

def Home(screen, texto, pos, cor_texto, cor_rect=(255, 255, 255)):
    texto_surface = fonte_titulo.render(texto, True, cor_texto)
    texto_rect = texto_surface.get_rect(center=pos)

    pygame.draw.rect(screen, cor_rect, texto_rect.inflate(20, 20), border_radius=10)
    screen.blit(texto_surface, texto_rect)

    return texto_rect

def Titulo(screen, titulo, cor_titulo, fonte=None):
    if fonte is None:
        fonte = pygame.font.SysFont('Arial', 30)
    
    texto = fonte.render(titulo, True, cor_titulo)
    screen.blit(texto, (10, 10))

def listar_conteudo(diretorio):
    conteudo = os.listdir(diretorio)
    pastas = [item for item in conteudo if os.path.isdir(os.path.join(diretorio, item))]
    musicas = [item for item in conteudo if item.endswith('.mp3') or item.endswith('.wav') or item.endswith('.mp4')]
    return pastas, musicas

def tocar_musica(musica):
    caminho_musica = os.path.join(pasta_Musica, musica)  # Caminho completo para a música
    pygame.mixer.music.load(caminho_musica)  # Carrega a música
    pygame.mixer.music.play()  # Toca a música

def pausar_musica(musica):
    caminho_musica = os.path.join(pasta_Musica, musica)
    pygame.mixer.music.load(caminho_musica)
    pygame.mixer.music.pause()

