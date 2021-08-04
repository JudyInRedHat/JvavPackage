#导入必要的库
from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
#新建主窗口
window = Tk()
#初始化主窗口
window.title("Jvav编辑器——让您的智商降低")
window.geometry("550x650")
window.iconbitmap("icon.ico")
#————函数区————
#新建文件函数
def newFile():
    #获取用户的文本输入
    INPUT = text.get("0.0","end")
    #如果用户有输入，那么警告用户
    if len(INPUT) != 1:
        #弹出警告窗口
        fileMode = tkinter.messagebox.askyesno(title='你确定要新建文件吗？', message='如果你没有保存该文件，您的文件可能会丢失！')
    #否则直接将fileMode设为True
    else:
        fileMode = True
    #如果否，那么跳过
    if fileMode == False:
        pass
    #否则直接新建
    else:
        text.delete('1.0','end')
        window.title("Jvav编辑器——让您的智商降低")
def saveFile():
    #保存文件
    path = filedialog.asksaveasfilename(title="保存文件",filetypes=(("jvav files", "*.jvav"),))
    if path != "":
        #写入文件
        file = open(path,mode="w")
        INPUT = text.get("0.0","end")
        file.write(INPUT)
        file.close()
        #弹出保存成功信息
        tkinter.messagebox.showinfo(title='提示', message='保存成功！')
        window.title("Jvav文件-"+path)
#打开文件函数
def openFile():
    path = filedialog.askopenfilename(title="选择打开的文件",filetypes=(("jvav files", "*.jvav"),))
    if path != "":
        file = open(path,"r",encoding='utf-8')
        fileIn = file.read()
        file.close()
        #清空文本框
        text.delete('1.0','end')
        #把内容写入到文本框
        text.insert(END,fileIn)
        #设置窗口名
        window.title('Jvav文件-'+path)
#————分割线————
#新建菜单栏
menuBar = Menu(window)
#创建一个文件菜单项
file=Menu(menuBar,tearoff=0)
#菜单栏里有小菜单
file.add_command(label="新建",command=newFile)
file.add_command(label="保存",command=saveFile)
file.add_command(label="打开",command=openFile)
#显示菜单栏
menuBar.add_cascade(label="文件",menu=file)
window['menu']=menuBar
#创建一个滚动条
scroll = Scrollbar()
#创建全屏文本框
text = Text(window,height=640,fg="black",yscrollcommand=scroll.set)
scroll.pack(side=RIGHT,fill=Y)
text.pack()
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)
#窗口主循环
window.mainloop()
