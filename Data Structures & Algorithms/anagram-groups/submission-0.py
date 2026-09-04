class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       res = {}
       for word in strs:
         key = "".join(sorted(word))
         res.setdefault(key, []).append(word)
       return list(res.values())
