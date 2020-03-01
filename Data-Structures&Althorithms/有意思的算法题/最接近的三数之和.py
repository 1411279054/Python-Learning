# -*- coding: utf-8 -*- 
# @Time : 2020/3/1 14:00 
# @Author : LiChao
# @File : 最接近的三数之和.py 

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        ans = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-1):
            start,end = i+1,len(nums) -1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum   >  target:
                    end -=1
                elif sum < target:
                    start +=1
                else :
                    return sum
                if abs(target-ans) > abs(target-sum):
                    ans = sum
        return ans
def main():
    nums = [-1,2,1,-4]
    target = 3
    result = Solution().threeSumClosest(nums,target)
    print(result)
if __name__ == '__main__':
    main()


