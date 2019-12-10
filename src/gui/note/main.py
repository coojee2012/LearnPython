'''
我的记事本
主体窗口，包含一个Text用于文本的输入,主体菜单和快捷菜单单独模块中定义
'''
import tkinter
from tkinter.filedialog import asksaveasfilename
from menu import MainMenu,QuickMenu
class Note(tkinter.Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.root = root
        self.text = None 
        self.filename = None 
        self.mainMenu = None
        self.quickMenu = None
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        # 创建一个Text
        self.text = tkinter.Text(self,width=550, height=650)
        self.text.pack()

        # 将主菜单栏加到根窗口

        menu = MainMenu(root)
        menu.createWidget()
        self.mainMenu = menu.getMenu()
        #添加快捷键事件处理
        root.bind("<Control-n>",lambda event:self.newfile()) 
        root.bind("<Control-o>",lambda event:self.openfile()) 
        root.bind("<Control-s>",lambda event:self.savefile()) 
        root.bind("<Control-q>",lambda event:self.exit())

        self.root["menu"] = self.mainMenu

    def newfile(self):
        self.text.delete('1.0','end') #把Text控件中的内容清空 
        self.filename = asksaveasfilename(title='另存为', 
        initialfile='未命名.txt',
        filetypes=[("文本文档", "*.txt")],
        defaultextension='.txt')
        self.savefile()

    def savefile(self):
        pass

    def exit(self):
        pass

    def openfile(self):
        pass

root = tkinter.Tk()
root.geometry("550x650+200+300") 
root.title("Mac记事本") 
app = Note(root=root) 
root.mainloop()