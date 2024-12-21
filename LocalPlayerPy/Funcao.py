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


def Home(texto, pos, cor_texto, cor_rect=(255,255,255)):
    texto_surface = fonte_titulo.render(texto, True, cor_texto)
    texto_rect = texto_surface.get_rect(center=pos)

    pygame.draw.rect(screen, cor_rect,texto_rect.inflate(20, 20), border_radius=10)
    screen.blit(texto_surface, texto_rect)

    return texto_rect

def desenhar_botao(x, y, largura, altura, texto, cor, cor_hover):
    Posicao_Mouse = pygame.mouse.get_pos()
    Clique_Mouse = pygame.mouse.get_pressed()
    if x < Posicao_Mouse[0] < x + largura and y < Posicao_Mouse[1] < y + altura: #O [0] significa posição do mouse no eixo X, e o [1] significa posição do mouse no eixo y
        pygame.draw.rect(screen, cor_hover, (x, y, largura, altura), border_radius=10)
        
        if Clique_Mouse[0]:  # O [0] significa botão esquerdo
            return True
    else:
        pygame.draw.rect(screen, cor, (x, y, largura, altura), border_radius = 10)
    
    
    #Desenhando o texto
    text_surface = fonte_titulo.render(texto, True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(x + largura // 2, y + altura // 2))
    screen.blit(text_surface, text_rect)

    return False

def cor(nome_cor):
    cor = pygame.Color(nome_cor)  
    return (cor.r, cor.g, cor.b)

def Titulo(screen, titulo, cor_titulo, fonte = None):
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
