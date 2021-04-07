import pygame
pygame.init()
th_long=4#格子长
th_wide=4#格子宽
minus=2.5#中间容差
block_long=100#实际显示长度
P_generate2=0.9#产生2的概率，精确到两位小数
max_regret=10#最大悔步步数
P_generate4=1-P_generate2
choice=[2]*int(P_generate2*100)+[4]*int(P_generate4*100)
rect_long=block_long-2*minus
screen_long=block_long*th_long
screen_wide=block_long*th_wide
font_size=block_long//2
font1=pygame.font.SysFont("arial",font_size)
back_color=(187,173,160)
color0=(200,189,178)
color2=(228,219,208)
color4=(227,216,195)
color8=(231,180,135)
color16=(233,159,119)
color32=(234,140,115)
color64=(234,118,88)
color_bigger=(227,201,117)
color_dict={0:color0,2:color2,4:color4,
            8:color8,16:color16,32:color32,
            64:color64,"bigger":color_bigger}

screen = pygame.display.set_mode((screen_long,screen_wide))
screen.fill(back_color)

