#!/usr/bin/python
# -*- coding:UTF-8 -*-

import random
while 1:
    s = int(random.randint(1,3))
    if s==1:
        ind = "石头"
    elif s ==2:
        ind = "剪子"
    elif s==3:
        ind = "布"
    m=input('输入 石头、剪子、布，输入end结束游戏：')
    blist = ['石头','剪子','布']
    if (m not in blist) and (m!='end'):
        print('input error')
    elif m =='end' :
        print('end...')
        break
    elif m==ind :
        print('电脑出了：'+ ind +'，平局')
    elif (m =='石头' and ind =='布') or (m == '布' and ind == '剪子') or (m=='剪子' and ind =='石头'):
        print('电脑出了：' + ind + '，你输了')
    elif (m =='布' and ind == '石头') or (m == '剪子' and ind == '布') or (m== '石头' and ind =='剪子'):
        print('电脑出了：' + ind + '，你赢了')