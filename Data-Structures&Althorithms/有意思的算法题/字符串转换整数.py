# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 16:10 
# @Author : LiChao
# @File : 字符串转换整数.py 

#请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
def myAtoi(str: str) -> int:
    new_str = list(str.lstrip())
    num = []
    result = ''
    symbol = 1
    if len(new_str)==0:
        return 0
    if new_str[0] == '+':
        symbol = 1
        del new_str[0]
    elif new_str[0] == '-':
        symbol = -1
        del new_str[0]
    elif not (new_str[0]<='9' and new_str[0]>='0'):
        return 0
    for i in new_str:
        if i >= '0' and i <= '9':
            num.append(i)
        else:
            break
    for i in range(len(num)):
        if num[0] == '0':
            del num[0]
        else:
            break
    for j in num:
        result += j
    if len(result) ==0 :
        return 0
    if symbol == -1:
        result = symbol * eval(result)
    else:
        result = eval(result)
    if result < -2 ** 31:
        return -2 ** 31
    elif result > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return result
# strs = "  0000000000012345678"
# result = myAtoi(strs)
# print(result)

##一行正则表达式解决问题
import re
def myAtoi(s: str) -> int:
    return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2 ** 31 - 1), -2 ** 31)

result2=myAtoi(s)
print(result2)
