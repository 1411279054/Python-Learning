# -*- coding: utf-8 -*- 
# @Time : 2020/2/2 10:21 
# @Author : LiChao
# @File : P-1.31.py 

def transaction(pay,money):
    if money < pay:
        print("你所支付的钱不够")
    else:
        money_list = [] #应找零钱的列表
        price = money - pay #支付钱减去需要支付的钱的差价
        while price > 0.001:
            if price > 50:
                money_list.append("50元")
                price -= 50
            elif price > 20:
                money_list.append("20元")
                price -= 20
            elif price > 10:
                money_list.append("10元")
                price -=10
            elif price > 5:
                money_list.append("5元")
                price -=5
            elif price > 1:
                money_list.append("1元")
                price -= 1
            elif price > 0.5:
                money_list.append("0.5元")
                price -=0.5
            elif price > 0.0999:#在pycharm编译器中0.1储存为0.0999999999999943
                money_list.append("0.1元")
                price -= 0.999
    return money_list
pay = 76.4
money = 100
result = transaction(pay,money)
print(result)