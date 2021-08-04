#导入库
import os
import sys
#打印欢迎语
print("Jvav0.0.1在电脑上，输入一个Jvav文件名来开始：")
while True:
    filename = input("@")
    #如果输入“quit()”就退出程序
    if filename == "quit()":
        break
    elif not (".jvav" in filename):
        print("……你输入的貌似不是一个Jvav文件名喔！")
        #跳过本次循环
        continue
    #尝试打开用户所输入的文件
    try:
        file = open(filename,mode="r")
        file.close()
        #你 被 骗 了
        print("开始运行：")
        print("============================================================")
        input("按下任意键继续……")
        print("============================================================")
        print("运行结束。")
        continue
    #如果打不开就提示用户不存在此文件
    except:
        print("错误：文件不存在喔")
        continue
sys.exit()
