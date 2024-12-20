import pygame
import os

user_home_directory = os.path.expanduser("~")
pasta_Musica = f'{user_home_directory}\\Music\\'

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