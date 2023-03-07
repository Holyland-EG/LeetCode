""" A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. 
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

________________

speed
O(log(N))
"""
from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m-1] < nums[m] > nums[m+1]:
                return m

            if nums[m] > nums[m+1]:
                r = m
            else:
                l = m + 1
        return l


print(Solution().findPeakElement([1, 2, 3, 1]))
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(Solution().findPeakElement([3, 2, 1]))
