""" Given an integer x, return true if x is a palindrome, and false otherwise.

________________

speed 
O(N)
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

print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))
