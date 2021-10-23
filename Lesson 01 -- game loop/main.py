import pygame
import sys

pygame.init()


clock = pygame.time.Clock()

screen = pygame.display.set_mode((1280, 960))

pygame.display.set_caption("Pong")

ball = pygame.Rect(1280/2-15, 960/2-15, 30, 30)
player = pygame.Rect(1280-20, 960/2-70, 10, 140)
opponent = pygame.Rect(10, 960/2-70, 10, 140)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	pygame.draw.rect(screen, (200,200,200), ball)
	pygame.draw.rect(screen, (200,200,200), player)
	pygame.draw.rect(screen, (200,200,200), opponent)

	pygame.display.flip()
	clock.tick(60)