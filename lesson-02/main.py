import pygame
import sys

# Inicialização
pygame.init()
clock = pygame.time.Clock()

# Configurando a janela
screen_height = 720
scree_width = 1280
limit_left = 0
limit_right = scree_width
limit_top = 0
limit_bottom = screen_height
main_color = (200, 200, 200)
screen = pygame.display.set_mode((scree_width, screen_height))
screen.fill("#4C956C")
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
player = createObject(limit_right-20, half(screen_height)-half(140), 10, 140)
opponent = createObject(10, half(screen_height)-half(140), 10, 140)

ballSpeedX = 5  # 500/1000ms
ballSpeedY = 5

while True:

    # Processando as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Atualização
    ball.x = ball.x + ballSpeedX
    ball.y = ball.y + ballSpeedY
    screen.fill("#4C956C")

    if ball.bottom >= limit_bottom or ball.top <= limit_top:
        ballSpeedY = -ballSpeedY
    
    if ball.right >= limit_right or ball.left <= limit_left:
        ballSpeedX = -ballSpeedX
    
    drawObject(ball,"ellipse", "#F5EE9E")
    drawObject(player,"rect", main_color)
    drawObject(opponent,"rect", main_color)
    
    # Atualizando a janela 60fps
    pygame.display.flip()
    clock.tick(60)