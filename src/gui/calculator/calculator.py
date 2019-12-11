import tkinter
import math

class Calculator(tkinter.Frame):

    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.result=0
        self.numbers=[]
        self.operators= [] # 操作符
        self.needOper = False # =号后需要输入一个运算符
        self.pack()
        self.createWidget()
    def createWidget(self):

        btnText = (("MC","M+","M-","MR"),
        ("C","±","/","*"),
        (7,8,9,"-"),
        (4,5,6,"+"),
        (1,2,3,"="),
        (0,"."))
        # 第一行显示器
        self.shower = tkinter.Label(self,bg='yellow',width=42,height=2)
        self.shower['text'] = ''
        self.current_num = ''
        self.shower.grid(row=0,column=0,columnspan=4,pady=10)
        # 从第二行开始布局按钮
        for tindex,t in enumerate(btnText):
            for dindex,k in enumerate(t):
                if k == "=":
                    self.eqBtn = tkinter.Button(self,text=k,width=8)
                    self.eqBtn.grid(row=tindex+1,column=dindex,rowspan=2,sticky=tkinter.NSEW)
                elif k == 0:
                    tkinter.Button(self,text=k,width=8)\
                    .grid(row=tindex+1,column=dindex,columnspan=2,sticky=tkinter.NSEW)
                elif k == ".":
                    tkinter.Button(self,text=k,width=8)\
                    .grid(row=tindex+1,column=dindex+1,sticky=tkinter.NSEW)
                else:
                    tkinter.Button(self,text=k,width=8)\
                    .grid(row=tindex+1,column=dindex,sticky=tkinter.NSEW)

        self.eqBtn.bind_class('Button','<Button-1>',self.input)        
        tkinter.Label(self,text="科学计算器，实现了加减乘除").grid(row=7,column=0,columnspan=4,pady=10)
        self.tip = tkinter.Label(self,text="提示: 使用愉快！")
        self.tip.grid(row=8,column=0,columnspan=4,pady=10)

    def count(self):
        self.current_num = str(eval(self.shower['text']))
        self.shower['text'] = str(self.current_num)
        self.operators = []
        self.numbers = [self.current_num]
        self.needOper = True
    def input(self,event):
        widget = event.widget
        inputText = widget['text']
        print(type(inputText))
        if inputText in ['+','-','*','/']:
            if(self.current_num == ''):
                self.tip['text'] = '提示：没有可以运算的数!'
                return        
            self.numbers.append(self.current_num)
            self.operators.append(inputText)
            self.current_num = ''
            self.shower['text'] = self.shower['text'] + str(inputText)
            self.needOper = False
        elif inputText == '=':
            if len(self.operators) > 0:
                self.count()
            else:
                self.tip['text'] = '提示：连续点等号有意思吗!'
        elif inputText == '.':
            if self.needOper:
                self.tip['text'] = '提示：当前是上次运算结果，需要一个运算符！！！'
                return
            if '.' in self.current_num:
                self.tip['text'] = '提示：小数点太多了!'
                return
            self.current_num = '0.' if self.current_num == '' else self.current_num +'.'
            self.shower['text'] = '0.' if self.shower['text'] == '' else self.shower['text']+'.'
        elif inputText in ["MC","M+","M-","MR","±"]:
            self.tip['text'] = '提示：功能太强大,暂时实现不了!'
        elif inputText == 'C':
            self.current_num = ''
            self.numbers = []
            self.operators = []
            self.shower['text'] = ''
            self.needOper = False
        else:
            if self.needOper:
                self.tip['text'] = '提示：当前是上次运算结果，需要一个运算符！！！'
                return
            self.current_num = self.current_num + str(inputText)
            self.shower['text'] = self.shower['text'] + str(inputText)
    def input_oper(self):
        pass
    def clearResult(self):
        pass
    def clearInput(self):
        pass

root = tkinter.Tk()
root.title('超级科学计算器') 
root.geometry("400x600+200+300")
app = Calculator(root=root)
root.mainloop()