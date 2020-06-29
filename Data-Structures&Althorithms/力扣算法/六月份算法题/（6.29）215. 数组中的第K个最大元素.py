class Solution:
    def findKthLargest(self, nums,k):
        nums.sort()
        return nums[len(nums)-k]

def main():
    nums = [3,2,1,5,6,4]
    k = 2
    num = Solution().findKthLargest(nums, 2)
    print(num)
if __name__ == '__main__':
    main()