""" Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

________________

speed
O(N)
"""
from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        elem_dict = {}

        for elem in nums:
            prev_val = elem_dict.get(elem, 0)
            if prev_val > 0:
                del elem_dict[elem]
            else:
                elem_dict[elem] = elem_dict.get(elem, 0) + 1

        return list(elem_dict.keys())[0]
        

print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([1]))
