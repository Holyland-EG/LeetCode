""" A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and 
removing all non-alphanumeric characters, it reads the same forward and backward. 
Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

________________

speed
O(2*N)
"""
import string 


valid_characters = string.ascii_lowercase + string.digits


class Solution:

    @staticmethod
    def cleanChar(c: str) -> str:
        c = c.lower()
        return "" if c not in valid_characters else c

    def isPalindrome(self, s: str) -> bool:
        s = "".join(list(map(self.cleanChar, s)))
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] == s[right_pointer]:
                left_pointer += 1
                right_pointer -= 1
            else:
                return False
        return True


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome(" "))
