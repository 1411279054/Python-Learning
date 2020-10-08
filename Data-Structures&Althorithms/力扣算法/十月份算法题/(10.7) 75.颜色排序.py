class Solution:
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort()
        pre = 0
        for i in range(len(nums)):
            if nums[i] == 0 :
                nums[i],nums[pre] = nums[pre],nums[i]
                pre = pre + 1
        for j in range(pre,len(nums)):
            if nums[j] == 1:
                nums[j], nums[pre] = nums[pre], nums[j]
                pre += 1
def main():
    nums =  [2, 0, 2, 1, 1, 0]
    Solution().sortColors(nums)
    print(nums)
if __name__ == '__main__':
    main()

