# -*- coding: utf-8 -*- 
# @Time : 2020-06-30 22:07 
# @Author : LiChao
# @File : （6.30）剑指 Offer 09. 用两个栈实现队列.py
import queue
class CQueue:
    def __init__(self):
        self.stack1 = queue.LifoQueue()
        self.stack2 = queue.LifoQueue()

    def appendTail(self, value: int) -> None:
        self.stack1.put(value)
    def deleteHead(self):
        if self.stack2.empty() == True:
            while not self.stack1.empty() :
                self.stack2.put(self.stack1.get())
        if self.stack2.empty():
            return  -1
        else:
            deleteItem = self.stack2.get()
            return deleteItem
stack1 = CQueue()
stack1.appendTail(1)
stack1.appendTail(2)
print(stack1.deleteHead())

# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()