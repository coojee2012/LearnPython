
from tkinter.filedialog import asksaveasfilename

def newfile(textpad):
    textpad.delete('1.0','end') #把Text控件中的内容清空 
    filename = asksaveasfilename(title='另存为', 
    initialfile='未命名.txt',
    filetypes=[("文本文档", "*.txt")],
     defaultextension='.txt')
    return filename

def savefile():
    pass

def exit():
    pass

def openfile():
    pass