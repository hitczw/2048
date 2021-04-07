from sys import exit
from pygame.locals import *
from core import*
from collections import*
print('''欢迎来到2048游戏界面
按空格键返回上一步
按R键重新开始
Programmed by hitczw
''')
#加入锁死判断功能
game_exam=game2048()
while(1):
    for e in pygame.event.get():
        if e.type==QUIT:#检测到退出则退出游戏
            exit()
        elif e.type==KEYDOWN:
            #print(e.key)
            #以下可采用字典进行简化,为更明了分开写
            if(e.key==273):
                game_exam.event_deal("up")
            elif(e.key==274):
                game_exam.event_deal("down")
            elif(e.key==275):
                game_exam.event_deal("right")
            elif(e.key==276):
                game_exam.event_deal("left")
            elif(e.key==114):#按空格键返回上一步
                game_exam.__init__()
            elif(e.key==32):#按下R键重新开始
                game_exam.reg()

    game_exam.draw()#界面绘制

    pygame.display.update()  # 刷新界面

