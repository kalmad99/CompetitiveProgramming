class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left, right = 0, 0
        if len(s) == 0:
            return True
        while right < len(t):
            if s[left] == t[right]:
                left += 1
                right += 1
            else:
                right += 1

            if left == len(s):
                return True

        return False