class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, answer = 0, 0, -1
        ans = set()
        for right in range(len(s)):
            while s[right] in ans:
                ans.remove(s[left])
                left += 1
            ans.add(s[right])
            answer = max(answer, right - left + 1)

        if answer == -1:
            return 0
        return answer