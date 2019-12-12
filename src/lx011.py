# _*_coding:utf-8_*_

import pygame
from pygame.locals import *
import sys,os

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
font_path = image_path = os.path.join(sys.path[0],'TimesNewRoman.ttf')
my_font = pygame.font.Font(font_path, 16)
FONT_COLOR = (255, 255, 0)

textSurface = my_font.render(u"San Guo Zhan Ji",True,FONT_COLOR)

x,y = 10,10

while True:
    event = pygame.event.wait()
    if event.type == QUIT:
        sys.exit()
    screen.blit(textSurface,(x,y))
    pygame.display.update()