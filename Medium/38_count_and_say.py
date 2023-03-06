""" The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. 
Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

Given a positive integer n, return the nth term of the count-and-say sequence.

________________

speed
O(N^2)
"""


class Solution:

    def say(self, digit: str) -> str:
        new_s, cnt, pointer = "", 0, digit[0]
        for idx in range(len(digit)):
            if digit[idx] == pointer:
                cnt += 1
            else:
                new_s += str(cnt) + pointer
                cnt, pointer = 1, digit[idx]
        new_s += str(cnt) + pointer
        return new_s

    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            s = self.say(s)
        return s


print(Solution().countAndSay(1))
print(Solution().countAndSay(4))
