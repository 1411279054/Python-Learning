# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 11:38 
# @Author : LiChao
# @File : C-1.33.py 
def calculator2():
    temp = input("please,put the expression:").split(' ')
    num1 = eval(temp[0])
    symbol = temp[1]
    num2 = eval(temp[2])
    if symbol == '+':
        answer = num1 + num2
    elif symbol == '-':
        answer = num1 - num2
    elif symbol == '*':
        answer = num1 * num2
    elif symbol == '>>':
        answer = num1 >> num2
    elif symbol == '<<':
        answer = num1 << num2
    elif symbol == '>':
        answer = num1 > num2
    elif symbol == '==':
        answer = num1 == num2
    elif symbol == '<':
        answer = num1 < num2
    elif symbol == '>=':
        answer = num1 >= num2
    elif symbol == '<':
        answer = num1 <= num2
    print(answer)

calculator2()