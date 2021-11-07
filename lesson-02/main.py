import pygame
import sys
from components.screen import Screen
from components.ball import Ball
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

ball = Ball ([half(screen.width)-half(30), half(screen.height)-half(30)],[30,30],"#F5EE9E")

player = createObject(screen.limit_right-20, half(screen.height)-half(140), 10, 140)
opponent = createObject(10, half(screen.height)-half(140), 10, 140)


while True:

    # Processando as entradas (eventos)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Atualização
    dt = clock.tick(60)
    ball.x = ball.x + ball.speedX * dt
    ball.y = ball.y + ball.speedY * dt
    screen.display.fill("#4C956C")

    if ball.bottom >= screen.limit_bottom or ball.top <= screen.limit_top:
        ball.setSpeed(ball.speedX, -ball.speedY)
    
    if ball.right >= screen.limit_right or ball.left <= screen.limit_left:
        ball.setSpeed(-ball.speedX, ball.speedY)
    
    ball.draw(screen)
    drawObject(player,"rect", main_color)
    drawObject(opponent,"rect", main_color)
    
    # Atualizando a janela 60fps
    pygame.display.flip()