""" There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

________________

speed 
O(log(N))
"""
from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left_pointer, right_pointer = 0, len(nums) - 1
        while left_pointer <= right_pointer:
            m = (right_pointer + left_pointer) // 2

            if nums[m] == target:
                return m
            elif nums[left_pointer] <= nums[m]:
                if nums[left_pointer] <= target < nums[m]:
                    right_pointer = m - 1
                else:
                    left_pointer = m + 1
            else:
                if nums[m] < target <= nums[right_pointer]:
                    left_pointer = m + 1
                else:
                    right_pointer = m - 1
        return -1


print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
print(Solution().search([1], 0))
print(Solution().search([1, 2, 3], 3))
print(Solution().search([1, 2, 3], 1))
