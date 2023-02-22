roman_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

class Solution:

    def romanToInt(self, s: str) -> int:
        integers = []
        for num in s:
            num = roman_map.get(num)
            if len(integers) > 0 and integers[-1] < num:
                integers[-1] = num - integers[-1]
            else:
                integers.append(num)

        return sum(integers)
