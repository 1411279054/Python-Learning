# -*- coding: utf-8 -*- 
# @Time : 2020/3/1 15:46 
# @Author : LiChao
# @File : 删除链表倒数第n个元素.py 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lens = 0
        fp = head
        if head != None:
            prenum = head
            num = head.next
        while fp != None:
            fp = fp.next
            lens += 1
        sub = lens - n -1
        while sub != 0:
            num = num.next
            prenum = num.next
            sub -=1
        prenum.next = num.next
        return head
def main():
    head =(ListNode)[1,2,3,4,5]
    n = 2
    result = Solution().removeNthFromEnd(head,n)
    print(result)
if __name__ == '__main__':
    main()
