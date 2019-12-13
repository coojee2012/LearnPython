
import pygame
import sys,os,random
class Music:
    def __init__(self,fireFile,hitFile):
        #先初始化混合器
        pygame.mixer.init()
        self.fire = pygame.mixer.Sound(os.path.join(sys.path[0],fireFile)) 
        self.hit = pygame.mixer.Sound(os.path.join(sys.path[0],hitFile)) 
    def playbgm(self,bgmFile):
        pygame.mixer.music.load(os.path.join(sys.path[0],bgmFile))
        pygame.mixer.music.play( )

    def playfire(self):
        self.fire.play()
    def playhit(self):
        self.hit.play()