#-*- coding:utf-8 -*-
 
import pygame,os,sys
from pygame.locals import *
from sys import exit
 
pygame.init()
 
screen = pygame.display.set_mode((640, 480), 0, 32)
 
sprite_image_filename = os.path.join(sys.path[0],'game/tanker/img/blast0.gif')
background_image_filename = os.path.join(sys.path[0],'game/hello_game/sea.jpg')
background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename)
#sprite起始坐标
x = 0.

# Clock对象
clock = pygame.time.Clock()
# 速度（像素/秒）
speed = 250.
 
# 加载并播放一个特效音频文件
sound = pygame.mixer.Sound('src/game/tanker/img/start.wav') 
sound.play()
# 加载背景音乐文件 
pygame.mixer.music.load('src/game/tanker/img/fire.wav')
# 播放背景音，循环的播放
# 第一个参数表示播放次数 -1 循环
# 第二个播放位置
pygame.mixer.music.play(-1, 0.0)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            # 停止播放背景音乐 
            pygame.mixer.music.stop() 
            # 退出 
            pygame.quit()
            exit()
 
    screen.blit(background, (0, 0))
    screen.blit(sprite, (x, 100))
    #上次调用经过的时间
    time_passed = clock.tick()
    time_passed_seconds = time_passed / 1000.0
    #移动距离
    distance_moved = time_passed_seconds * speed
    x += distance_moved
    #画出sprite
    screen.blit(sprite, (x, 100))
    #若超出边界则从头开始
    if x > 640.:
        x -= 640
    pygame.display.update()
 