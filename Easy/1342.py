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
        