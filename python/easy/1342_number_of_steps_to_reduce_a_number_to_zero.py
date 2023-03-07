""" Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

________________

speed
O(N)
"""


class Solution:
    
    @staticmethod
    def reduce_num(num: int) -> int:
        return {
            True: num / 2,
            False: num - 1
        }.get(num % 2 == 0)

    def numberOfSteps(self, num: int) -> int:
        opers = 0
        while num != 0:
            num = self.reduce_num(num)
            opers += 1
        return opers


print(Solution().numberOfSteps(14))
print(Solution().numberOfSteps(8))
print(Solution().numberOfSteps(123))
print(Solution().numberOfSteps(0))
        