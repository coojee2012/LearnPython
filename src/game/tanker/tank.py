import pygame
import sys,os,random
from config import *
from bullet import Bullet
from base_sprite import BaseSprite

class Tank(BaseSprite):
    def __init__(self,window,left,top):
        self.window = window
        self.speed = 5
        self.stop = True
        self.live = True
        self.images = {
            'U':pygame.image.load(os.path.join(sys.path[0],'img/p1tankU.gif')),
            'D':pygame.image.load(os.path.join(sys.path[0],'img/p1tankD.gif')),
            'L':pygame.image.load(os.path.join(sys.path[0],'img/p1tankL.gif')),
            'R':pygame.image.load(os.path.join(sys.path[0],'img/p1tankR.gif')),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]

        self.rect = self.image.get_rect()

        # 初始化图像显示的x,y轴
        self.rect.left = left
        self.rect.top = top

        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top
    def displayTank(self):
        # 重新设定显示的tank图片，改变方向使用 
        self.image = self.images[self.direction]
        self.window.blit(self.image,self.rect)
    #坦克的移动方法 
    def move(self):
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

        if self.direction == 'L': 
            if self.rect.left > 0:
                self.rect.left -= self.speed 
        elif self.direction == 'R':
            if self.rect.left + self.rect.height < SCREEN_WIDTH: 
                self.rect.left += self.speed
        elif self.direction == 'U': 
            if self.rect.top > 0:
                self.rect.top -= self.speed 
        elif self.direction == 'D':
            if self.rect.top + self.rect.height < SCREEN_HEIGT: 
                self.rect.top += self.speed
    
    def shot(self):
        return Bullet(self)

    def stay(self):
        self.rect.left = self.oldLeft 
        self.rect.top = self.oldTop
    
    def hitWalls(self,walls):
        for wall in walls:
            if pygame.sprite.collide_rect(wall,self):
                self.stay()
    def hitTank(self,etanks,p1):
        if pygame.sprite.collide_rect(p1,self) and p1 is not self:
                self.stay()
        for eTank in etanks:
            if pygame.sprite.collide_rect(eTank,self) and eTank is not self:
                #print("敌军坦克可以穿过任何坦克！这样才好玩！！！！")
                #self.stay()
                pass


class EnemyTank(Tank):

    def __init__(self,window,left,top,speed):
        self.window = window
        self.speed = speed
        self.stop = True
        self.step = 0
        self.live = True
        self.images = {
            'U':pygame.image.load(os.path.join(sys.path[0],'img/enemy1U.gif')),
            'D':pygame.image.load(os.path.join(sys.path[0],'img/enemy1D.gif')),
            'L':pygame.image.load(os.path.join(sys.path[0],'img/enemy1L.gif')),
            'R':pygame.image.load(os.path.join(sys.path[0],'img/enemy1R.gif')),
        }
        self.direction = self.randDirection()
        self.image = self.images[self.direction]

        self.rect = self.image.get_rect()

        # 初始化图像显示的x,y轴
        self.rect.left = left
        self.rect.top = top
        self.oldLeft = self.rect.left
        self.oldTop = self.rect.top

    def displayTank(self):
        # 重新设定显示的tank图片，改变方向使用 
        self.image = self.images[self.direction]
        self.window.blit(self.image,self.rect)
    
    def randDirection(self):

        num = random.randint(1,4) 
        if num == 1:
            return 'U' 
        elif num == 2: 
            return 'D' 
        elif num == 3:
            return 'L' 
        elif num == 4: 
            return 'R'
    
    def randMove(self): 
        if self.step <= 0:
            self.direction = self.randDirection()
            self.step = 50 
        else:
            self.move() 
            self.step -= 1
    
    def shot(self):
        num = random.randint(1,1000) 
        if num <= 20:
            return Bullet(self)
