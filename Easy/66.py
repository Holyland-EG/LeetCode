class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join(list(map(str, digits)))) + 1
        return list(map(int, list(str(digit))))
        