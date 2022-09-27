from collections import defaultdict
class Solution (object):
    def twoSum(self, nums, target):
        hashMap = defaultdict(int)
        for i in nums:
            remaining = target - i 
            if i in hashMap:
                return [i, hashMap[i]]
            hashMap[remaining] = i
            
            
print(Solution().twoSum([1,3,4,5,9,6], 12))