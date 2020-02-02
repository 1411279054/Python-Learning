# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 15:24 
# @Author : LiChao
# @File : 整数反转.py 


#题目：给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    rev = 0
    if x > 0:
        while x != 0:
            pop = x % 10
            x = x // 10
            if rev > 214748364 or (rev == 214748364 and pop > 7): return 0
            if rev < -214748364 or (rev == -214748364 and pop < -8): return 0
            rev = rev * 10 + pop
        return rev
    else:
        x = -x
        while x != 0:
            pop = x % 10
            x = x // 10
            if rev > 214748364 or (rev == 214748364 and pop > 7): return 0
            if rev < -214748364 or (rev == -214748364 and pop < -8): return 0
            rev = rev * 10 + pop
        return -rev
result = reverse(-120)
print(result)