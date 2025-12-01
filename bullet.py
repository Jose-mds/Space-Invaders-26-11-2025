# bullet.py
import pygame

class Bullet:
    def __init__(self, startx, starty, speedBullet):
        self.rect = pygame.Rect(startx,starty,4,10)
        self.speedBullet = speedBullet

    def moveBullet(self):
        self.rect.y += self.speedBullet

    def drawBullet(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.rect)
