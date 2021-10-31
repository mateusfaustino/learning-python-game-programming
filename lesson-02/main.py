import pygame
import sys
from components.screen import Screen
# Inicialização
pygame.init()
clock = pygame.time.Clock()

# Configurando a janela
screen = Screen("Pong", 720, 1280,"#4C956C" )
screen.fill()

main_color = (200,200,200)

def half(value):
    return value/2

def createObject(position_x, position_y, object_width, object_height):
    return pygame.Rect(position_x, position_y, object_width, object_height)

def drawObject(object, shape, color):
    if shape=="ellipse":
        pygame.draw.ellipse(screen.display, color, object)
    elif shape=="rect":
        pygame.draw.rect(screen.display, color, object)
    else:
        print (shape,"não é reconhecido como um valor válido")

ball = createObject(half(screen.width)-half(30), half(screen.height)-half(30), 30, 30)
player = createObject(screen.limit_right-20, half(screen.height)-half(140), 10, 140)
opponent = createObject(10, half(screen.height)-half(140), 10, 140)

ballSpeedX = 0.5 
ballSpeedY = 0.5

while True:

    # Processando as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Atualização
    dt = clock.tick(60)
    ball.x = ball.x + ballSpeedX * dt
    ball.y = ball.y + ballSpeedY * dt
    screen.display.fill("#4C956C")

    if ball.bottom >= screen.limit_bottom or ball.top <= screen.limit_top:
        ballSpeedY = -ballSpeedY
    
    if ball.right >= screen.limit_right or ball.left <= screen.limit_left:
        ballSpeedX = -ballSpeedX
    
    drawObject(ball,"ellipse", "#F5EE9E")
    drawObject(player,"rect", main_color)
    drawObject(opponent,"rect", main_color)
    
    # Atualizando a janela 60fps
    pygame.display.flip()