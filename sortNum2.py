class Solution (object):
    def sortNums2(self, nums):
        index, index1, index3 = 0, 0, len(nums)- 1
        while index <= index3:
            if nums[index] == 1:
                nums[index], nums[index1] = nums[index1], nums[index]
                index1 += 1
                index += 1
            elif nums[index] == 2:
                index += 1
            elif nums[index] == 3:
                nums[index3], nums[index] = nums[index], nums[index3]
                index3 -= 1
            print(nums)    
        return nums
print(Solution().sortNums2([3,3,2,1,3,2,1,1]))