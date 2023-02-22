"""
Given an integer x, return true if x is a palindrome, and false otherwise.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        if x < 0:
            return False
        elif str(x) == ''.join(x_list[::-1]):
            return True
        else:
            return False
