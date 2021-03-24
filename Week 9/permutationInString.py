class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        if len(s1) > len(s2):
            return False
        for left in range(len(s2) - len(s1) + 1):
            right = left + len(s1)
            if s1 == sorted(s2[left:right]):
                return True
        return False
