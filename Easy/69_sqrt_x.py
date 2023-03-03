""" Given a non-negative integer x, return the square root of x rounded down to the nearest integer. 
The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

________________

speed
O(log(N))
"""


class Solution:

    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            m = (l + r) // 2
            if m*m <= x < (m+1)*(m+1):
                return m
            elif m*m > x:
                r = m
            else:
                l = m + 1                


print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(1))
print(Solution().mySqrt(0))
