import tkinter
root = tkinter.Tk(screenName="Hello World")
root.title("GUI开发练习") # 设置标题
root.geometry("500x400+100+200") # 设置画布大小
btn001 = tkinter.Button(root)
btn001['text'] = "按钮一"
btn001.pack() # 将按钮放在画布上
root.mainloop()