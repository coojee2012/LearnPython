import sys, pygame,os
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(os.path.join(sys.path[0],'img/y.jpeg'))
# ballrect = ball.get_rect()
screen.blit(ball, (0,0))
pygame.display.update()
while True:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
