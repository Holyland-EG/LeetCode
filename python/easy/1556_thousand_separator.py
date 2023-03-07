""" Given an integer n, add a dot (".") as the thousands separator and return it in string format.

________________

speed
O(N)
"""


class Solution:
	
    def thousandSeparator(self, n: int) -> str:
        if n >= 1000:
            n = list(str(n))
            i = -3
            while abs(i) < len(n):
                n[i:i] = '.'
                i -= 4
            return ''.join(n)
        return str(n)



print(Solution().thousandSeparator(987))
print(Solution().thousandSeparator(1234))
