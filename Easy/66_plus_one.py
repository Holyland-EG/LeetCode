""" You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

________________

speed
O(N)
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = int("".join(list(map(str, digits)))) + 1
        return list(map(int, list(str(digit))))
        

print(Solution.plusOne([1, 2, 3]))
print(Solution.plusOne([4, 3, 2, 1]))
print(Solution.plusOne([9]))
