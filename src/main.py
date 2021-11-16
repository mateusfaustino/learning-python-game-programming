import pygame
import sys
import random

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

def draw():
    ball.draw(screen)
    player.draw(screen)
    opponent.draw(screen)
    pygame.display.flip()

def inputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    (x,y)= pygame.mouse.get_pos()
    player.y = y - 70

def update():
    dt = clock.tick(60)
    ball.x = ball.x + ball.speedX * dt
    ball.y = ball.y + ball.speedY * dt
    screen.display.fill("#4C956C")

    ball.colid_on_limits(screen)
    ball.colid_on_paddle(player)
    ball.colid_on_paddle(opponent)
    ball.go_out(screen)
    opponent.move_towards_ball(ball)

while True:
    inputs()
    update()
    draw()
  
    