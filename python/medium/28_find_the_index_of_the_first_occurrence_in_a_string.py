""" Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

________________

speed
O(N^2)
"""


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack)):
            left_pointer = idx
            right_pointer = idx + 1
            while (right_pointer <= len(haystack) and 
                   haystack[left_pointer:right_pointer] == needle[:(right_pointer - left_pointer)]):
                if haystack[left_pointer:right_pointer] == needle:
                    return idx
                else:
                    right_pointer += 1
        return -1


print(Solution().strStr("sadbutsad", "sad"))
print(Solution().strStr("saddbutsad", "db"))
print(Solution().strStr("a", "a"))
