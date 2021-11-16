import pygame
import random
class Ball (pygame.Rect):

    def __init__(self,position=[0,0], size=[20,60], color = (255, 255, 255) ):
        self.speedX = 0.5
        self.speedY = 0.5
        super().__init__(position[0], position[1], size[0], size[1])
        self.initial_position = position
        self.score = 0
        self.color = color
        
    def setSpeed(self, speedX, speedY):
        self.speedX = speedX
        self.speedY = speedY

    def draw(self,screen):
        pygame.draw.ellipse(screen.display, self.color, self)
    
    def colid_on_limits(self,screen):
        
        if self.bottom >= screen.limit_bottom or self.top <= screen.limit_top:
            self.setSpeed(self.speedX, -self.speedY)
    
    def go_out(self,screen):
        if self.right >= screen.limit_right or self.left <= screen.limit_left:
            self.reset(screen)

    def colid_on_paddle(self, paddle):
        if self.colliderect(paddle):
            self.setSpeed(-self.speedX, self.speedY)

    def reset(self,screen):
        self.center = (screen.width/2,screen.height/2)
        self.speedX = random.choice((-0.5,0.5))
        
        