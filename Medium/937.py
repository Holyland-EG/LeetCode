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
        