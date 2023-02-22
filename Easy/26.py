class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev_element = None
        for i in nums.copy():
            if i == prev_element:
                nums.remove(i)
            else:
                prev_element = i
        return len(nums)
