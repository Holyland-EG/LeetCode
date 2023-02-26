""" Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

________________

speed
O(N^2)
"""


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        nums = sorted(nums)

        for idx, val in enumerate(nums):

            left_pointer = idx + 1
            right_pointer = len(nums) - 1

            while left_pointer < right_pointer:
                triplet = (nums[idx], nums[left_pointer], nums[right_pointer])
                triplet_sum = sum(triplet)

                if triplet_sum > 0:
                    right_pointer -= 1
                elif triplet_sum < 0:
                    left_pointer += 1
                else:
                    triplets.add(triplet)

                    while nums[left_pointer] == triplet[1] and left_pointer < right_pointer:
                        left_pointer += 1
                    while nums[right_pointer] == triplet[2] and left_pointer < right_pointer:
                        right_pointer -= 1

        return list(triplets)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 1, 1]))
print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-4, -3, -1, -1, 0, 1, 2, 5, 7]))
