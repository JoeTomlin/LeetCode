# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        L = 0

        for R in range(len(s)):
            count[s[R]] = count.get(s[R], 0) + 1
            max_freq = max(max_freq, count[s[R]])
            if (R - L + 1) - max_freq > k:
                count[s[L]] -= 1
                L += 1

        return len(s) - L