import pygame
import sys,os

pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
image_path = os.path.join(sys.path[0],'game/tanker/img/blast0.gif')
img = pygame.image.load(image_path)
x,y = 0,0 # 设置坐标

while True:

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                x += -10
            elif e.key == pygame.K_RIGHT:
                x += 10
            elif e.key == pygame.K_UP:
                y += -10
            elif e.key == pygame.K_DOWN:
                y += 10 # 不太理解 反角方向是反的哈哈

        screen.fill((0,0,0))
        screen.blit(img,(x,y))
        pygame.display.update()