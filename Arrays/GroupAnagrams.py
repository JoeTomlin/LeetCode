# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key in ans:
                ans[key].append(s)
            else:
                ans[key] = [s]
        return list(ans.values())
      
# Time: O(n * k)    
# Space: O(n * k)   