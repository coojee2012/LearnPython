'''
定义一个主体标题类及快捷标题类
'''
import tkinter
class MainMenu:
    '''
    主体菜单
    '''
    def __init__(self,root):
        self.root =root
        self.menu = None
        self.menuFile= None
        self.menuEdit = None
        self.menuHelp = None
    def createWidget(self):
        self.menu = tkinter.Menu(self.root)
        # 创建子菜单
        self.menuFile = tkinter.Menu(self.menu)
        self.menuEdit = tkinter.Menu(self.menu)
        self.menuHelp = tkinter.Menu(self.menu)

        self.menu.add_cascade(label="文件(F)", menu=self.menuFile)
        self.menu.add_cascade(label="编辑(E)", menu=self.menuEdit) 
        self.menu.add_cascade(label="帮助(H)", menu=self.menuHelp)
        
        # 将主菜单栏加到根窗口
        # self.root["menu"] = self.menu
    def bindMenuFile(self,newfile,openfile,savefile,exit):
        # 添加菜单项
        self.menuFile.add_command(label="新建", accelerator="ctrl+n", command=newfile)
        self.menuFile.add_command(label="打开", accelerator="ctrl+o", command=openfile)
        self.menuFile.add_command(label="保存", accelerator="ctrl+s",command=savefile)
        self.menuFile.add_separator() # 添加分割线
        self.menuFile.add_command(label="退出", accelerator="ctrl+q",command=exit)

    def getMenu(self):
        return self.menu


class QuickMenu:
    '''
    快捷菜单
    '''
    def __init__(self,root):
        pass