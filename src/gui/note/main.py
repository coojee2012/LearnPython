'''
我的记事本
主体窗口，包含一个Text用于文本的输入,主体菜单和快捷菜单单独模块中定义
'''
import tkinter
from tkinter.filedialog import asksaveasfilename,askopenfile
from tkinter.colorchooser import askcolor
from menu import MainMenu,QuickMenu

NOTE_TITLE = 'Mac记事本'
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
        self.root.bind("<Control-n>",lambda event:self.newfile()) 
        self.root.bind("<Control-o>",lambda event:self.openfile()) 
        self.root.bind("<Control-s>",lambda event:self.savefile()) 
        self.root.bind("<Control-q>",lambda event:self.exit())

        menu.bindMenuFile(newfile=self.newfile,
        openfile=self.openfile,
        savefile=self.savefile,
        exit=self.exit)

        quickMenu = QuickMenu(self.root)
        quickMenu.createWidget()
        quickMenu.bindMenu(changeBG=self.changBG)
        self.quickMenu = quickMenu.menu


        self.root["menu"] = self.mainMenu
        #为右键绑定事件
        self.root.bind("<Button-2>",self.showQuickMenu)

    def newfile(self,cleanText=True):
        if cleanText:
            self.text.delete('1.0',tkinter.END) #把Text控件中的内容清空 
        self.filename = asksaveasfilename(title='另存为', 
        initialfile='未命名.txt',
        filetypes=[("文本文档", "*.txt")],
        defaultextension='.txt')

        self.root.title('{} {}'.format(NOTE_TITLE,self.filename))
        print(self.filename)

    def savefile(self):
        if not self.filename:
            self.newfile(cleanText=False)
        with open(self.filename,'w',encoding='utf8') as f:
            content = self.text.get(1.0,tkinter.END)
            print(content)
            f.write(content)

    def exit(self):
        self.root.quit()

    def openfile(self):
        self.text.delete('1.0',tkinter.END) #先把Text控件中的内容清空 
        with askopenfile(title="打开文件") as f:
            self.text.insert(tkinter.INSERT, f.read()) 
            self.filename = f.name
            self.root.title('{} {}'.format(NOTE_TITLE,f.name)) 
            print(f.name)
    def changBG(self):
        s1 = askcolor(color="red", title="选择背景色") 
        self.text.config(bg=s1[1])
    
    def showQuickMenu(self,event):
        self.quickMenu.post(event.x_root,event.y_root)

root = tkinter.Tk()
root.geometry("550x650+200+300") 
root.title(NOTE_TITLE) 
app = Note(root=root) 
root.mainloop()