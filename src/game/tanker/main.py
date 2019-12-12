'''
坦克大战
本代码参考了部分教程代码，根据自己对游戏的想法做了一定调整
'''
import pygame,sys,time,random
from pygame.locals import *
from config import *
import tank
_dispaly = pygame.display
COLOR_BG = pygame.Color(0,0,0) # 游戏背景色-黑色
COLOR_RED = pygame.Color(255, 255, 255)
class MainGame:
    '''
    游戏主类
    '''
    window = None # 游戏的窗体对象

    # 定义我方的坦克
    TANK_P1 = None
    # 敌方坦克
    EnemyTanks = []
    def __ini__(self):
        pass
    def start(self):
        _dispaly.init()
        MainGame.window = _dispaly.set_mode([SCREEN_WIDTH,SCREEN_HEIGT])
        
        _dispaly.set_caption("坦克又见坦克")
        
        # 加载我方坦克
        MainGame.TANK_P1 = tank.Tank(MainGame.window,400,300)
        # 加载敌方坦克
        self.creatEnemyTank()
        
        # 循环刷新窗体
        while True:
            # 不循环事件会卡住
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit(0) # 0正常退出程序
                else:
                    self.doneEvent(event)

            MainGame.window.fill(COLOR_BG)
            MainGame.window.blit(self.getTextSurface(u"Remain %d Tankers"%5),(5,5))
            MainGame.TANK_P1.displayTank()

            
            self.blitEnemyTank()
            #根据坦克的开关状态调用坦克的移动方法
            if MainGame.TANK_P1 and not MainGame.TANK_P1.stop:
                MainGame.TANK_P1.move() 
            time.sleep(0.02)
            _dispaly.update()
    def getTextSurface(self,text):
        pygame.font.init()
        font = pygame.font.SysFont('Arial',18)
        textSurface = font.render(text,True,COLOR_RED)
        return textSurface
    def doneEvent(self,event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("我方坦克正在向左行进......")
                MainGame.TANK_P1.direction = 'L'
                MainGame.TANK_P1.stop = False
            elif event.key == pygame.K_RIGHT:
                print("我方坦克正在向右行进......")
                MainGame.TANK_P1.direction = 'R'
                MainGame.TANK_P1.stop = False
            elif event.key == pygame.K_UP:
                print("我方坦克正在进攻......")
                MainGame.TANK_P1.direction = 'U'
                MainGame.TANK_P1.stop = False
            elif event.key == pygame.K_DOWN:
                print("我方坦克正在战术撤退......")
                MainGame.TANK_P1.direction = 'D'
                MainGame.TANK_P1.stop = False
            elif event.key == pygame.K_SPACE:
                print("发射子弹")
        if event.type == pygame.KEYUP:
            print("按键松开")
            if event.key in [K_LEFT,K_RIGHT,K_UP,K_DOWN]:
                print("方向：",event.key)
                MainGame.TANK_P1.stop = True
    
    #创建敌方坦克
    def creatEnemyTank(self):
        top = 100
        speed = random.randint(3,6)
        for i in range(ENEMTANK_COUNT):
        #每次都随机生成一个 left 值
            left = random.randint(1, 7)
            eTank = tank.EnemyTank(MainGame.window,left*100,top,speed) 
            MainGame.EnemyTanks.append(eTank)
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTanks: 
            eTank.displayTank() 
            #坦克移动的方法 
            eTank.randMove()
# 运行游戏

game = MainGame()
game.start()

