"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
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
        