""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

________________

speed
O(N^2)
"""
from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, item in enumerate(nums):
            for i, el in enumerate(nums[idx+1:], start = idx + 1):
                if item + el == target:
                    return [idx, i]
                    

print(Solution().twoSum([2, 7, 11, 15], 9))
print(Solution().twoSum([3, 2, 4], 6))
print(Solution().twoSum([3, 3], 6))
