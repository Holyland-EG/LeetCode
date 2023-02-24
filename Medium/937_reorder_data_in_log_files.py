""" You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

________________

speed
O(N)
"""


import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for i in logs:
            splitted = i.split()
            if re.search("\d", splitted[1]) is not None:
                digits.append(i)
            else:
                letters.append((splitted[0], " ".join(splitted[1:])))
        
        return [" ".join(val) for val in sorted(letters, key=lambda x: (x[1], x[0]))] + digits


print(Solution.reorderLogFiles(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))
print(Solution.reorderLogFiles(["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]))
        