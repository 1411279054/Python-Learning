# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 20:51
# @Author : LiChao
# @File : C-1.28.py
def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for item in temp[::-1]:
        yield item
g = factors(100)
try:
    while True:
        print(next(g))
except Exception:
    pass