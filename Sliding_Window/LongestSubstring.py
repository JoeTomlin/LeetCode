# Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        L = 0
        max_length = 0

        for R in range(len(s)):
            while s[R] in char_set:
                char_set.remove(s[L])
                L += 1
            char_set.add(s[R])
            max_length = max(max_length, R - L + 1)

        return max_length