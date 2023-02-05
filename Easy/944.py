class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([tuple(sorted(tuples)) != tuples for tuples in zip(*strs)])
