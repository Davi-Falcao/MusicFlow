import sys
import os
import pygame
import Funcao

user_home_directory = os.path.expanduser("~")
pasta_Musica = f'{user_home_directory}\\Music\\'

#Inicializando Pygame
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("MusicFlow")
icone = pygame.image.load('./icone/MusicFlow.ico') 
pygame.display.set_icon(icone)

#Tela
info_tela = pygame.display.Info()
SCREEN_WIDTH = int(info_tela.current_w/2)
SCREEN_HEIGHT = int(info_tela.current_h/1.5)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()

fonte = "Impact"
fonte_titulo = pygame.font.SysFont(fonte, 30)


while True:
    screen.fill(Funcao.cor('gray'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.VIDEORESIZE:
            SCREEN_WIDTH, SCREEN_HEIGHT = event.w, event.h
            if SCREEN_HEIGHT < int(450):
                SCREEN_HEIGHT = int(450)
            if SCREEN_WIDTH < int(300):
                SCREEN_WIDTH = int(300)
            screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
    
   
    #texto_retangulo = Home("MusicFlow", pos=(100,30), cor_texto=Funcao.cor('black'))
    

    # if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
    #         if event.button == 1: 
    #             if texto_retangulo.collidepoint(event.pos):
    #                 screen.fill(Funcao.cor('white'))
    #                 texto_retangulo = Home("MusicFlow", pos=(100,30), cor_texto=Funcao.cor('black'))
    
    if Funcao.desenhar_botao(30, 30, 100, 30, "MusicFlow", 'white', 'blue'):
        screen.fill(Funcao.cor('white'))
        
    
    if Funcao.desenhar_botao(30, 100, 200, 30, "Clique Aqui", 'white', 'blue'):
        print('botão clicado')

    pygame.display.flip()
    pygame.display.update()
    clock.tick(30)
