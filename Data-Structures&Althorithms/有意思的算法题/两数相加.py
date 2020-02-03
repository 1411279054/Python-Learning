# -*- coding: utf-8 -*- 
# @Time : 2020/2/3 22:30 
# @Author : LiChao
# @File : 两数相加.py
#题目：
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p,q = l1,l2 #使用变量p,q指向链表l1,l2
        new_ld = ListNode(0) #新建立一个链表，用于输出值
        pt = new_ld #使用变量pt 指向
        carry = 0   #用于当相加进位时
        while p != None or q != None:
            x = p.val if p != None else 0
            y = q.val if q != None else 0
            sum = carry +x +y
            carry = sum // 10
            pt.next = ListNode(sum%10)
            pt = pt.next
            if (p!=None): p = p.next
            if (q!=None): q = q.next
        if carry>0:
            pt.next = ListNode(carry)
        return new_ld.next
