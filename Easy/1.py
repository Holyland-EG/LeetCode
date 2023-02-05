class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, item in enumerate(nums):
            for i, el in enumerate(nums[idx+1:], start = idx + 1):
                if item + el == target:
                    return [idx, i]
                    