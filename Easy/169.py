""" 
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem_dict = {}

        for elem in nums:
            elem_dict[elem] = elem_dict.get(elem, 0) + 1

            if elem_dict[elem] > len(nums) / 2:
                return elem
