""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

________________

speed
O(log(N+M))
"""
from typing import List


class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left_pointer = right_pointer = 0
        new_nums = []
        odd = (len(nums1) + len(nums2)) % 2 == 0

        while len(new_nums) <= (len(nums1) + len(nums2)) // 2:
            if left_pointer < len(nums1):
                if right_pointer < len(nums2):
                    if nums1[left_pointer] < nums2[right_pointer]:
                        new_nums.append(nums1[left_pointer])
                        left_pointer += 1
                    else:
                        new_nums.append(nums2[right_pointer])
                        right_pointer += 1
                else:
                    new_nums.append(nums1[left_pointer])
                    left_pointer += 1
            else:
                if right_pointer < len(nums2):
                    new_nums.append(nums2[right_pointer])
                    right_pointer += 1
                else:
                    break
                
        return new_nums[-1] if not odd else (new_nums[-1] + new_nums[-2]) / 2


print(Solution().findMedianSortedArrays([1,3], [2]))
print(Solution().findMedianSortedArrays([1,2], [3,4]))
