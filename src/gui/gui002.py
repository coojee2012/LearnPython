from tkinter import *
from tkinter import messagebox 

class App(Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.root = root
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        """创建组件"""
        # super()代表的是父类的
        self.btn01 = Button(self) 
        self.btn01["text"] = "按钮一" 
        self.btn01.pack() 
        self.btn01["command"] = self.show_msg
        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=self.root.destroy)
        self.btnQuit.pack()

        # 创建一个Lable
        self.lable01 = Label(self,text="Label1")
        self.lable01.config({'bg':'red','width':10,'height':2})
        self.lable01['fg'] = "blue"
        self.lable01.pack() # pack后面讲到，是一个布局
        

        # 创建一个Entry
        self.entry01 = Entry(self,text="Entry")
        self.entry01.pack(side="left")

        self.btn02 = Button(self, text="输入", command=lambda:self.text01.insert(4.0,self.entry01.get()))
        self.btn02.pack(side="left") 

        # 创建一个Text
        self.text01 = Text(self,width=30, height=12,bg="black")
        self.text01.pack()
        self.text01.insert(1.0,"坚持就会胜利\n")
        self.text01.insert(3.0,"我是一个思想者，行动者！\n")
        self.text01['fg'] = "green"

        print(self.text01.get(2.0,END))

        # 创建一个画布并画点东西
        self.canvas = Canvas(self, width=300, height=200,bg="green")
        self.canvas.pack(side="left")
        self.canvas.create_line(10, 10, 30, 20, 40, 50)
        self.canvas.create_rectangle(50, 50, 100, 100)
        self.canvas.create_oval(50, 50, 100, 100)

        # 时间绑定测试
        self.btn01.bind("<Button-1>", self.btnClick01)
        self.btn02.bind("<Button-1>", self.btnClick02)

        self.btnQuit.bind_class("Button","<Button-1>", self.allBtnClick)

    
    def show_msg(self):
        messagebox.showinfo("消息","恭喜你被百度选中为优质客户！")
    
    def btnClick01(self,event):
        print("按钮01被点击了") 
        print(event.widget)
    def btnClick02(self,event):
        print("按钮02被点击了") 
        print(event.widget)
    # 经过测试发现btn01的command事件被阻止了
    def allBtnClick(self,event):
        print("你点击了一个按钮")
        print(event.widget) 

# 对模块进行测试
if __name__ == '__main__':
    root = Tk()
    root.geometry("800x600+300+300") 
    root.title("一个经典的GUI程序类") 
    app = App(root=root) 
    root.mainloop()