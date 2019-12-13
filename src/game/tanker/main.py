'''
坦克大战
本代码参考了部分教程代码，根据自己对游戏的想法做了一定调整
'''
import pygame,sys,time,random
from pygame.locals import *
from config import *
import tank
from wall import Wall
from music import Music


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
    # 存放子弹
    Bullets = []

    # 爆炸列表
    Exploads = []

    # 墙体
    Walls = []
    def __init__(self):
        self.music = Music(fireFile='img/fire.wav',hitFile='img/hit.wav')
    def start(self):
        _dispaly.init()
        MainGame.window = _dispaly.set_mode([SCREEN_WIDTH,SCREEN_HEIGT])
        
        _dispaly.set_caption("坦克又见坦克")
        
        self.music.playbgm(bgmFile='img/start.wav')
        # 加载我方坦克
        MainGame.TANK_P1 = tank.Tank(MainGame.window,400,300)
        # 加载敌方坦克
        self.creatEnemyTank()
        self.creatWalls()
        
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
            if len(MainGame.EnemyTanks) == 0:
                x = random.randint(10, 700)
                y = random.randint(10, 500)
                MainGame.window.blit(self.getTextSurface("You Win Press 'R' Restart"),(x,y))
                time.sleep(1)
                _dispaly.update()
                continue
            if not MainGame.TANK_P1.live:
                x = random.randint(10, 700)
                y = random.randint(10, 500)
                MainGame.window.blit(self.getTextSurface("You Loss Press 'R' Restart"),(x,y))
                time.sleep(1)
                _dispaly.update()
                continue


            MainGame.window.blit(self.getTextSurface(u"Remain %d Tankers"%len(MainGame.EnemyTanks)),(5,5))
            if MainGame.TANK_P1.live:
                MainGame.TANK_P1.displayTank()
                MainGame.TANK_P1.hitWalls(MainGame.Walls)
                MainGame.TANK_P1.hitTank(MainGame.EnemyTanks, MainGame.TANK_P1)

            self.blitWalls()
            self.blitEnemyTank()
            self.blitBullets()
            self.blitExploads()
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
                #产生一颗子弹
                m = MainGame.TANK_P1.shot() 
               
                self.music.playfire()
                #将子弹加入到子弹列表 
                MainGame.Bullets.append(m)
            elif event.key == pygame.K_r:
                if len(MainGame.EnemyTanks) == 0  or not MainGame.TANK_P1.live:
                    self.restart()
        if event.type == pygame.KEYUP:
            print("按键松开")
            if event.key in [K_LEFT,K_RIGHT,K_UP,K_DOWN]:
                print("方向：",event.key)
                MainGame.TANK_P1.stop = True
    
    def restart(self):
        MainGame.EnemyTanks = []
        MainGame.Walls = []
        MainGame.Bullets = []
        MainGame.Exploads = []
        MainGame.TANK_P1 = None

        self.music.playbgm(bgmFile='img/start.wav')
        # 加载我方坦克
        MainGame.TANK_P1 = tank.Tank(MainGame.window,400,300)
        # 加载敌方坦克
        self.creatEnemyTank()
        self.creatWalls()
    #创建敌方坦克
    def creatEnemyTank(self):
        top = 100
        speed = random.randint(3,6)
        for i in range(ENEMTANK_COUNT):
        #每次都随机生成一个 left 值
            left = random.randint(1, 7)
            eTank = tank.EnemyTank(MainGame.window,left*100,top,speed) 
            MainGame.EnemyTanks.append(eTank)
    
    #创建墙壁的方法 
    def creatWalls(self):
        for i in range(6):
            wall = Wall(130*i,240) 
            MainGame.Walls.append(wall)
    
    def blitEnemyTank(self):
        for eTank in MainGame.EnemyTanks:
            if eTank.live: 
                eTank.displayTank() 
                #坦克移动的方法 
                eTank.randMove()
                eTank.hitWalls(MainGame.Walls)
                eTank.hitTank(MainGame.EnemyTanks, MainGame.TANK_P1)
                eBullet = eTank.shot()
                if eBullet:
                    MainGame.Bullets.append(eBullet)
            else:
                MainGame.EnemyTanks.remove(eTank)
    def blitBullets(self):
        for bull in MainGame.Bullets:
            if bull.live:
                MainGame.window.blit(bull.image,bull.rect)
                bull.bulletMove()
                bull.hitWalls(MainGame.Walls)
                MainGame.Exploads = bull.hitTank(MainGame.EnemyTanks,MainGame.TANK_P1)
            else:
                MainGame.Bullets.remove(bull)
    
    def blitExploads(self):
        for explode in MainGame.Exploads: 
            if explode.live:
                self.music.playhit()
                explode.displayExplode(MainGame.window)
            else:
                MainGame.Exploads.remove(explode)
    def blitWalls(self):
        for wall in MainGame.Walls:
            if wall.live: 
                wall.displayWall(MainGame.window)
            else: 
                MainGame.Walls.remove(wall)

# 运行游戏

game = MainGame()
game.start()

