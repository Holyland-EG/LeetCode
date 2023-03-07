""" Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

________________

speed
O(N)
"""
from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        s = set("".join(strs))
        anagram_map = []

        for i in strs:
            anagram_map.append(" ".join([str(i.count(char)) for char in s]))

        d = defaultdict(list)
        for idx, i in enumerate(strs):
            d[anagram_map[idx]] = d.get(anagram_map[idx], []) + [i]

        return d.values()


print(Solution().groupAnagrams([""]))
print(Solution().groupAnagrams(["a"]))
print(Solution().groupAnagrams(["eat", "tea"]))
print(Solution().groupAnagrams(["", ""]))
print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(Solution().groupAnagrams(["abbbbbbbbbbb", "aaaaaaaaaaab"]))
