# -*- coding: utf-8 -*- 
# @Time : 2020/3/1 20:25 
# @Author : LiChao
# @File : 删除排序数组重复项.py 
class Solution:
    def removeDuplicates(self, nums):
        sets = []
        for i in nums:
            if i not in sets:
                sets.append(i)
        lists = list(sets)
        nums[:len(lists)] = lists
        print(nums)
        print(lists)
        return len(lists)
def main():
    a = [-1,0,0,0,0,3,3]
    result = Solution().removeDuplicates(a)
    print(result)
if __name__ == '__main__':
    main()