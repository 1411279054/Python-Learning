# -*- coding: utf-8 -*- 
# @Time : 2020/2/1 21:36 
# @Author : LiChao
# @File : 两数之和.py

#方法一：利用list函数求解
def twosum(nums,target):
    j = -1
    for i in range(len(nums)):
        temp = nums[:i]
        if target - nums[i] in temp:
            j = temp.index(target-nums[i])
            break
    if j >=0:
        return i,j
nums = [1,-2,-3,-4,-5,6]
target = 7
print(twosum(nums,target))
#方法二：哈希求解，字典模拟哈希求解
def twoSum(nums, target):
    hashmap={}
    for ind,num in enumerate(nums):
        hashmap[num] = ind
    for i,num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i!=j:
            return [i,j]