import pygame
import sys,os,random
from config import *
class Tank:
    def __init__(self,window,left,top):
        self.window = window
        self.speed = 5
        self.stop = True
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
    def displayTank(self):
        # 重新设定显示的tank图片，改变方向使用 
        self.image = self.images[self.direction]
        self.window.blit(self.image,self.rect)
    #坦克的移动方法 
    def move(self):

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


class EnemyTank(Tank):

    def __init__(self,window,left,top,speed):
        self.window = window
        self.speed = speed
        self.stop = True
        self.step = 0
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
