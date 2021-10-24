import pygame
import sys

# Inicialização
pygame.init()
clock = pygame.time.Clock()

# Configurando a janela
screen_height = 720
scree_width = 1280
limit_left = 10
limit_right = scree_width-10
limit_top = 10
limit_bottom = screen_height-10
main_color = (200, 200, 200)
screen = pygame.display.set_mode((scree_width, screen_height))

pygame.display.set_caption('Pong')


def half(value):
    return value/2

def createObject(position_x, position_y, object_width, object_height):
    return pygame.Rect(position_x, position_y, object_width, object_height)

def drawObject(object, shape, color):
    if shape=="ellipse":
        pygame.draw.ellipse(screen, color, object)
    elif shape=="rect":
        pygame.draw.rect(screen, color, object)
    else:
        print (shape,"não é reconhecido como um valor válido")

ball = createObject(half(scree_width)-half(30), half(screen_height)-half(30), 30, 30)
player = createObject(limit_right-10, half(screen_height)-half(140), 10, 140)
opponent = createObject(10, half(screen_height)-half(140), 10, 140)

while True:

    # Processando as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
   
    drawObject(ball,"ellipse", main_color)
    drawObject(player,"rect", main_color)
    drawObject(opponent,"rect", main_color)
    
    # Atualizando a janela 60fps
    pygame.display.flip()
    clock.tick(60)