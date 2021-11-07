import pygame
import sys
from components.screen import Screen
from components.ball import Ball
from components.paddle import Paddle
# Inicialização
pygame.init()
clock = pygame.time.Clock()

# Configurando a janela
screen = Screen("Pong", 720, 1280,"#4C956C" )
screen.fill()

ball = Ball ([screen.getMidWidthCentralized(30), screen.getMidHeightCentralized(30)],[30,30],"#F5EE9E")
player = Paddle([screen.limit_right-20,screen.getMidHeightCentralized(140)],[10, 140],(200,200,200))
opponent = Paddle([10,screen.getMidHeightCentralized(140)],[10, 140],(200,200,200))

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
    
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball.setSpeed(-ball.speedX, ball.speedY)
    

    ball.draw(screen)
    player.draw(screen)
    opponent.draw(screen)
    
    # Atualizando a janela 60fps
    pygame.display.flip()