# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 10:41 
# @Author : LiChao
# @File : P-1.32.py 
def calculator():
    num =[]
    str1 = input("请输入：")
    temp = ['+','-',"*","/"]
    while  str1 != 'quit':
        if str1 in temp:
            num.append(str1)
        elif str1 == '=':
            if num[1] == '+':
                answer = eval(num[0]) + eval(num [2])
                print(answer)
                del num[:]
                num.append(str(answer))

            elif num[1] == '-':

                answer = eval(num[0]) - eval(num[2])
                print(answer)
                del num[:]
                num.append(str(answer))
            elif num[1] == '*':

                answer = eval(num[0]) * eval(num[2])
                print(answer)
                del num[:]
                num.append(str(answer))
            elif num[1] == '/':
                try:

                    answer = eval(num[0]) / eval(num[2])
                    print(answer)
                    del num[:]
                    num.append(str(answer))
                except ZeroDivisionError:
                    print("除数为零")
                    del num[1:]

        else:
            num.append(str1)
        str1 = input("请输入：")
calculator()