import time
import pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
positionX = 0
speedX = 100  # 100 pixels por segundo
ti = time.time()  # captura o tempo inicial
while True:
    if pygame.event.poll().type == pygame.QUIT:
        break
    tf = time.time()  # captura o tempo deste ciclo
    dt = (tf - ti)  # calcula o delta
    ti = tf  # atribui o tempo final como tempo inicial
    positionX += speedX * dt  # move o quadrado na velocidade média definida
    screen.fill((0, 0, 0))
    pygame.draw.ellipse(screen, (255, 255, 255), [positionX, 230, 20, 20])
    pygame.display.flip()