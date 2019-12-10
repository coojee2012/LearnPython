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
    def createWidget(self):
        self.menu = tkinter.Menu(self.root)
        # 创建子菜单
        menuFile = tkinter.Menu(self.menu)
        menuEdit = tkinter.Menu(self.menu)
        menuHelp = tkinter.Menu(self.menu)

        self.menu.add_cascade(label="文件(F)", menu=menuFile)
        self.menu.add_cascade(label="编辑(E)", menu=menuEdit) 
        self.menu.add_cascade(label="帮助(H)", menu=menuHelp)
        # 添加菜单项
        menuFile.add_command(label="新建", accelerator="ctrl+n", command=self.newfile)
        menuFile.add_command(label="打开", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="保存", accelerator="ctrl+s",command=self.savefile)
        menuFile.add_separator() # 添加分割线
        menuFile.add_command(label="退出", accelerator="ctrl+q",command=self.exit)
        # 将主菜单栏加到根窗口
        # self.root["menu"] = self.menu

    def newfile(self):
        pass
    def savefile(self):
        pass
    def exit(self):
        pass
    def openfile(self):
        pass
    def getMenu(self):
        return self.menu


class QuickMenu:
    '''
    快捷菜单
    '''
    def __init__(self,root):
        pass