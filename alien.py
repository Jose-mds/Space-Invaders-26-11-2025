# alien.py
import pygame
import random
from bullet import Bullet

alienColors = {1:(50,150,255), 2:(50,255,50), 3:(255,50,50)}

ALIENWIDTH = 40
ALIENHEIGHT = 30

class Alien:
    def __init__(self, posx, posy, typeAlien):
        self.x = posx
        self.y = posy
        self.typeAlien = typeAlien
        self.alive = True
        self.rect = pygame.Rect(self.x, self.y, ALIENWIDTH, ALIENHEIGHT)
        self.nextShot = random.uniform(0.5,3.0)

    def moveAlien(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def tryToShoot(self, bulletsList):
        self.nextShot -= 1/60
        if self.nextShot <=0:
            chance = random.randint(0,200)
            if chance == 1:
                b = Bullet(self.rect.centerx, self.rect.bottom, 5)
                bulletsList.append(b)
            self.nextShot = random.uniform(0.5,3.0)

    def drawAlien(self, screen):
        pygame.draw.rect(screen, alienColors[self.typeAlien], self.rect)
        font = pygame.font.SysFont(None,16)
        img = font.render(str(self.typeAlien),True,(0,0,0))
        screen.blit(img, (self.rect.x+10,self.rect.y+5))
