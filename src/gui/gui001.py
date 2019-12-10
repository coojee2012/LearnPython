from tkinter import *
from tkinter import messagebox # 为什么要这样导入一次，前面已经有*了？

def btn_click(e):
    messagebox.showinfo("Message","按钮点击！")
    print("点击了按钮")

root = Tk(screenName="Hello World")
root.title("GUI开发练习") # 设置标题
root.geometry("500x400+100+200") # 设置画布大小
btn001 = Button(root)
btn001['text'] = "按钮一"
btn001.bind("<Button-1>",btn_click) 

btn001.pack() # 将按钮放在画布上

root.mainloop()