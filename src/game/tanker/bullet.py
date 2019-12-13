'''
坦克的子弹类
'''
import pygame
import sys,os,random
from config import *
from base_sprite import BaseSprite
from explode import Explode
class Bullet(BaseSprite):
    def __init__(self,tank):
        self.image = pygame.image.load(os.path.join(sys.path[0],'img/enemymissile.gif'))
        self.direction = tank.direction
        self.rect = self.image.get_rect()
        self.tank = tank

        if self.direction == 'U':
            self.rect.left = tank.rect.left + tank.rect.width/2 - self.rect.width/2
            self.rect.top = tank.rect.top - self.rect.height
        elif self.direction == 'D':
            self.rect.left = tank.rect.left + tank.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.height
        elif self.direction == 'L':
            self.rect.left = tank.rect.left - self.rect.width / 2 - self.rect.width / 2
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        elif self.direction == 'R':
            self.rect.left = tank.rect.left + tank.rect.width
            self.rect.top = tank.rect.top + tank.rect.width / 2 - self.rect.width / 2
        #速度
        self.speed = 7 
        #用来记录子弹是否活着 
        self.live = True
    def bulletMove(self):
        if self.direction == 'U': 
            if self.rect.top > 0:
                self.rect.top -= self.speed 
            else:
                #修改状态值
                self.live = False
        elif self.direction == 'D':
            if self.rect.top < SCREEN_HEIGT - self.rect.height: 
                self.rect.top += self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'L':
            if self.rect.left > 0: 
                self.rect.left -= self.speed
            else:
                # 修改状态值
                self.live = False
        elif self.direction == 'R':
            if self.rect.left < SCREEN_WIDTH - self.rect.width: 
                self.rect.left += self.speed
            else:
                # 修改状态值
                self.live = False

    def hitTank(self,etanks,p1):
        explodes = []
        # 我方坦克牺牲了
        if pygame.sprite.collide_rect(p1,self):

            self.live = False
            if self.tank is not p1: 
                p1.live = False
                explodes.append(Explode(p1))

        # 地方坦克
        for tank in etanks:
            if pygame.sprite.collide_rect(tank,self):
                self.live = False
                if self.tank is p1:  # 自己人不打自己人，不科学
                    tank.live = False
                    explodes.append(Explode(tank))
        return explodes
    
    def hitWalls(self,walls):
        for wall in walls:
            if pygame.sprite.collide_rect(wall,self): #修改子弹的 live 属性
                self.live = False
                wall.hp -= 1
                if wall.hp <= 0: 
                    wall.live = False
