""" Given a string s, find the length of the longest substring without repeating characters.

________________

speed
O(N)
"""
from collections import defaultdict


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = defaultdict(int)
        longest = left_pointer = 0

        for right_pointer in range(len(s)):
            char = s[right_pointer]

            if charset.get(char, -1) < left_pointer:
                longest = max(longest, (right_pointer-left_pointer+1))
            else:
                left_pointer = charset[char] + 1

            charset[char] = right_pointer
        return longest


print(Solution().lengthOfLongestSubstring("abcabcbb"))
print(Solution().lengthOfLongestSubstring("bbbbb"))
print(Solution().lengthOfLongestSubstring("pwwkew"))
print(Solution().lengthOfLongestSubstring(""))
print(Solution().lengthOfLongestSubstring(" "))
