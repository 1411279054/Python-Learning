# -*- coding: utf-8 -*- 
# @Time : 2020/2/23 16:59 
# @Author : LiChao
# @File : 盛水最多的容器.py

'''
题目描述：
给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

'''
class Solution:
    #1.暴力法（不推荐）
    # def maxArea(self, height):
    #     max = 0
    #     for i in range(len(height)):
    #         for j in range(i,len(height)):
    #             if height[i] >= height[j] and max < height[j]*(j-i):
    #                 max = height[j]*(j-i)
    #             elif height[i] < height[j] and max < height[i]*(j-i):
    #                 max = height[i] *(j-i)
    #     return max
    def maxArea(self, height):
        maxare=0
        left,right=0,len(height)-1 #左右指针 分别指向开头和末尾
        while left<=right:
            maxare = max(maxare,min(height[left],height[right])*(right-left))
            if height[left]<height[right]:
                left +=1
            else: right -=1
        return maxare
if __name__ == '__main__':
    height = [2,3,4,5,18,17,6]
    print(Solution().maxArea(height))

