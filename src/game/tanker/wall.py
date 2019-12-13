import pygame
import sys,os,random
from config import *

class Wall:
    def __init__(self,left,top):
        self.image = pygame.image.load(os.path.join(sys.path[0],'img/steels.gif'))
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top 
        #用来判断墙壁是否应该在窗口中展示 
        self.live = True
        #用来记录墙壁的生命值
        self.hp = 3
    def displayWall(self,window):
        window.blit(self.image,self.rect)
   