# tutprial:
# https://www.youtube.com/watch?v=vMnr7sS3Sv4&ab_channel=Ecodigit

import pygame

class ScoreBoard ():
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)
        self.points = 0
    
    def count(self,screen):
        self.text= self.font.render("Pontos = "+ str(self.points),1,1,(255,255,255))
        self.textpos=self.text.get_rect()
        self.textpos.center = screen.get_width() / 2
        screen.blit(self.text, self.textpos)
        screen.blit(screen, (0,0))
