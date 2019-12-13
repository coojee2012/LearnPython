'''
碰撞检测的基类，让tank 和 子弹都集成它
'''
import pygame
class BaseSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)