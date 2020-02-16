# -*- coding: utf-8 -*- 
# @Time : 2020/2/16 21:35 
# @Author : LiChao
# @File : 三数之和.py

#题目描述：
# 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。



#  自己第一次做的，不能排除重复的，菜。。。
# def threeSum(nums):
#     lists=[]
#     for a in range(len(nums)):
#         for b in range(a+1,len(nums)):
#             for c in range(b+1,len(nums)):
#                 if nums[a]+nums[b]+nums[c] == 0:
#                     sublist =[]
#                     sublist.append(nums[a])
#                     sublist.append(nums[b])
#                     sublist.append(nums[c])
#                     lists.append(sublist)
#     return lists

## 看了题解大佬后，在做的
def threeSum(nums):
    res = []
    if(len(nums)<3):
        return res
    nums.sort()
    for i in range(len(nums)):
        if nums[0] > 0:
            return res
        if nums[i] == nums[i-1] and i>0:
            continue
        R = len(nums) - 1
        L = i + 1
        while(L<R):
            if(nums[i]+nums[R]+nums[L] == 0):
                res.append([nums[i],nums[R],nums[L]])
                while(L<R and nums[L]==nums[L+1]):
                    L = L + 1
                while(L<R and nums[R]==nums[R-1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            elif(nums[i]+nums[R]+nums[L]>0):
                R = R-1
            else:
                L = L+1
    return res

def main():
    nums = [-1, 0, 1, 2, -1, -4]
    result = threeSum(nums)
    print(result)

if __name__ == '__main__':
    main()