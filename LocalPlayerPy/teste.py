import pygame

# Inicializar o pygame
pygame.init()

# Configurar a tela
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Texto com Retângulo Clicável")

# Configurar fontes e cores
fonte_titulo = pygame.font.Font(None, 72)  # Fonte do título
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 123, 255)

# Funcao para renderizar texto e desenhar retângulo clicável
def desenhar_texto_clicavel(screen, texto, pos, fonte, cor_texto, cor_retangulo):
    # Renderizar o texto
    texto_surface = fonte.render(texto, True, cor_texto)
    texto_rect = texto_surface.get_rect(center=pos)

    # Desenhar o retângulo ao redor do texto
    pygame.draw.rect(screen, cor_retangulo, texto_rect.inflate(20, 20), border_radius=10)

    # Desenhar o texto na tela
    screen.blit(texto_surface, texto_rect)

    return texto_rect  # Retorna o retângulo para detectar clique

# Loop principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detectar clique do mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Clique esquerdo
            mouse_pos = event.pos
            if texto_retangulo.collidepoint(mouse_pos):
                print("Texto clicado!")

    # Preencher a tela com branco
    screen.fill(WHITE)

    # Desenhar o título e obter o retângulo clicável
    texto_retangulo = desenhar_texto_clicavel(
        screen,
        "MusicFlow",
        pos=(400, 300),  # Posição centralizada
        fonte=fonte_titulo,
        cor_texto=BLACK,
        cor_retangulo=BLUE,
    )

    # Atualizar a tela
    pygame.display.flip()

# Finalizar o pygame
pygame.quit()
