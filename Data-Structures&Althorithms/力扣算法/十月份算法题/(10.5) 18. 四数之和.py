class Solution:
    def fourSum(self, nums, target) :
        nums.sort()
        res = []
        if len(nums)<4:
            return res
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                start,end = j+1,len(nums)-1
                while start < end :
                    num = nums[start] + nums[end] + nums[i] + nums[j]
                    if num == target and  [nums[i], nums[j], nums[start], nums[end]]  not in res:
                        res.append([nums[i], nums[j], nums[start], nums[end]])
                        # while(start<end and nums[start]==nums[start+1]):
                        #     start +=1
                        # while(start<end and nums[end]==nums[end-1]):
                        #     end -=1
                        start +=1
                        end -=1
                    elif num > target:
                        end -= 1
                    else:
                        start += 1
        return res
def main():
    nums = [1,1,1,1]
    target = 4
    result = Solution().fourSum(nums,target)
    print(result)
if __name__ == '__main__':
    main()
