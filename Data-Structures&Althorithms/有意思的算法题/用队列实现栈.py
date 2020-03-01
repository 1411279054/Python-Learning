# -*- coding: utf-8 -*- 
# @Time : 2020/3/1 13:27 
# @Author : LiChao
# @File : 用队列实现栈.py
import  queue
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = queue.LifoQueue()
        self.length = 0
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.stack.put(x)
        self.length +=1
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self.length:
            result = self.stack.get()
            return result
        else:
            return False
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.length:
            result = self.stack.get()
            self.stack.put(result)
            return result
        else:
            return False
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()
demo = MyStack()
demo.push(3)
demo.push(2)

result = demo.pop()
result2 = demo.top()
result3 = demo.pop()

print(result,result2,result3)