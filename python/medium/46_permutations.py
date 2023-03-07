""" Given an array nums of distinct integers, return all the possible permutations. 
You can return the answer in any order.

________________

speed
O(2^n)
"""
from typing import List


class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        def generatePerm(data): 
            if len(data) == 0:
                return []
            elif len(data) == 1:
                return [data]

            new_data = []
            for i in range(len(data)):
                data_slice = data[:i] + data[i+1:]
                for val in generatePerm(data_slice):
                    new_data.append([data[i]] + val)
            return new_data

        return generatePerm(nums)


print(Solution().permute([1, 2, 3]))
print(Solution().permute([0, 1]))
print(Solution().permute([1]))
