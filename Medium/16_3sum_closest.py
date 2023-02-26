""" Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

________________

speed
O(N^2)
"""


class Solution:

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        best_sum = float("inf")
        
        for idx, val in enumerate(nums):

            left_pointer = idx + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                triplet = (val, nums[left_pointer], nums[right_pointer])
                triplet_sum = sum(triplet)

                if triplet_sum < target:
                    left_pointer += 1
                elif triplet_sum > target:
                    right_pointer -= 1
                else:
                    return triplet_sum

                if abs(triplet_sum - target) < abs(best_sum - target):
                    best_sum = triplet_sum

        return best_sum


print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
print(Solution().threeSumClosest([0, 0, 0], 1))
