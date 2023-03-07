""" Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

________________

speed 
O(N)
"""
from typing import List


class Solution:

    def validMountainArray(self, arr: List[int]) -> bool:
        has_a_peak = False
        has_lower = False
        prev_item = None
        for item in arr:
            if prev_item is None:
                prev_item = item
            else:
                if not has_a_peak and item > prev_item:
                    prev_item = item
                    has_lower = True
                elif not has_a_peak and has_lower and item < prev_item:
                    has_a_peak = True
                    prev_item = item
                elif has_a_peak and item < prev_item:
                    prev_item = item
                else:
                    return False
        if has_a_peak:
            return True
        else:
            return False


print(Solution().validMountainArray([2, 1]))
print(Solution().validMountainArray([3, 5, 5]))
print(Solution().validMountainArray([0, 3, 2, 1]))
