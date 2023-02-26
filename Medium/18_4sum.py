""" Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

________________

speed
O(N^3)
"""


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = set()
        nums = sorted(nums)

        for idx_1 in range(len(nums)):

            for idx_2 in range(idx_1 + 1, len(nums)):

                left_pointer = idx_2 + 1
                right_pointer = len(nums) - 1

                while left_pointer < right_pointer:
                    quadruplet = (nums[idx_1], nums[idx_2], nums[left_pointer], nums[right_pointer])
                    quadruplet_sum = sum(quadruplet) 

                    if quadruplet_sum > target:
                        right_pointer -= 1
                    elif quadruplet_sum < target:
                        left_pointer += 1
                    else:
                        quadruplets.add(quadruplet)

                        while nums[left_pointer] == quadruplet[2] and left_pointer < right_pointer:
                            left_pointer += 1
                        while nums[right_pointer] == quadruplet[3] and left_pointer < right_pointer:
                            right_pointer -= 1

        return list(quadruplets)


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2, 2], 8))
