""" Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

________________

speed
O(N)
"""
from typing import List


class Solution:

    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums) + 1)*(len(nums) / 2) - sum(nums))


print(Solution().missingNumber([3,0,1]))
print(Solution().missingNumber([0,1]))
print(Solution().missingNumber([9,6,4,2,3,5,7,0,1]))
