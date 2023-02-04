# def sum_in_list(nums, target):
#    for i in range(len(nums)):
#       for j in range(len(nums)):
#          if nums[i]+nums[j] == target and i != j:
#             print([i, j])
#    break


# print("Enter an amount of elements")
# n = int(input())
# certain_list = []
# for k in range(0, n):
#   print(f"Enter the element {k+1}")
#  elem = int(input())
# certain_list.append(elem)

# print("Now enter a desired number which will represent a sum of two elements")
# desired_number = int(input())

# sum_in_list(certain_list, desired_number)

class Solution(object):
    def twoSum(self, nums, target):
       for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j] == target and i != j:
                    print([i, j])
            break



Sol = Solution()

nums = list(input(),remove('[',']',','))
target = int(input())
Sol.twoSum(nums, target)
