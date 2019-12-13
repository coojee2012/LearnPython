'''
爆炸效果,坦克的爆炸效果
'''
import pygame
import sys,os
class Explode:
    def __init__(self,tank):
        self.rect = tank.rect
        self.step = 0 
        self.images = [
            pygame.image.load(os.path.join(sys.path[0],'img/blast0.gif')), 
            pygame.image.load(os.path.join(sys.path[0],'img/blast1.gif')), 
            pygame.image.load(os.path.join(sys.path[0],'img/blast2.gif')), 
            pygame.image.load(os.path.join(sys.path[0],'img/blast3.gif')),
            pygame.image.load(os.path.join(sys.path[0],'img/blast4.gif')) 
            ]
        self.image = self.images[self.step]
        self.live = True

    def displayExplode(self,window):
        if self.step < len(self.images): 
            window.blit(self.image, self.rect) 
            self.image = self.images[self.step]
            self.step += 1
        else:
            self.live = False
            self.step = 0

