class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lenght = ''
        min_len = min(list(map(len, strs)))
        if min_len == 0:
            return ''
        else:
            for idx in range(min_len):
                items = [self.get_i_pos(item, idx) for item in strs]
                intersec = len(set(items))
                print(items, intersec)
                if idx == 0 and intersec == 0:
                    return ''
                elif intersec == 1:
                    lenght += items[0]
                else:
                    break
            return lenght

    def get_i_pos(self, string, i):
        return string[i]
