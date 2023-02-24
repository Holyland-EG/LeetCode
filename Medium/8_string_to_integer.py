""" Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. 
Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. 
Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

_________

speed
O(N)
"""


all_nums = "0123456789"


class Solution:

    def myAtoi(self, s: str) -> int:
        left_border = -2**31
        right_border = 2**31 - 1
        
        s = s.strip()

        num = ""
        sign = 1
        
        for idx, i in enumerate(s):

            if i in all_nums:
                num += i
            elif idx == 0 and len(s) > idx+1 and i in "+-" and s[idx + 1] in all_nums:
                sign = -1 if i == "-" else 1
            else:
                break
            
        if num:
            if sign < 0:
                return max(left_border, int(num) * sign)
            else:
                return min(right_border, int(num) * sign)
        return 0


print(Solution.myAtoi("42"))
print(Solution.myAtoi("   -42"))
print(Solution.myAtoi("4193 with words"))
print(Solution.myAtoi("h42"))
print(Solution.myAtoi("+-12"))
print(Solution.myAtoi("-+12"))
print(Solution.myAtoi(""))
