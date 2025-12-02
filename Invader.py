# invader.py
import pygame
import random
from bullet import Bullet

invaderColors = {1:(50,150,255), 2:(50,255,50), 3:(255,50,50)}

INVADERWIDTH = 40
INVADERHEIGHT = 30

class Invader:
    def __init__(self, posx, posy, typeAlien):
        self.x = posx
        self.y = posy
        self.typeInvader = typeInvader
        self.alive = True
        self.rect = pygame.Rect(self.x, self.y, INVADERWIDTH, INVADERHEIGHT)
        self.nextShot = random.uniform(0.5,3.0)

    def moveInvader(self, dx, dy):
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

    def drawInvader(self, screen):
        pygame.draw.rect(screen,InvaderColors[self.typeInvader], self.rect)
        font = pygame.font.SysFont(None,16)
        img = font.render(str(self.typeInvader),True,(0,0,0))
        screen.blit(img, (self.rect.x+10,self.rect.y+5))
