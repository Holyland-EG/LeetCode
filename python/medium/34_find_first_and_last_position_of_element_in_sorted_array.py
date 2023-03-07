""" Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

________________

speed
O(log(N))
"""
from typing import List


class Solution:

    def leftSearch(self, l: int, r: int, nums: List[int], target: int) -> int:
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l

    def rightSearch(self, l: int, r: int, nums: List[int], target: int) -> int:
        while l < r:
            m = (l + r + 1) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m - 1
        return r

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        args = (nums, target)
        first, second = self.leftSearch(l, r, *args), self.rightSearch(l, r, *args)
        return [first, second] if first <= second and (nums[first] == nums[second] == target) else [-1, -1]


print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 5))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 6))
print(Solution().searchRange([5, 6, 7, 7, 8, 8, 10], 8))
print(Solution().searchRange([], 0))
print(Solution().searchRange([1], 1))
print(Solution().searchRange([1], 0))
