class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                summa = nums[i] + nums[j]
                if summa == target and i != j:
                    return [i, j]


print(Solution().twoSum([2, 7, 11, 15], 9))

# Hahaha suck my balls
