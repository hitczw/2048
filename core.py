from constant import*
import random
from copy import deepcopy
class game2048():
    def __init__(self):
        self.long=th_long#游戏格子长度个数
        self.wide=th_wide#游戏格子宽度个数
        self.block_long=block_long#游戏底盘格子大小
        self.rect_long=rect_long#实际格子大小
        self.minus=minus#容差
        self.choice_lyst=choice
        self.max_regret=max_regret
        self.color_dict=color_dict
        self.screen=screen
        self.font1=font1
        self.font_size=font_size
        self.init_matrix()
        self.regret=[deepcopy(self.matrix)]
        self.score=0
        self.score_lyst=[self.score]
    def init_matrix(self):#初始化矩阵
        self.matrix=[[0 for i in range(self.long)]
                     for j in range(self.wide)]
        point1=self.generate_point()#生成第一个点
        point2=self.generate_point()#生成第二个点
        while(point1==point2):#第一个点等于第二个点,重新生成第二个点
            point2=self.generate_point()
        self.matrix[point1[1]][point1[0]]=2
        self.matrix[point2[1]][point2[0]]=2
        return
    def generate_point(self):#生成随机点
        x=random.randint(0,self.long-1)
        y=random.randint(0,self.wide-1)
        return [x,y]


    def deal_lyst(self,lyst):#按游戏规则对列表进行处理
        result1=[]
        result2=[]
        th=0
        for number in lyst:#让元素紧密的挨在一起
            if(number==0):#等于0,遍历下一个
                continue
            result1=result1+[number]#不为0,记录结果

        while(th<=len(result1)-1):#遍历到最后一个元素
            if(th==len(result1)-1):
                result2=result2+[result1[th]]
                break
            first=result1[th]
            second=result1[th+1]
            if(first==second):#两个元素相等
                result2=result2+[first+second]#进行相加操作
                th=th+2#往上进行两格
                self.score=self.score+first+second
                continue
            #两个元素不相等
            result2=result2+[first]
            th=th+1
        result2=result2+[0]*(len(lyst)-len(result2))#补齐剩余0元素
        return result2
    @staticmethod
    def reverse_lyst(lyst):#对列表进行翻转操作
        result=deepcopy(lyst)
        for i in range(len(lyst)//2):
            result[i],result[len(result)-1-i]=\
            result[len(result)-1-i],result[i]
        return result


    def event_deal(self,direction):#事件处理,对上下左右进行处理
        before=deepcopy(self.matrix)
        if(direction=="down" or direction=="up"):
            for j in range(0,self.long):#遍历每一列
                column=[i[j] for i in self.matrix]#取这一列元素
                if(direction=="down"):
                    column=self.reverse_lyst(column)
                column=self.deal_lyst(column)#得到处理后的元素
                if(direction=="down"):
                    column=self.reverse_lyst(column)
                for k in range(self.wide):
                    self.matrix[k][j]=column[k]
        elif(direction=="right" or direction=="left"):
            for row_matrix in self.matrix:#遍历每一行
                row=deepcopy(row_matrix)
                if(direction=="right"):
                    row=self.reverse_lyst(row)
                row=self.deal_lyst(row)#对行进行处理
                if(direction=="right"):
                    row=self.reverse_lyst(row)
                #进行赋值
                for j in range(self.long):
                    row_matrix[j]=row[j]
        if(before==self.matrix):#滑动前后相同
            #不产生新数字,返回
            return

        new_number=random.choice(self.choice_lyst)
        newpoint=self.generate_point()
        while(self.matrix[newpoint[1]][newpoint[0]]!=0):
            newpoint = self.generate_point()

        self.matrix[newpoint[1]][newpoint[0]]=new_number
        self.regret = self.regret + [deepcopy(self.matrix)]
        self.score_lyst=self.score_lyst+[self.score]
        if(len(self.regret)>self.max_regret+1):
            del self.regret[0]
            del self.score_lyst[0]

        return
    def draw(self):
        pygame.display.set_caption("分数:%d"%self.score)
        for x in range(self.wide):
            for y in range(self.long):
                rectpos1=y*self.block_long+self.minus
                rectpos2=x*self.block_long+self.minus
                value=self.matrix[x][y]
                if(value<=64):
                    color=self.color_dict[value]#根据值计算颜色
                else:
                    color=self.color_dict["bigger"]

                pygame.draw.rect(self.screen,
                                 color,
                                 (rectpos1, rectpos2,
                                  self.rect_long, self.rect_long),
                                 0)#绘制底部颜色
                #print(rectpos1, rectpos2)
                #print(rectpos1 + self.rect_long,rectpos2 + self.rect_long)

                if(value==0):
                    continue#数字0不进行绘制
                if(value<=4):
                    text_color=(50,50,50)
                else:
                    text_color=(255,255,255)

                text=self.font1.render(str(value) , True, text_color)
                long=len(str(value))
                x1=rectpos1+(self.rect_long-self.font_size)//1.1-long*self.font_size//5
                y1=rectpos2+(self.rect_long-self.font_size)//2.5
                self.screen.blit(text, [x1,y1])
        return
    def reg(self):
        if(len(self.regret)==1):
            #self.__init__()
            return
        self.matrix=deepcopy(self.regret[-2])
        del self.regret[-1]
        del self.score_lyst[-1]
        self.score=self.score_lyst[-1]













