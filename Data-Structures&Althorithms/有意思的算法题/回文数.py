# -*- coding: utf-8 -*- 
# @Time : 2020/2/7 20:29 
# @Author : LiChao
# @File : 回文数.py 


##题目描述：输入5，输出：
# 1  2  3  4  5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9
def hui_wen_num(n):
    lists = [[] for j in range(n)]
    for row in range(n):
        for i in range(n):
            lists[i].append(0)
    count,maxX,maxY,minX,minY = 0,n-1,n-1,0,0
    while minX<=maxX:
        for x in range(minX,maxX+1):
            count +=1
            lists[minY][x] = count
        minY +=1
        for y in range(minY,maxY+1):
            count +=1
            lists[y][maxX] = count
        maxX -=1
        for x in range(maxX,minX-1,-1):
            count +=1
            lists[maxY][x] = count
        maxY -=1
        for y in range(maxY,minY-1,-1):
            count +=1
            lists[y][minX] = count
        minX +=1
    for i in lists:
        for j in i:
            print('{:<5d}'.format(j),end=' ')
        print()

hui_wen_num(5)