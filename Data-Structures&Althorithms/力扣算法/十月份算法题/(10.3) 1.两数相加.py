class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        j = -1
        for i in range(len(nums)):
            temp = nums[:i]
            if target - nums[i] in temp:
                j = temp.index(target-nums[i])
                break
        if j >= 0:
            return i,j

x = [2,7,11,15]
Solution().twoSum(x,9)
